import logging
import os
import click

from .convert import PdfToImages
from .matcher import Matcher
from .ocr import GeolangOcr


logger = logging.getLogger(__name__)


@click.group()
def cli():
    pass


@cli.command()
@click.option('-i', '--input', 'inp', type=click.Path(exists=True))
@click.option('-o', '--output', 'out', type=click.Path(exists=True))
@click.option('-t', '--threads', 'threads', default=os.cpu_count(), type=click.INT)
@click.option('-f', '--fmt', 'fmt', default='png', type=click.STRING)
def pdf2img(inp, out, threads, fmt):
    """Converting pdf to images"""
    pdf = PdfToImages(
        input_folder=inp,
        output_folder=out,
        thread_count=threads,
        fmt=fmt
    )
    pdf.run()


@cli.command()
@click.option('-l', '--lang', 'lang', default='Georgian', type=click.STRING)
@click.option('-s', '--save', 'save', default=False, type=click.BOOL)
@click.option('--check_convert_pdf', default=False, type=click.BOOL)
@click.option('--del_converted_images', default=False, type=click.BOOL)
@click.option('--del_converted_texts', default=False, type=click.BOOL)
def img2text(lang, save, check_convert_pdf,
             del_converted_images, del_converted_texts):
    """Converting image to text using Tesseract model"""
    glang = GeolangOcr(
        lang=lang,
        save=save,
        check_convert_pdf=check_convert_pdf,
        del_converted_images=del_converted_images,
        del_converted_texts=del_converted_texts
    )
    glang.run()


@cli.command()
def matcher():
    """Command on cli3"""
    logger.info("Matching sensitive keywords in these texts.")


commands = click.CommandCollection(sources=[cli])


if __name__ == '__main__':
    # import signal
    # import sys
    #
    # def signal_handler(sig, frame):
    #     print('You pressed Ctrl+C!')
    #     sys.exit(0)
    #
    # signal.signal(signal.SIGINT, signal_handler)
    # print('Press Ctrl+C')
    # signal.pause()
    commands()
