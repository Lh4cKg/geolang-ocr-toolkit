import pathlib
import logging
import typing as typ

from .conf import settings
from .utils import pdf_to_image


logger = logging.getLogger(__name__)


class PdfToImages:

    def __init__(
        self,
        input_folder: pathlib.Path = settings.INPUT_DIR,
        output_folder: pathlib.Path = settings.OUTPUT_DIR,
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
        self.input_folder = input_folder
        if not isinstance(self.input_folder, pathlib.Path):
            raise TypeError('`input_folder` must be a type of pathlib.Path')
        self.output_folder = output_folder
        if not isinstance(self.output_folder, pathlib.Path):
            raise TypeError('`output_folder` must be a type of pathlib.Path')

        if self.input_folder.is_dir() is False:
            self.input_folder.mkdir(parents=True, exist_ok=True)

        if self.output_folder.is_dir() is False:
            self.output_folder.mkdir(parents=True, exist_ok=True)

        self.kwargs = kwargs

    def execute(self) -> None:
        if self.input_folder.is_dir() is False:
            raise FileNotFoundError(
                f'Input folder `{self.input_folder}` does not exists.'
            )
        for file in self.input_folder.iterdir():
            if file.suffix != '.pdf':
                continue
            logger.info(f'{file.name} is processing...')
            pdf_to_image(file, self.output_folder, **self.kwargs)
