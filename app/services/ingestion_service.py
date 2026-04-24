from pathlib import Path
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.config import RAW_DATA_DIR
from app.core.logging import setup_logger

logger = setup_logger(__name__)

def load_documents() -> list[Document]:
    documents = []

    for file_path in RAW_DATA_DIR.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        documents.append(
            Document(
                page_content=text,
                metadata={"source": file_path.name}
            )
        )

    logger.info(f"Loaded {len(documents)} documents")
    return documents


def chunk_documents(documents: list[Document]) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=80
    )

    chunks = splitter.split_documents(documents)

    logger.info(f"Created {len(chunks)} chunks")
    return chunks

# What this file does?

"""
Read documents
-> Split them into smaller chunks
Why Chunking?
Small chunks = easier to retrieve relevant information
"""
