from langchain_core.documents import Document
from langfuse.callback import CallbackHandler
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict

from rag_agent_man.rag import RAG


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


if __name__ == "__main__":
    langfuse_handler = CallbackHandler()
    question = input("Hello! How can I help you? \n")
    rag = RAG()
    graph_builder = StateGraph(State).add_sequence([retrieve, generate])
    graph_builder.add_edge(START, "retrieve")
    graph = graph_builder.compile()
    for state in graph.stream(
        {"question": question},
        config={"callbacks": [langfuse_handler], "configurable": {"rag": rag}},
    ):
        print(state)
