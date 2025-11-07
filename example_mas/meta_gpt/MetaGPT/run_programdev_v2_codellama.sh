#!/bin/bash

# MetaGPT ProgramDev V2 Evaluation with CodeLlama-13b-Instruct
# This script runs the programdev_v2 dataset evaluation using the CodeLlama model

# Change to MetaGPT directory if not already there
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=============================================="
echo "MetaGPT ProgramDev V2 Evaluation with CodeLlama"
echo "=============================================="

# Configuration
export BASE_URL="http://localhost:12355/v1"
export OPENAI_API_KEY="fake-key"
export CODELLAMA_MAX_TOKENS="4096"  # Conservative token limit for 13B model
export PYTHONPATH="$SCRIPT_DIR:$PYTHONPATH"  # Ensure MetaGPT can be found
export TOKENIZERS_PARALLELISM=false  # Disable tokenizer warnings
MODEL_TYPE="codellama"
DATASET_PATH="/data/user_data/mert/example_mas/programdev_v2"

# Check if CodeLlama server is running
echo "Checking CodeLlama model server..."
if curl -s "$BASE_URL/models" >/dev/null 2>&1; then
    echo "✅ CodeLlama model server is accessible"
    # Test a simple completion to verify it's working
    echo "Testing server responsiveness..."
    TEST_RESPONSE=$(curl -s -X POST "$BASE_URL/completions" \
        -H "Content-Type: application/json" \
        -d '{"model": "CodeLlama-13b-Instruct", "prompt": "Hello", "max_tokens": 5}' 2>/dev/null)
    if [ $? -eq 0 ] && echo "$TEST_RESPONSE" | grep -q "choices"; then
        echo "✅ CodeLlama server is responding correctly"
    else
        echo "⚠️  Server accessible but may be slow - proceeding anyway"
    fi
else
    echo "❌ CodeLlama model server is not accessible at $BASE_URL"
    echo "Please make sure your CodeLlama server is running with:"
    echo "  bash serve_codellama.sh"
    exit 1
fi

# Check if dataset exists
if [ ! -d "$DATASET_PATH" ]; then
    echo "❌ Dataset not found at: $DATASET_PATH"
    echo "Please ensure the programdev_v2 dataset is available"
    exit 1
fi

echo "📂 Dataset path: $DATASET_PATH"
echo "🔧 Model type: $MODEL_TYPE"
echo "🌐 Base URL: $BASE_URL"
echo "🎯 Max tokens: $CODELLAMA_MAX_TOKENS"
echo ""

# Create output directory if it doesn't exist
mkdir -p logs/programdev_v2_codellama

echo "Starting evaluation..."
echo ""

# Run evaluation on subset of examples (modify loop as needed)
for ((i=0; i<100; i++)); do
    DESCRIPTION_FILE="$DATASET_PATH/descriptions_$i.txt"
    
    if [ ! -f "$DESCRIPTION_FILE" ]; then
        echo "⚠️  Skipping $i: Description file not found: $DESCRIPTION_FILE"
        continue
    fi
    
    echo "Processing example $i..."
    LOG_FILE="logs/programdev_v2_codellama/metagpt_codellama_$i.txt"
    
    # Run MetaGPT with CodeLlama model
    python3 examples/build_customized_multi_agents.py \
        --idea "$(cat "$DESCRIPTION_FILE")" \
        --log_file="$LOG_FILE" \
        --model_type="$MODEL_TYPE" \
        --investment=3.0 \
        --n_round=5
    
    if [ $? -eq 0 ]; then
        echo "✅ Example $i completed successfully"
    else
        echo "❌ Example $i failed"
    fi
    
    echo "---"
done

echo ""
echo "🎉 MetaGPT ProgramDev V2 evaluation with CodeLlama model completed!"
echo "Results saved in: logs/programdev_v2_codellama/"
echo "Generated projects can be found in the workspace directories" 