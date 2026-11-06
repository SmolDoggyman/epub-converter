import mammoth

def docx_to_html(path):
    """
    Convert a DOCX file to HTML using the Mammoth library.

    Args:
        path (str): The file path to the DOCX file.

    Returns:
        str: The HTML content extracted from the DOCX file.
    """
    with open(path, "rb") as f:
        result = mammoth.convert_to_html(f)
    for msg in result.messages:
        print("warning:", msg)
    return result.value