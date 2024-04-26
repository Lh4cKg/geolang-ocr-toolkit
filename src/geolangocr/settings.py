import os
import pathlib


BASE_DIR = pathlib.Path(__file__).resolve().parent


TESSDATA_PREFIX = BASE_DIR / 'tessdata'
os.environ['TESSDATA_PREFIX'] = str(TESSDATA_PREFIX)
