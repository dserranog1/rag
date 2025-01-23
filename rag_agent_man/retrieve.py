from rag_agent_man.rag import RAG

if __name__ == "__main__":
    # question = input("Hello! How can I help you? \n")
    question = "cual es el perfil de un aspirante a administracion de sistemas informaticos?"
    rag = RAG()
    docs = rag.retrieve(question, as_list=True)
    for i, doc in enumerate(docs):
        print("*****************************************************")
        print("DOCUMENT NUMBER: ", i)
        print(doc)
        print("*****************************************************")
        print("\n\n")