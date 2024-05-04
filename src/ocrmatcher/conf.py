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
    CURRENT_DIR: pathlib.Path = pathlib.Path(os.getcwd()).resolve()
    # Levenshtein configuration
    LEVENSHTEIN_MATCH_THRESHOLD: int = 95
    TOKEN_FULL_PROCESS: bool = True

    try:
        INPUT_DIR: pathlib.Path = pathlib.Path(
            os.environ.get(
                'INPUT_DIR',
                CURRENT_DIR / 'dataset'
            )
        )
        INPUT_DIR.mkdir(parents=True, exist_ok=True)
    except TypeError:
        raise EnvironmentError(f'Invalid `INPUT_DIR` environment value.')
    try:
        OUTPUT_DIR: pathlib.Path = pathlib.Path(
            os.environ.get(
                'OUTPUT_DIR',
                INPUT_DIR / 'images'
            )
        )
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    except TypeError:
        raise EnvironmentError(f'Invalid `OUTPUT_DIR` environment value.')

    TESSDATA_PREFIX: pathlib.Path = BASE_DIR / 'tessdata'


settings = Settings()

# Configure Logging

logging.basicConfig(
    # format='%(levelname)s %(asctime)s %(name)s %(message)s',
    format='%(asctime)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S',
    level=logging.INFO
)

# Set Default Environment Variables

os.environ['TESSDATA_PREFIX'] = str(settings.TESSDATA_PREFIX)
