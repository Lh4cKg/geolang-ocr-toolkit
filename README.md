# About - OCR Toolkit
Search pre-defined keywords into the scanned PDF files using Levenshtein algorithm.  


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

1. [Tesseract Docs](https://tesseract-ocr.github.io/)
2. [Tesseract](https://digi.bib.uni-mannheim.de/tesseract/)
3. [Leptonica](https://github.com/danbloomberg/leptonica/releases)

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
$ pip install dist/ocrmatcher-<version>-py3-none-any.whl
```

For Linux

```bash
$ pip install dist/ocrmatcher-<version>-tar.gz
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
 $ ocrmatcher --help
 ```
Or

 ```bash
 $ python -m ocrmatcher --help
 ```

Add new keywords by `add-keywords` command 

 ```bash
 $ ocrmatcher add-keywords --k my-search-keyword1 my-search-keyword2 etc.
 ```

Search Keywords  

 ```bash
 $ ocrmatcher search 
 ```

Run with specific language

Search Keywords  

 ```bash
 $ ocrmatcher search --lang Occupant-Pigs
 ```

Run with specific `threshold` for two strings similarity, default is: `95`

Search Keywords  

 ```bash
 $ ocrmatcher search --threshold 75
 ```

Pdf file convert to images  

 ```bash
 $ ocrmatcher pdf2img 
 ```
