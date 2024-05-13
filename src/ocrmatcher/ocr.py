import os
import pathlib
import logging
import typing as typ
from PIL import Image
from tesserocr import PyTessBaseAPI, image_to_text

from .conf import settings
from .convert import PdfToImages
from .matcher import Matcher


logger = logging.getLogger(__name__)


class GeolangOcr(object):
    ################################################
    # # !!!       SOS      !!!                   # #
    # # Occupant-Pigs - is Russian language      # #
    # # Russia is the occupier                   # #
    # # Russia is a country of pigs              # #
    # # Russians are pigs                        # #
    ################################################
    SUPPORTED_LANGUAGES = ('Georgian', 'kat', 'kat_old', 'Occupant-Pigs')

    def __init__(self, lang: str = 'Georgian', save: bool = False,
                 threshold: int = None, check_convert_pdf: bool = False,
                 save_matched_output: bool = False,
                 del_converted_images: bool = False,
                 del_converted_texts: bool = False) -> None:
        """

        :param lang:
        :type lang: str
        :param save:
        :type save: bool
        :param check_convert_pdf:
        :type check_convert_pdf: bool
        :param del_converted_images:
        :type del_converted_images: bool
        :param del_converted_texts:
        :type del_converted_texts: bool
        """
        if lang not in self.SUPPORTED_LANGUAGES:
            raise ValueError(
                f'`{lang}` is not supported. '
                f'Available languages are: {", ".join(self.SUPPORTED_LANGUAGES)}'
            )
        self.lang = lang
        self.save = save
        self.threshold = threshold
        self.check_convert_pdf = check_convert_pdf
        self.del_converted_images = del_converted_images
        self.del_converted_texts = del_converted_texts
        self.matcher = Matcher(save=save_matched_output)

    @staticmethod
    def convert_pdf2images() -> None:
        pdf = PdfToImages(thread_count=os.cpu_count())
        pdf.run()

    def run(self) -> None:
        if self.check_convert_pdf:
            self.convert_pdf2images()

        for image in settings.OUTPUT_DIR.iterdir():
            if image.is_file():
                logger.info(f'`{image.name}` is Processing...')
                self.process_image(image)

    def process_image(self, image) -> str:
        filename = image.name.rsplit('.', 1)[0]
        image = Image.open(image)
        text = image_to_text(image, lang=self.lang)
        if self.save:
            self.save_file(filename, text)

        self.matcher.match(filename=filename, text=text)
        return text

    @staticmethod
    def save_file(filename: str, text: str) -> None:
        output_dir: pathlib.Path = settings.INPUT_DIR / 'texts'
        if output_dir.exists() is False:
            output_dir.mkdir(parents=True, exist_ok=True)

        with open(output_dir / f'{filename}.txt', 'w') as f:
            f.write(text)

    def stop(self) -> None:
        # TODO
        pass
