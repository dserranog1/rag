from langchain_ollama import ChatOllama
from langchain_core.documents import Document
from typing_extensions import List, TypedDict
from langgraph.graph import START, StateGraph
from rag_agent_man.prompt import get_promt
from rag_agent_man.vector_store import get_vector_store


class State(TypedDict):
    question: str
    context: List[Document]
    answer: str


def get_question(state: State):
    question = input("Hello! How can I help you? \n")
    return {"question": question}


def retrieve(state: State):
    vector_store = get_vector_store()
    retrieved_docs = vector_store.similarity_search(state["question"], 2)
    docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)
    return {"context": docs_content}


def generate(state: State):
    llm = ChatOllama(model="llama3.1:8b")
    prompt = get_promt()
    messages = prompt.invoke(
        {"question": state["question"], "context": state["context"]}
    )
    response = llm.invoke(messages)
    return {"answer": response.content}

def print_answer(state: State):
    print(state["answer"])

if __name__ == "__main__":
    graph_builder = StateGraph(State).add_sequence([get_question, retrieve, generate, print_answer])
    graph_builder.add_edge(START, "get_question")
    graph = graph_builder.compile()
    graph.invoke({"question": None})
