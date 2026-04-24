from pathlib import Path
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw"
VECTOR_PATH = BASE_DIR / "vector_store"

def load_docs():
    docs = []
    for file in DATA_PATH.glob("*.txt"):
        text = file.read_text()
        docs.append(Document(page_content=text, metadata={"source": file.name}))
    return docs

def build_vector_store():
    docs = load_docs()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    store = FAISS.from_documents(chunks, embeddings)

    VECTOR_PATH.mkdir(exist_ok=True)
    store.save_local(str(VECTOR_PATH))

    return store

def load_vector_store():
    embeddings = OpenAIEmbeddings()

    if not (VECTOR_PATH / "index.faiss").exists():
        return build_vector_store()

    return FAISS.load_local(str(VECTOR_PATH), embeddings, allow_dangerous_deserialization=True)


def retrieve(query):
    store = load_vector_store()
    return store.similarity_search(query, k=3)

# What this file does

"""
1. Read documents
2. Split into chunks
3. Convert chunks -> embeddings (numbers)
4. Store in FAISS (vector DB)
5. When user asks question:
-> find most relevant chunks
"""