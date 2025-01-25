import chromadb
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag_agent_man.prompt import TEMPLATE


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
        return HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

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

    def retrieve(self, query, top_k=3, as_list=False):
        retrieved_docs = self.vector_store.similarity_search(query, top_k)
        if as_list:
            return [doc.page_content for doc in retrieved_docs]
        return "\n\n".join(doc.page_content for doc in retrieved_docs)

    def generate(self, query, relevant_docs):
        messages = self.prompt.invoke({"question": query, "context": relevant_docs})
        response = self.llm.invoke(messages)
        return response
