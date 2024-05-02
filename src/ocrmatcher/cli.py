import os
import logging
import click

from .convert import PdfToImages
from .ocr import GeolangOcr
from .utils import add_keywords_txt


logger = logging.getLogger(__name__)


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('-t', '--threads', 'threads', default=os.cpu_count(), type=click.INT)
@click.option('-f', '--fmt', 'fmt', default='png', type=click.STRING)
def pdf2img(threads: int, fmt: str) -> None:
    """Convert pdf to images"""
    pdf = PdfToImages(
        thread_count=threads,
        fmt=fmt
    )
    pdf.run()


@cli.command(
    help="""
        1. Converting images to text using Tesseract model\n
        2. Search in the converted texts using search keywords 
    """,
    short_help="""
        1. Converting images to text using Tesseract model\n
        2. Search keywords in the converted texts 
    """
)
@click.option('-l', '--lang', 'lang', default='Georgian', type=click.STRING)
@click.option('-s', '--save', 'save', default=False, type=click.BOOL)
@click.option('--check_convert_pdf', default=True, type=click.BOOL)
@click.option('--save_matched_output', default=True, type=click.BOOL)
@click.option('--del_converted_images', default=False, type=click.BOOL)
@click.option('--del_converted_texts', default=False, type=click.BOOL)
def search(
        lang: str, save: bool,
        check_convert_pdf: bool,
        save_matched_output: bool,
        del_converted_images: bool,
        del_converted_texts: bool
) -> None:
    glang = GeolangOcr(
        lang=lang,
        save=save,
        check_convert_pdf=check_convert_pdf,
        save_matched_output=save_matched_output,
        del_converted_images=del_converted_images,
        del_converted_texts=del_converted_texts
    )
    glang.run()


@cli.command()
@click.option('-k', '--keywords', type=click.STRING, required=True)
def add_keywords(keywords: str) -> None:
    """Add Search Keywords"""
    add_keywords_txt(keywords)


commands = click.CommandCollection(
    sources=[cli],
    help="""Geolang OCR command line interface."""
)


if __name__ == '__main__':
    # def signal_handler(sig, frame):
    #     print('You pressed Ctrl+C!')
    #     sys.exit(0)
    #
    # signal.signal(signal.SIGINT, signal_handler)
    # print('Press Ctrl+C')
    # signal.pause()
    commands()
