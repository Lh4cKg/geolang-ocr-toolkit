import os
import logging
import pathlib
from dataclasses import dataclass


@dataclass
class Settings:
    """
    Settings class to store the settings for the Geolangocr project
    """

    BASE_DIR: pathlib.Path = pathlib.Path(__file__).resolve().parent
    try:
        INPUT_DIR: pathlib.Path = pathlib.Path(
            os.environ.get(
                'INPUT_DIR',
                BASE_DIR.parent.parent / 'dataset'
            )
        )
    except TypeError:
        raise EnvironmentError(f'Invalid `INPUT_DIR` environment value.')
    try:
        OUTPUT_DIR: pathlib.Path = pathlib.Path(
            os.environ.get(
                'OUTPUT_DIR',
                INPUT_DIR / 'images'
            )
        )
    except TypeError:
        raise EnvironmentError(f'Invalid `OUTPUT_DIR` environment value.')

    TESSDATA_PREFIX: pathlib.Path = BASE_DIR / 'tessdata'


settings = Settings()

# Configure Logging

logging.basicConfig(
    format='%(levelname)s %(asctime)s %(name)s %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S',
    level=logging.INFO
)

# Set Default Environment Variables

os.environ['TESSDATA_PREFIX'] = str(settings.TESSDATA_PREFIX)
