# About - Geolang OCR Toolkit



# Prerequisites

------
`Python`  
`Tesseract`


# Install dependencies for Linux

-----

Requires `libtesseract` (>=3.04) and `libleptonica` (>=1.71).

On Debian/Ubuntu:

```bash
$ sudo apt-get install tesseract-ocr libtesseract-dev libleptonica-dev pkg-config
```

On RedHat/Fedora:

```bash
$ sudo dnf install tesseract tesseract-devel leptonica-devel leptonica
```

# Install dependencies for Windows

-----

https://github.com/danbloomberg/leptonica/releases
https://tesseract-ocr.github.io/tessdoc/Downloads.html
https://digi.bib.uni-mannheim.de/tesseract/

# Setup Project 

------

```bash
$ git clone <project_repo>
```

```bash
$ cd <project_directory>/
```

## Install Source dependencies from `requirements`

----

```bash
$ pip install -r requirements/dev.txt
```

### Package Build and Install

-----

```bash
$ python -m build
```

For Windows

```bash
$ pip install dist/geolangocr-<version>-py3-none-any.whl
```

For Linux

```bash
$ pip install dist/geolangocr-<version>-tar.gz
```

# Using

------
1. Add `dataset` folder current directory
2. Add Scanned `PDF` files into `dataset` directory
3. Add `keywords.txt` file into `dataset` directory
4. Add Search Keywords to `keywords.txt` file (each keywords must be new line without numbering)


### Commands

----

List of available commands

 ```bash
 $ python -m geolangocr
 ```

Add new keywords by `add-keywords` command 

 ```bash
 $ python -m geolangocr add-keywords --k my-search-keyword1 my-search-keyword2 etc.
 ```

Search Keywords  

 ```bash
 $ python -m geolangocr matcher 
 ```

Pdf file convert to images  

 ```bash
 $ python -m geolangocr pdf2img 
 ```
