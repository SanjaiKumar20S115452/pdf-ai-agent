from langchain_openai import ChatOpenAI
from langchain_core.documents import Document

from app.core.config import LLM_MODEL
from app.core.logging import setup_logger

logger = setup_logger(__name__)

llm = ChatOpenAI(
    model=LLM_MODEL,
    temperature=0.2
)

def generate_answer(question: str, documents: list[Document]) -> str:
    context = "\n\n".join(
        [
            f"Source: {doc.metadata.get('source', 'unknown')}\n{doc.page_content}"
            for doc in documents
        ]
    )

    prompt = f"""
You are a private enterprise knowledge assistant.

Answer the question using ONLY the provided context.

Question:
{question}

Context:
{context}
"""

    response = llm.invoke(
        prompt,
        config={
            "run_name": "LLM Answer Generation",
            "tags": ["llm", "generation"]
        }
    )

    logger.info("Generated LLM answer")
    return response.content