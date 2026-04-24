from typing import TypedDict, List
from langchain_core.documents import Document

class AgentState(TypedDict):
    question: str
    retrieved_docs: List[Document]
    answer: str
    
# What this does?
"""
This defines the memory/state object that moves through the graph
question -> what user asked
retrieved_docs -> document chunks found by search
answer -> final LLM response

LangGraph passes this state from one step to the next.
"""