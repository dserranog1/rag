from rag_agent_man.vector_store import get_vector_store

if __name__ == "__main__":
    vector_store = get_vector_store()
    query = input("Enter a query to search by similarity:\n")
    results = vector_store.similarity_search(query, 2)
    print("Result 1: ", results[0])
    print("Result 2: ", results[1])
