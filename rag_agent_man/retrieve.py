from rag_agent_man.rag import RAG

if __name__ == "__main__":
    # question = input("Hello! How can I help you? \n")
    question = "cuantas carreras existen en la universidad?"
    rag = RAG()
    docs = rag.retrieve(question, as_list=True, top_k=5)
    for i, doc in enumerate(docs):
        print("*****************************************************")
        print("DOCUMENT NUMBER: ", i)
        print(doc)
        print("*****************************************************")
        print("\n\n")