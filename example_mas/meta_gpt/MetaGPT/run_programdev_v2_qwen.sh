#!/bin/bash

# MetaGPT ProgramDev V2 Evaluation with Qwen2.5-Coder-32B-Instruct
# This script runs the programdev_v2 dataset evaluation using the Qwen model

# Change to MetaGPT directory if not already there
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "============================================="
echo "MetaGPT ProgramDev V2 Evaluation with Qwen"
echo "============================================="

# Configuration
export BASE_URL="http://localhost:12355/v1"
export OPENAI_API_KEY="fake-key"
export QWEN_MAX_TOKENS="4096"  # Conservative token limit for MetaGPT
export PYTHONPATH="$SCRIPT_DIR:$PYTHONPATH"  # Ensure MetaGPT can be found
MODEL_TYPE="qwen"
DATASET_PATH="/data/user_data/mert/example_mas/programdev_v2"

# Check if Qwen server is running
echo "Checking Qwen model server..."
if curl -s "$BASE_URL/models" > /dev/null; then
    echo "✅ Qwen model server is accessible"
else
    echo "❌ Cannot connect to Qwen model server at $BASE_URL"
    echo "Please ensure your Qwen model is running at http://localhost:12355/v1"
    exit 1
fi

# Check if dataset path exists
if [ ! -d "$DATASET_PATH" ]; then
    echo "❌ Dataset path not found: $DATASET_PATH"
    echo "Please update DATASET_PATH in this script to point to your programdev_v2 dataset"
    exit 1
fi

echo "Dataset path: $DATASET_PATH"
echo "Model type: $MODEL_TYPE"
echo "Starting evaluation..."
echo ""

# Create output directory if it doesn't exist
mkdir -p logs/programdev_v2_qwen

# Run evaluation on subset of examples (modify loop as needed)
for ((i=0; i<100; i++)); do
    DESCRIPTION_FILE="$DATASET_PATH/descriptions_$i.txt"
    
    if [ ! -f "$DESCRIPTION_FILE" ]; then
        echo "⚠️  Skipping $i: Description file not found: $DESCRIPTION_FILE"
        continue
    fi
    
    echo "Processing example $i..."
    LOG_FILE="logs/programdev_v2_qwen/metagpt_qwen_$i.txt"
    
    # Run MetaGPT with Qwen model
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
echo "🎉 MetaGPT ProgramDev V2 evaluation with Qwen model completed!"
echo "Results saved in: logs/programdev_v2_qwen/"
echo "Generated projects can be found in the workspace directories" 