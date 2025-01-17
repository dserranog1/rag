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

# Wait for Ollama process to finish.
wait $pid