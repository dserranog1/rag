import argparse

from rag_agent_man.loader import load_documents
from rag_agent_man.rag import RAG
from rag_agent_man.splitter import split_documents


def load_documents_to_db(docs, delete=False):
    vector_store = RAG.get_vector_store()
    if delete:
        vector_store.reset_collection()
    return vector_store.add_documents(documents=docs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load documents into the database.")
    parser.add_argument(
        "-d",
        "--delete",
        action="store_true",
        help="Delete the collection before loading documents.",
    )

    args = parser.parse_args()

    # Use the delete flag
    docs = load_documents()
    all_splits = split_documents(docs)
    ids = load_documents_to_db(all_splits, delete=args.delete)
    print(ids)
