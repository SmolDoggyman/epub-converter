# PDF/DOCX to EPUB Converter

Convert PDF and Word documents into reflowable EPUB e-books that read well on Kindle and other e-readers.

Most PDFs have a fixed page layout, so on a small screen the text shrinks instead of rewrapping. This converter recovers the document's structure (headings and paragraphs) and rebuilds it as an EPUB, so the text adjusts to your screen and chosen font size.

## Try it online

**Link coming soon.**

1. Open the app in your browser. No installation is needed.
2. Upload a PDF or DOCX file.
3. Click **Download EPUB**.
4. To read it on a Kindle, upload the EPUB at [amazon.com/sendtokindle](https://www.amazon.com/sendtokindle).

## Features

- Converts **PDF** and **DOCX** files to **EPUB**
- Detects headings in PDFs from their font size
- Uses Word's heading styles in DOCX files
- Splits the book into chapters at each main heading, with a table of contents
- Removes page numbers, running headers and footers from PDFs

## Run it on your own computer

You need Python 3.12 or later.

```bash
git clone https://github.com/SmolDoggyman/epub-converter.git
cd epub-converter
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Start the web app:

```bash
streamlit run app.py
```

Or convert a file from the command line:

```bash
python -m kindleconv.cli mybook.pdf
```

The EPUB is saved next to the original file.

## Known limitations

This is an early version. PDFs don't store their structure, so the converter infers it, and some documents won't convert perfectly.

- **Scanned PDFs** aren't supported, because they contain images of text rather than text.
- **Words split across lines** with a hyphen may appear as two parts.
- **Paragraphs that continue onto the next page** may be split in two.
- **Images** in PDFs are not included.
- **Multi-column layouts** may come out in the wrong reading order.
- **Lines containing only a number** may be removed, because they look like page numbers.
- **Text very close to the top or bottom of a page** may be removed, because it looks like a header or footer.
- **DOCX files** only get chapters if they use Word's built-in heading styles.

## Privacy

When you use the online app, your file is sent to the server for conversion. It's processed in a temporary folder that's deleted afterwards, and it isn't stored by this app. Please avoid uploading sensitive documents.

## Project structure

```
app.py                  Web app (Streamlit)
kindleconv/
  cli.py                Command-line tool
  docx_reader.py        DOCX → HTML
  pdf_reader.py         PDF → HTML
  epub_writer.py        HTML → EPUB
```

## Built with

- [PyMuPDF](https://pymupdf.readthedocs.io/) for reading PDFs
- [Mammoth](https://github.com/mwilliamson/python-mammoth) for reading DOCX files
- [EbookLib](https://github.com/aerkalov/ebooklib) for writing EPUBs
- [Streamlit](https://streamlit.io/) for the web app

## Licence

Copyright © 2026 Hassaan A. Shah

This project is licensed under the [GNU Affero General Public License v3.0](LICENSE).

Kindle is a trademark of Amazon.com, Inc. This project is not affiliated with Amazon.