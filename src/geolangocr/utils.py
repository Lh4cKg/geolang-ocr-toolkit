import re
import pathlib
import typing as typ
from pdf2image import convert_from_path

from .conf import settings


def pdf_to_image(
        pdf_path: pathlib.Path,
        output_folder: pathlib.Path,
        fmt: str = 'png',
        output_file: str = None,
        **kwargs: typ.Dict[str, typ.Any]
) -> None:
    if not isinstance(pdf_path, pathlib.Path):
        raise TypeError(f'`pdf_path` must be type of `pathlib.Path`')

    if pdf_path.suffix != '.pdf':
        raise ValueError(f'Unsupported file extension: `{pdf_path.suffix}`.')

    if output_folder.exists() is False or output_folder.is_dir() is False:
        raise FileNotFoundError(
            f'Output folder `{output_folder}` does not exists.'
        )

    if output_file is None:
        name = pdf_path.name.rsplit('.', 1)
        output_file = f'{name[0]}'
    convert_from_path(
        pdf_path=str(pdf_path),
        fmt=fmt,
        output_file=output_file,
        output_folder=output_folder,
        **kwargs
    )


def is_empty(_dir: pathlib.Path) -> bool:
    return not any(_dir.iterdir())


def add_keywords_txt(keywords: str) -> None:
    file: pathlib.Path = settings.CACHE_DIR / 'keywords.txt'
    if file.is_file() is False:
        file.touch()

    with open(file, 'a') as f:
        for keyword in re.split(r',|\s|\s+', keywords):
            f.write(f'{keyword}\n')
