import pathlib
import logging
import typing as typ

from .conf import settings
from .utils import pdf_to_image


logger = logging.getLogger(__name__)


class PdfToImages:

    def __init__(self, **kwargs: typ.Any) -> None:
        """

        :param kwargs:
        :type kwargs: typ.Any
        """

        self.input_folder: pathlib.Path = settings.INPUT_DIR
        self.output_folder: pathlib.Path = settings.OUTPUT_DIR
        self.kwargs = kwargs

    def run(self) -> None:
        if self.input_folder.is_dir() is False:
            raise FileNotFoundError(
                f'Input folder `{self.input_folder}` does not exists.'
            )
        for file in self.input_folder.iterdir():
            if file.suffix != '.pdf':
                continue
            logger.info(f'{file.name} is processing...')
            pdf_to_image(file, self.output_folder, **self.kwargs)
