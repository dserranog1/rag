from rag_agent_man.vector_store import get_vector_store
from rag_agent_man.prompt import get_promt
from langchain_ollama import ChatOllama


def retrieve_docs_by_similarity(query):
    vector_store = get_vector_store()
    return vector_store.similarity_search(query, 2)


if __name__ == "__main__":
    while True:
        query = input("Hello! How can I help you today?:\n")
        print("************")
        retrieved_docs = retrieve_docs_by_similarity(query)
        docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)
        prompt = get_promt()
        final_prompt = prompt.invoke({"question": query, "context": docs_content})
        llm = ChatOllama(model="llama3.1:8b")
        answer = llm.invoke(final_prompt)
        print(answer.content)
