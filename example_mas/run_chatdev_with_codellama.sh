#!/bin/bash

# Convenience script for running ChatDev with CodeLlama model
# Usage: ./run_chatdev_with_codellama.sh "Your task description" "ProjectName"

# Check if task and name are provided
if [ $# -lt 2 ]; then
    echo "Usage: $0 \"Task description\" \"Project name\" [config]"
    echo "Example: $0 \"Create a calculator app\" \"Calculator\" \"Default\""
    exit 1
fi

TASK="$1"
PROJECT_NAME="$2"
CONFIG="${3:-Default}"  # Default config if not provided

echo "=========================================="
echo "Running ChatDev with CodeLlama Model"
echo "=========================================="
echo "Task: $TASK"
echo "Project: $PROJECT_NAME"
echo "Config: $CONFIG"
echo ""

# Set environment variables for CodeLlama
export BASE_URL="http://localhost:12355/v1"
export OPENAI_API_KEY="fake-key"
export CODELLAMA_MAX_TOKENS="30208"

# Check if CodeLlama server is running
echo "Checking CodeLlama server..."
if curl -s "$BASE_URL/models" > /dev/null; then
    echo "✅ CodeLlama server is accessible"
else
    echo "❌ Cannot connect to CodeLlama server at $BASE_URL"
    echo "Please start your CodeLlama server using serve_codellama.sh"
    exit 1
fi

# Change to ChatDev directory
cd ChatDev

# Run ChatDev with CodeLlama
echo "Starting ChatDev with CodeLlama..."
python run.py \
    --task "$TASK" \
    --name "$PROJECT_NAME" \
    --model "CodeLlama-13b-Instruct" \
    --config "$CONFIG" \
    --org "CodeLlamaOrg"

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 ChatDev completed successfully!"
    echo "Check WareHouse/ directory for generated project"
else
    echo ""
    echo "❌ ChatDev encountered an error"
    exit 1
fi 