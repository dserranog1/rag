from rag_agent_man.loader import load_documents
from rag_agent_man.rag import RAG


def split_documents(docs):
    splitter = RAG.get_splitter()
    return splitter.split_documents(docs)


if __name__ == "__main__":
    docs = load_documents()
    all_splits = split_documents(docs)
    for i, split in enumerate(all_splits):
        print("split number", i)
        print(split)
        print("*****")
        print("\n")
