from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import chromadb


def get_embedder():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def get_vector_store():
    embedder_model = get_embedder()
    chroma_client = chromadb.HttpClient(host="localhost", port=8000)
    return Chroma(embedding_function=embedder_model, client=chroma_client)
