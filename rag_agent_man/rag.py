import chromadb
from chromadb.utils.embedding_functions.ollama_embedding_function import (
    OllamaEmbeddingFunction,
)
from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag_agent_man.prompt import TEMPLATE


class OllamaEmbeddings(Embeddings):
    """Wrapper to use OllamaEmbeddingFunction with LangChain's Chroma vector store."""

    def __init__(self, model_name="jina/jina-embeddings-v2-base-es", url="http://ollama:11434/api/embeddings"):
        self.embedding_function = OllamaEmbeddingFunction(url=url, model_name=model_name)

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Embed multiple documents and return a list of embeddings."""
        return self.embedding_function(texts)  # Already returns List[List[float]]

    def embed_query(self, text: str) -> list[float]:
        """Embed a single query and return a single embedding."""
        return self.embedding_function(text)[0]  # Extract the first (and only) embedding



class RAG:
    def __init__(self):
        self.llm = self.get_llm()
        self.embeddings = self.get_embeddings()
        self.vector_store = self.get_vector_store()
        self.prompt = PromptTemplate.from_template(TEMPLATE)

    @classmethod
    def get_llm(cls):
        return ChatOllama(model="hermes3:8b", base_url="ollama")

    @classmethod
    def get_embeddings(cls):
        return OllamaEmbeddings()

    @classmethod
    def get_vector_store(cls):
        chroma_client = chromadb.HttpClient(host="chromadb", port=8000)
        return Chroma(embedding_function=cls.get_embeddings(), client=chroma_client)

    @classmethod
    def get_splitter(cls):
        return RecursiveCharacterTextSplitter(
            chunk_size=1340,
            chunk_overlap=200,
        )

    def retrieve(self, query, top_k=3, as_list=True):
        retrieved_docs = self.vector_store.similarity_search(query, top_k)
        if as_list:
            return [
                {"content": doc.page_content, "source": doc.metadata}
                for doc in retrieved_docs
            ]
        return "\n\n".join(doc.page_content for doc in retrieved_docs)

    def generate(self, query, relevant_docs):
        messages = self.prompt.invoke({"question": query, "context": relevant_docs})
        response = self.llm.invoke(messages)
        return response
