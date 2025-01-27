from pathlib import Path

import frontmatter
from langchain.schema import Document


def load_documents():
    markdown_path = Path("documents")
    docs = []
    
    for md_file in markdown_path.glob("**/*.md"):
        # Parse file with frontmatter
        post = frontmatter.load(md_file)
        
        # Create document with combined metadata
        docs.append(Document(
            page_content=post.content,
            metadata={
                **post.metadata
            }
        ))
    
    return docs

if __name__ == "__main__":
    docs = load_documents()
    for doc in docs:
        print("Content:", doc.page_content[:50] + "...")
        print("Metadata:", doc.metadata)
        print("\n---\n")