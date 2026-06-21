"""
Step 1 logic: turn an uploaded CV file (PDF or DOCX) into plain text
that the rest of the app — and eventually Claude — can read.

This file does NOT touch Streamlit or the Claude API. It only knows
how to read files. That makes it easy to test on its own.
"""

from pypdf import PdfReader
from docx import Document


def extract_text_from_pdf(uploaded_file) -> str:
    """Read every page of a PDF and join the text together."""
    reader = PdfReader(uploaded_file)
    text_parts = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:  # some pages (e.g. scanned images) may return nothing
            text_parts.append(page_text)
    return "\n".join(text_parts).strip()


def extract_text_from_docx(uploaded_file) -> str:
    """Read every paragraph of a Word document and join the text together."""
    document = Document(uploaded_file)
    paragraphs = [p.text for p in document.paragraphs]
    return "\n".join(paragraphs).strip()


def extract_cv_text(uploaded_file) -> str:
    """
    Look at the uploaded file's name to decide whether it's a PDF or DOCX,
    then call the right extraction function.

    uploaded_file comes from Streamlit's file_uploader widget — it behaves
    like a normal file, and also has a .name attribute (e.g. "cv.pdf").
    """
    filename = uploaded_file.name.lower()

    if filename.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)
    elif filename.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)
    else:
        raise ValueError("Unsupported file type. Please upload a PDF or DOCX file.")