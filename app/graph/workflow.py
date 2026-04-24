from langgraph.graph import StateGraph, END

from app.graph.state import AgentState
from app.graph.nodes import guardrail_node, retrieval_node, answer_node

def build_workflow():
    workflow = StateGraph(AgentState)

    workflow.add_node("guardrails", guardrail_node)
    workflow.add_node("retrieval", retrieval_node)
    workflow.add_node("answer", answer_node)

    workflow.set_entry_point("guardrails")

    workflow.add_edge("guardrails", "retrieval")
    workflow.add_edge("retrieval", "answer")
    workflow.add_edge("answer", END)

    return workflow.compile()

agent_workflow = build_workflow()