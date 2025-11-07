#!/bin/bash

# ChatDev ProgramDev V2 Evaluation with Qwen2.5-Coder-32B-Instruct
# This script runs the programdev_v2 dataset evaluation using the Qwen model

# Change to ChatDev directory if not already there
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=========================================="
echo "ProgramDev V2 Evaluation with Qwen Model"
echo "=========================================="

# Configuration
export BASE_URL="http://localhost:12355/v1"
export OPENAI_API_KEY="fake-key"
export QWEN_MAX_TOKENS="30208"  # Set max token length as hyperparameter
MODEL_NAME="Qwen2.5-Coder-32B-Instruct"
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
echo "Model: $MODEL_NAME"
echo "Starting evaluation..."
echo ""

# Create output directory if it doesn't exist
mkdir -p data_programdev_v2_qwen

# Run evaluation on 3 examples with 2 samples each
for j in {0..1}; do
    echo "Starting sample batch $j..."
    for ((i=30; i<100; i++)); do
        DESCRIPTION_FILE="$DATASET_PATH/descriptions_$i.txt"
        NAME_FILE="$DATASET_PATH/names_$i.txt"
        
        # Check if files exist
        if [ ! -f "$DESCRIPTION_FILE" ] || [ ! -f "$NAME_FILE" ]; then
            echo "⚠️  Skipping example $i: missing files"
            continue
        fi
        
        TASK=$(cat "$DESCRIPTION_FILE")
        PROJECT_NAME=$(cat "$NAME_FILE")
        
        echo "Running example $i (sample $j): $PROJECT_NAME"
        
        # Run ChatDev with Qwen model
        python run.py \
            --task "$TASK" \
            --name "$PROJECT_NAME" \
            --sample_num "$j" \
            --model "$MODEL_NAME" \
            --config "Default" \
            --org "QwenEval"
        
        if [ $? -eq 0 ]; then
            echo "✅ Completed example $i (sample $j)"
        else
            echo "❌ Failed example $i (sample $j)"
        fi
        
        echo "---"
    done
    echo "Completed sample batch $j"
    echo ""
done

echo "🎉 ProgramDev V2 evaluation with Qwen model completed!"
echo "Results saved in: data_programdev_v2_qwen/"
echo "Generated projects in: WareHouse/*QwenEval*" 