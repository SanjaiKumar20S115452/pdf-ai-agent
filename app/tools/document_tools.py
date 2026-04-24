from app.services.retrieval_service import retrieve_relevant_chunks
from app.services.ingestion_service import load_documents
from app.core.logging import setup_logger

logger = setup_logger(__name__)

def list_documents():
    """
    Tool: List available documents
    """
    docs = load_documents()
    sources = [doc.metadata.get("source", "unknown") for doc in docs]
    
    logger.info("Tool: list_documents called")
    return list(set(sources))


def search_documents(query: str):
    """
    Tool: Search relevant chunks from documents
    """
    results = retrieve_relevant_chunks(query)

    logger.info("Tool: search_documents called")

    return [
        {
            "source": doc.metadata.get("source", "unknown"),
            "content": doc.page_content
        }
        for doc in results
    ]
    
def read_document(file_name: str):
    """
    Tool: Read full document content
    """
    docs = load_documents()

    for doc in docs:
        if doc.metadata.get("source") == file_name:
            return doc.page_content

    return "Document not found"

# What this does?
"""
This creates tools.
Instead of calling services directly:
retrieval_services -> hidden
tools -> exposed
"""