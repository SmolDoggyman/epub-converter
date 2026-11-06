import pymupdf
from collections import Counter
import html

def block_text(block):
    text = ""
    for line in block["lines"]:
        line_text = ""
        for span in line["spans"]:
            line_text += span["text"]
        text += line_text.strip() + " "
    return text.strip()

def block_size(block):
    biggest = 0
    for line in block["lines"]:
        for span in line["spans"]:
            if span["size"] > biggest:
                biggest = span["size"]
    return biggest

def pdf_to_html(path):
    doc = pymupdf.open(path)
    sizes = Counter()
    parts = []
    for page in doc:
        for block in page.get_text("dict")["blocks"]:
            if block["type"] != 0:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    key =round(span["size"])
                    amount = len(span["text"])
                    sizes[key] += amount
    body = sizes.most_common(1)[0][0]

    for page in doc: 
        for block in page.get_text("dict")["blocks"]:
            if block["type"] != 0:
                continue
            text = block_text(block)
            if not text or text.isdigit():
                continue
            y = block["bbox"][1]
            height = page.rect.height
            if y < height * 0.06 or y > height * 0.92:
                continue
            html_text = html.escape(text)
            size = block_size(block)
            if size >=  body * 1.6:
                parts.append(f"<h1>{html_text}</h1>")
            elif size >= body * 1.2:
                parts.append(f"<h2>{html_text}</h2>")
            else: 
                parts.append(f"<p>{html_text}</p>")
    return "\n".join(parts)