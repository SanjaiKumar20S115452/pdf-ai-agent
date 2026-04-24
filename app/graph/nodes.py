from app.graph.state import AgentState
from app.guardrails.input_guardrails import validate_question
# from app.services.retrieval_service import retrieve_relevant_chunks
from app.tools.document_tools import search_documents
from app.services.llm_service import generate_answer
from app.core.logging import setup_logger
from app.tools.document_tools import search_documents
from langchain_core.documents import Document

logger = setup_logger(__name__)


def guardrail_node(state: AgentState) -> AgentState:
    question = validate_question(state["question"])

    logger.info("Guardrail check passed")

    return {
        **state,
        "question": question
    }

def retrieval_node(state: AgentState) -> AgentState:

    results = search_documents(state["question"])

    docs = [
        Document(
            page_content=item["content"],
            metadata={"source": item["source"]}
        )
        for item in results
    ]

    logger.info(f"Retrieved {len(docs)} chunks")

    return {
        **state,
        "retrieved_docs": docs
    }


def answer_node(state: AgentState) -> AgentState:
    answer = generate_answer(
        question=state["question"],
        documents=state["retrieved_docs"]
    )

    logger.info("Answer generated")

    return {
        **state,
        "answer": answer
    }