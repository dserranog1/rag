from langchain_text_splitters import RecursiveCharacterTextSplitter
from rag_agent_man.loader import load_documents


def get_splitter():
    return RecursiveCharacterTextSplitter(
        chunk_size=650,
        chunk_overlap=100,
    )


def split_documents(docs):
    splitter = get_splitter()
    return splitter.split_documents(docs)


if __name__ == "__main__":
    docs = load_documents()
    all_splits = split_documents(docs)
    for i, split in enumerate(all_splits):
        print("split number", i)
        print(split)
        print("*****")
        print("\n")
