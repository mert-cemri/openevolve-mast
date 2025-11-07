#!/bin/bash

# ChatDev with Qwen2.5-Coder-32B-Instruct Integration Script
# This script demonstrates how to run ChatDev with your locally hosted Qwen model

echo "=========================================="
echo "ChatDev + Qwen2.5-Coder-32B Integration"
echo "=========================================="

# Configuration
QWEN_SERVER_URL="http://localhost:12355/v1"
MODEL_NAME="Qwen2.5-Coder-32B-Instruct"

# Check if server is running
echo "Checking if Qwen model server is running..."
if curl -s "$QWEN_SERVER_URL/models" > /dev/null; then
    echo "✅ Qwen model server is accessible at $QWEN_SERVER_URL"
else
    echo "❌ Cannot connect to Qwen model server at $QWEN_SERVER_URL"
    echo "Please ensure your Qwen model is running with vLLM:"
    echo "  python -m vllm.entrypoints.openai.api_server \\"
    echo "    --model Qwen/Qwen2.5-Coder-32B-Instruct \\"
    echo "    --port 12355 \\"
    echo "    --host 0.0.0.0"
    exit 1
fi

# Set environment variables
export BASE_URL="$QWEN_SERVER_URL"
export OPENAI_API_KEY="fake-key"  # vLLM doesn't require a real API key

echo "Environment configured:"
echo "  BASE_URL=$BASE_URL"
echo "  OPENAI_API_KEY=$OPENAI_API_KEY"

# Define the task
if [ -z "$1" ]; then
    TASK="Create a simple Python password generator CLI tool. The tool should generate secure passwords with customizable length (8-32 characters) and allow users to include/exclude uppercase letters, lowercase letters, numbers, and special characters. The tool should be interactive and ask users for their preferences."
    PROJECT_NAME="PasswordGenerator_Qwen"
else
    TASK="$1"
    PROJECT_NAME="${2:-QwenProject}"
fi

echo ""
echo "Task: $TASK"
echo "Project Name: $PROJECT_NAME"
echo ""

# Run ChatDev with Qwen model
echo "Starting ChatDev with Qwen model..."
echo "This may take several minutes..."

cd ChatDev

python run.py \
    --task "$TASK" \
    --name "$PROJECT_NAME" \
    --model "$MODEL_NAME" \
    --config "Prompted" \
    --org "QwenTestOrg"

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 ChatDev completed successfully!"
    echo "Generated project can be found in: WareHouse/${PROJECT_NAME}_QwenTestOrg_*"
    echo ""
    echo "To run the generated software:"
    echo "  cd WareHouse/${PROJECT_NAME}_QwenTestOrg_*"
    echo "  python main.py"
else
    echo ""
    echo "❌ ChatDev execution failed"
    exit 1
fi 