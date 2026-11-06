import pathlib
import tempfile
from kindleconv.cli import READERS
from kindleconv.epub_writer import build_epub
import streamlit as st

st.title("PDF/DOCX to EPUB Converter")
st.write("Upload a PDF or DOCX file to convert it to EPUB format.")
st.write("Your file is sent to the server for conversion and isn't kept afterwards. Avoid uploading sensitive documents.")
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx"])

if uploaded_file is None:
    st.stop()
else:
    name = pathlib.Path(uploaded_file.name)
    with tempfile.TemporaryDirectory() as folder:
        src = pathlib.Path(folder) / f"input{name.suffix.lower()}"
        out = src.with_suffix(".epub")
        src.write_bytes(uploaded_file.getvalue())
        reader = READERS.get(src.suffix.lower())
        body = reader(str(src))
        build_epub(body, name.stem, str(out))
        epub_bytes = out.read_bytes()
    st.download_button(
        "Download EPUB",
        data=epub_bytes,
        file_name=f"{name.stem}.epub",
        mime="application/epub+zip"
    )