from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from app.core.config import VECTOR_STORE_DIR, LOCAL_EMBEDDING_MODEL, TOP_K_RESULTS
from app.core.logging import setup_logger
from app.services.ingestion_service import load_documents, chunk_documents

logger = setup_logger(__name__)


def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name=LOCAL_EMBEDDING_MODEL
    )


def build_vector_store() -> FAISS:
    documents = load_documents()
    chunks = chunk_documents(documents)

    embeddings = get_embeddings()

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    vector_store.save_local(str(VECTOR_STORE_DIR))

    logger.info("Vector store built and saved")
    return vector_store


def load_vector_store() -> FAISS:
    index_path = VECTOR_STORE_DIR / "index.faiss"

    embeddings = get_embeddings()

    if not index_path.exists():
        logger.info("Vector store not found. Building new vector store.")
        return build_vector_store()

    logger.info("Loading existing vector store")

    return FAISS.load_local(
        str(VECTOR_STORE_DIR),
        embeddings,
        allow_dangerous_deserialization=True
    )

def retrieve_relevant_chunks(question: str):
    vector_store = load_vector_store()

    docs = vector_store.similarity_search(
        question,
        k=TOP_K_RESULTS
    )

    logger.info(f"Retrieved {len(docs)} relevant chunks")
    return docs