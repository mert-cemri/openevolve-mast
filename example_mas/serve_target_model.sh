#!/bin/bash

hostname --ip-address
MODEL="Qwen/Qwen2.5-7B-Instruct"
MODEL_NAME="Qwen2.5-7B-Instruct"
# MODEL="Qwen/Qwen2.5-Math-7B-Instruct"
# MODEL_NAME="Qwen2.5-Math-7B-Instruct"

export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1


if [ -z "$1" ]; then
  echo "No CUDA device specified. Using default: 4"
  CUDA_DEVICE=4
else
  CUDA_DEVICE=$1
fi

export CUDA_VISIBLE_DEVICES=$CUDA_DEVICE
python -m vllm.entrypoints.openai.api_server \
        --model $MODEL \
        --served-model-name $MODEL_NAME \
        --tensor-parallel-size 1 \
        --port 12345 \
        --host 0.0.0.0 \
        --trust-remote-code \
        --gpu_memory_utilization 0.45 \
        --max_model_len 8192 \
        --enable_prefix_caching
        # --port 12347 \
        # --port 12352 \

        # --port 12347 \
        # --host 0.0.0.0 \
        # --trust-remote-code \
        # --gpu_memory_utilization 0.6

        # --port 12345 \
        # --host 0.0.0.0 \
        # --trust-remote-code \
        # --gpu_memory_utilization 0.6 \
        # --enable_prefix_caching

        
        