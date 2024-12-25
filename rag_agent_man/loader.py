from langchain_community.document_loaders import (
    UnstructuredMarkdownLoader,
    DirectoryLoader,
)


def load_documents():
    markdown_path = "documents"
    loader = DirectoryLoader(
        markdown_path, glob="**/*.md", loader_cls=UnstructuredMarkdownLoader
    )
    data = loader.load()
    return data


if __name__ == "__main__":
    docs = load_documents()
    for doc in docs:
        print(doc.page_content)
