from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from rag_agent_man.loader import load_documents
from rag_agent_man.splitter import split_documents
import chromadb


def embed_documents(docs):
    model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    chroma_client = chromadb.HttpClient(host="localhost", port=8000)
    vector_store = Chroma(embedding_function=model, client=chroma_client)
    return vector_store.add_documents(documents=docs)


if __name__ == "__main__":
    docs = load_documents()
    all_splits = split_documents(docs)
    ids = embed_documents(all_splits)
    print(ids)
