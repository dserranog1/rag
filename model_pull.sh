#!/bin/bash

# Start Ollama in the background.
/bin/ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

echo "🔴 Pulling hermes3:8b"
ollama pull hermes3:8b
echo "🟢 Done!"

echo "🔴 Pulling jina/jina-embeddings-v2-base-es"
ollama pull jina/jina-embeddings-v2-base-es
echo "🟢 Done!"

# Wait for Ollama process to finish.
wait $pid