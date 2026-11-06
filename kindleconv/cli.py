import argparse
import pathlib
from kindleconv.docx_reader import docx_to_html
from kindleconv.pdf_reader import pdf_to_html
from kindleconv.epub_writer import build_epub

READERS = {
    ".pdf": pdf_to_html,
    ".docx": docx_to_html,
}

def main():
    parser = argparse.ArgumentParser(description="Convert PDF or DOCX to EPUB")
    parser.add_argument("input_file")
    args = parser.parse_args()
    src = pathlib.Path(args.input_file)
    reader = READERS.get(src.suffix.lower())
    if reader is None:
        raise SystemExit(f"Unsupported file type: {src.suffix}")
    out = src.with_suffix(".epub")
    body_html = reader(str(src))
    build_epub(body_html, src.stem, str(out))
    print(f"EPUB file created: {out}")

if __name__ == "__main__":
    main()


