# RAG System for Universidad Nacional de Colombia, Manizales

## Overview
This repository contains an interactive Retrieval-Augmented Generation (RAG) system designed to enhance access to information from the Universidad Nacional de Colombia, Manizales campus. Built as a degree project, it leverages an open-source large language model (LLM) integrated with RAG to answer contextual queries (e.g., "What is the profile of an applicant to the Architecture program?") based on institutional website data. The system uses Docker for reproducibility, featuring a modular architecture with Chroma (vector database), Ollama (LLM), FastAPI (backend), and Streamlit (frontend). It aims to democratize information access for students and visitors in a local, lightweight setup.

## Features
- **Data Ingestion**: Scrapes and processes data from the university website using Scrapy.
- **RAG Integration**: Combines retrieval with Hermes 3 LLM for accurate responses.
- **Interactive Interface**: User-friendly frontend accessible via `localhost:8501`.
- **Reproducibility**: Fully containerized with Docker for consistent deployment.

## Requirements
- Docker (20.10+)
- Docker Compose (2.0+)
- Python 3.11
- Poetry (~1.8.2)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/dserranog1/rag
   cd rag
   ```
2. Install dependencies:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   poetry install
   ```
3. Collect data:
   ```bash
   scrapy crawl degrees
   scrapy crawl misc
   ```
4. Start the containers:
   ```bash
   docker compose up --build
   ```
5. Populate Chroma:
   ```bash
    docker exec -it rag_agent bash
    python -m rag_agent_man.db -d
   ```
6. Access the system at `http://localhost:8501`

## Usage
Enter questions in the Streamlit interface to retrieve answers. Initial setup (e.g., Ollama model download ~4GB) may take time, but subsequent runs are faster.

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request. Report issues via the Issues tab.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments

Special thanks to my thesis advisor and the Universidad Nacional de Colombia for support and resources.

   
   
