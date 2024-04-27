import pathlib
import logging
import typing as typ

from .conf import settings
from .utils import pdf_to_image


logger = logging.getLogger(__name__)


class PdfToImages:

    def __init__(
        self,
        input_folder: typ.Union[str, pathlib.Path] = None,
        output_folder: typ.Union[str, pathlib.Path] = None,
        **kwargs: typ.Any
    ) -> None:
        """

        :param input_folder:
        :type input_folder: pathlib.Path
        :param output_folder:
        :type output_folder: pathlib.Path
        :param kwargs:
        :type kwargs: typ.Any
        """

        if not input_folder:
            self.input_folder: pathlib.Path = settings.INPUT_DIR
        else:
            if isinstance(input_folder, pathlib.Path):
                self.input_folder = input_folder
            else:
                try:
                    self.input_folder = pathlib.Path(input_folder)
                except TypeError:
                    raise TypeError('Invalid `input_folder` type.')

        if not output_folder:
            self.output_folder: pathlib.Path = settings.OUTPUT_DIR
        else:
            if isinstance(output_folder, pathlib.Path):
                self.output_folder = output_folder
            else:
                try:
                    self.output_folder = pathlib.Path(output_folder)
                except TypeError:
                    raise TypeError(f'Invalid `output_folder` type.')

        if self.input_folder.is_dir() is False:
            self.input_folder.mkdir(parents=True, exist_ok=True)

        if self.output_folder.is_dir() is False:
            self.output_folder.mkdir(parents=True, exist_ok=True)

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
