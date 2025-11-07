# Qwen2.5-Coder-32B-Instruct Integration with ChatDev

This document describes how to use your locally hosted Qwen2.5-Coder-32B-Instruct model with the ChatDev framework.

## Overview

The integration allows ChatDev to use your locally hosted Qwen model served via vLLM with OpenAI-compatible API. The implementation is fully backward compatible and doesn't affect existing functionality.

## Prerequisites

1. **Qwen Model Server**: Your Qwen2.5-Coder-32B-Instruct model running via vLLM at `http://localhost:12355/v1`
2. **Python Dependencies**: 
   - Standard ChatDev dependencies
   - **transformers>=4.37.0** (for proper Qwen tokenization)
3. **Environment Variables**: `BASE_URL` and `OPENAI_API_KEY` (can be fake for local models)

## Installation

### 1. Install Dependencies

```bash
# Install transformers for proper Qwen tokenization
pip install transformers>=4.37.0

# Or install all ChatDev requirements (includes transformers)
pip install -r ChatDev/requirements.txt
```

### 2. Set Environment Variables

```bash
export BASE_URL="http://localhost:12355/v1"
export OPENAI_API_KEY="fake-key"  # vLLM doesn't require real API key
```

## Quick Start

### 1. Basic Usage with Qwen Model

```bash
cd ChatDev
python run.py \
    --task "Create a simple calculator CLI application" \
    --name "QwenCalculator" \
    --model "Qwen2.5-Coder-32B-Instruct" \
    --config "Default" \
    --org "MyOrg"
```

### 2. Using the Shell Script

```bash
# Run with default task
./run_chatdev_with_qwen.sh

# Run with custom task
./run_chatdev_with_qwen.sh "Create a web scraper" "WebScraper"
```

### 3. Testing the Integration

```bash
# Run comprehensive test
python test_qwen_model.py

# Show usage examples only
python test_qwen_model.py --examples
```

## Technical Implementation

### Code Changes Made

1. **Model Type Definition** (`ChatDev/camel/typing.py`):
   ```python
   QWEN_2_5_CODER_32B = "Qwen2.5-Coder-32B-Instruct"
   ```

2. **Command Line Integration** (`ChatDev/run.py` and `ChatDev/eval.py`):
   ```python
   'Qwen2.5-Coder-32B-Instruct': ModelType.QWEN_2_5_CODER_32B
   ```

3. **QwenModel Backend** (`ChatDev/camel/model_backend.py`):
   - Custom backend class that uses `client.completions.create()`
   - **Proper Qwen tokenizer** with fallback to tiktoken
   - Converts ChatML messages to prompt format
   - Handles OpenAI-compatible API responses
   - Automatic fallback to localhost:12355/v1

4. **Dependencies** (`ChatDev/requirements.txt`):
   ```
   transformers>=4.37.0
   ```

### Key Features

- **Proper Tokenization**: Uses official Qwen tokenizer for accurate token counting
- **Graceful Fallback**: Falls back to tiktoken if transformers unavailable
- **API Compatibility**: Uses OpenAI's completions endpoint
- **Message Conversion**: Automatically converts ChatML format to prompt format
- **Response Translation**: Converts completions response to chat format for compatibility
- **Environment Integration**: Uses `BASE_URL` and `OPENAI_API_KEY` environment variables
- **Backward Compatibility**: Existing functionality remains unchanged

### Tokenizer Implementation

The integration uses the proper Qwen tokenizer for accurate token counting:

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct", trust_remote_code=True)
```

**Benefits of proper tokenizer:**
- ✅ Accurate token counting for Qwen models
- ✅ Better context window management
- ✅ Proper handling of special tokens
- ✅ Fallback to tiktoken if transformers unavailable

### QwenModel Class Details

The `QwenModel` class handles:

- **Tokenization**: Uses official Qwen tokenizer with tiktoken fallback
- **Prompt Formatting**: Converts messages array to single prompt string
- **Token Management**: Calculates and enforces token limits (32K context)
- **API Calls**: Uses `client.completions.create()` as specified
- **Response Handling**: Converts completions format to chat format

Example prompt conversion:
```
Input Messages:
[
  {"role": "system", "content": "You are a helpful assistant"},
  {"role": "user", "content": "Write a calculator"}
]

Output Prompt:
System: You are a helpful assistant

User: Write a calculator 