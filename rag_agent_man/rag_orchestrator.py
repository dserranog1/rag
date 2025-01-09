import subprocess

from rag_agent_man.db import load_documents_to_db
from rag_agent_man.loader import load_documents
from rag_agent_man.splitter import split_documents


def scrape_data():
    """Run the Scrapy spider to scrape data."""
    print("Starting scraping process...")
    try:
        subprocess.run(["scrapy", "crawl", "degrees"], check=True)
        print("Scraping completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Scraping failed: {e}")
        raise


def load_data():
    """Load documents from the scraped files."""
    print("Loading documents...")
    docs = load_documents()
    print(f"Loaded {len(docs)} documents.")
    return docs


def split_data(docs):
    """Split the loaded documents into smaller chunks."""
    print("Splitting documents...")
    splits = split_documents(docs)
    print(f"Split into {len(splits)} chunks.")
    return splits


def reset_and_store(splits):
    """Reset the database collection and store the embeddings."""
    print("Resetting database and storing embeddings...")
    ids = load_documents_to_db(splits, delete=True)
    print(f"Stored {len(ids)} embeddings.")
    return ids


def run_pipeline():
    """Run the entire pipeline."""
    try:
        # Step 1: Scrape
        scrape_data()

        # Step 2: Load
        docs = load_data()

        # Step 3: Split
        splits = split_data(docs)

        # Step 4: Reset and Store
        reset_and_store(splits)

        print("Pipeline executed successfully.")
        return True
    except Exception as e:
        print(f"Pipeline execution failed: {e}")
        return False


if __name__ == "__main__":
    run_pipeline()
