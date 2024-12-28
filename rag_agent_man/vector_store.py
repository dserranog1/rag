from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import chromadb


def get_vector_store():
    model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    chroma_client = chromadb.HttpClient(host="localhost", port=8000)
    return Chroma(embedding_function=model, client=chroma_client)
