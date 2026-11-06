from ebooklib import epub
import uuid
import re

def chapter_title(chunk, number):
    """
    Generate a chapter title based on the provided chunk and number.

    Args:
        chunk (str): The content of the chapter.
        number (int): The chapter number."""
    match = re.search(r"<h1[^>]*>(.*?)</h1>", chunk, re.S)
    if match:
        return re.sub(r"<.*?>", "", match.group(1))
    else:
        return f"Chapter {number}" 
    
def build_epub(body_html, title, out_path):
    """
    Build an EPUB file from the provided HTML content.

    Args:
        body_html (str): The HTML content to include in the EPUB.
        title (str): The title of the EPUB book.
        out_path (str): The output file path for the generated EPUB."""
    book = epub.EpubBook()
    book.set_identifier(str(uuid.uuid4()))
    book.set_title(title)
    book.set_language("en")

    # Create a chapter
    chunks = re.split(r"(?=<h1)", body_html)
    chapters = []
    for chunk in chunks:
        if not chunk.strip():
            continue
        number = len(chapters) + 1
        name = chapter_title(chunk, number)
        chapter = epub.EpubHtml(title=name, file_name=f"chap_{number}.xhtml", lang="en")            
        chapter.content = chunk
        book.add_item(chapter)
        chapters.append(chapter)

    # Define Table Of Contents
    book.toc = chapters
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = ["nav"] + chapters

    # Write to the file
    epub.write_epub(out_path, book)