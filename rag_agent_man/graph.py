from langchain_core.documents import Document
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict


class State(TypedDict):
    question: str
    context: List[Document]
    answer: str


def retrieve(state: State, config):
    rag = config["configurable"]["rag"]
    docs = rag.retrieve(state["question"])
    return {"context": docs}


def generate(state: State, config):
    rag = config["configurable"]["rag"]
    response = rag.generate(state["question"], state["context"])
    return {"answer": response.content}


def get_graph():
    graph_builder = StateGraph(State).add_sequence([retrieve, generate])
    graph_builder.add_edge(START, "retrieve")
    return graph_builder.compile()
