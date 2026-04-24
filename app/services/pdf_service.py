from pathlib import Path
from pypdf import PdfReader

from app.core.config import RAW_DATA_DIR
from app.core.logging import setup_logger

logger = setup_logger(__name__)


def clear_raw_data_folder() -> None:
    """
    Remove old uploaded PDFs and extracted text files.
    """
    for file in RAW_DATA_DIR.glob("*"):
        if file.is_file():
            file.unlink()

    logger.info("Cleared old files from raw data folder")


def save_uploaded_pdf(file_bytes: bytes, filename: str) -> Path:
    """
    Clear old files, then save uploaded PDF into data/raw folder.
    """
    clear_raw_data_folder()

    pdf_path = RAW_DATA_DIR / filename

    with open(pdf_path, "wb") as f:
        f.write(file_bytes)

    logger.info(f"Uploaded PDF saved: {filename}")

    return pdf_path


def extract_text_from_pdf(pdf_path: Path) -> str:
    """
    Extract text from PDF file.
    """
    reader = PdfReader(str(pdf_path))

    text = ""
    for page in reader.pages:
        page_text = page.extract_text() or ""
        text += page_text + "\n"

    logger.info(f"Extracted text from PDF: {pdf_path.name}")

    return text


def convert_pdf_to_text_file(pdf_path: Path) -> Path:
    """
    Convert uploaded PDF into .txt file for the RAG pipeline.
    """
    text = extract_text_from_pdf(pdf_path)

    txt_filename = pdf_path.stem + ".txt"
    txt_path = RAW_DATA_DIR / txt_filename

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)

    logger.info(f"PDF converted to text: {txt_filename}")

    return txt_path

# What this does?
"""
This file handles PDF processing
PDF upload
1. save pdf
2. extract text
3. create .txt file
Your current RAG pipeline already works on .txt files. So we convert PDFs into text and reuse your existing system.
"""

