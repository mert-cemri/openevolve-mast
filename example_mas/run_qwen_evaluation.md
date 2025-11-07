# Qwen Model Evaluation on ProgramDev V2 Dataset

## Overview

This guide shows how to run ChatDev evaluation using your Qwen2.5-Coder-32B-Instruct model on the ProgramDev V2 dataset with 100 examples.

## Files Created

### 1. **`ChatDev/run_programdev_v2_qwen.sh`** - Main evaluation script
- Runs 100 examples from programdev_v2 dataset
- Uses Qwen2.5-Coder-32B-Instruct model
- Creates 2 samples per example (200 total runs)
- Includes error checking and progress tracking

### 2. **Updated `ChatDev/run.py`** - Model-specific logging
- Automatically creates different output directories based on model:
  - `data_programdev_v2_qwen/` for Qwen models
  - `data_programdev_v2_claude/` for Claude models  
  - `data_programdev_v2/` for GPT models (vanilla)

## Prerequisites

1. **Qwen server running** at `http://localhost:12355/v1`
2. **Dataset available** at `/home/mert/mlsys/programdev_v2/`
3. **Dependencies installed**: `pip install transformers>=4.37.0`

## Usage

### 1. Quick Start
```bash
# Make sure your Qwen server is running
curl http://localhost:12355/v1/models

# Run the evaluation
cd ChatDev
./run_programdev_v2_qwen.sh
```

### 2. Check Progress
The script will show progress for each example:
```
Running example 0 (sample 0): calculator_project
✅ Completed example 0 (sample 0)
---
Running example 1 (sample 0): web_scraper_tool
✅ Completed example 1 (sample 0)
---
```

### 3. Output Structure
```
ChatDev/
├── data_programdev_v2_qwen/           # Log files
│   ├── calculator_project_0_qwen.log
│   ├── calculator_project_1_qwen.log
│   ├── web_scraper_tool_0_qwen.log
│   └── ...
└── WareHouse/                         # Generated projects
    ├── calculator_project_QwenEval_timestamp/
    ├── web_scraper_tool_QwenEval_timestamp/
    └── ...
```

## Customization

### Update Dataset Path
Edit the script to point to your dataset location:
```bash
# In run_programdev_v2_qwen.sh
DATASET_PATH="/your/path/to/programdev_v2"
```

### Run Subset of Examples
Modify the loop to run fewer examples:
```bash
# Change this line in the script
for ((i=0; i<10; i++)); do  # Run only first 10 examples
```

### Different Configuration
Use different ChatDev configuration:
```bash
# In the script, change:
--config "Prompted" \     # Instead of "Default"
--org "YourOrgName"       # Custom organization name
```

## Monitoring

### Check Server Status
```bash
curl http://localhost:12355/v1/models
```

### Monitor Progress
```bash
# Watch log files being created
watch -n 5 "ls -la ChatDev/data_programdev_v2_qwen/ | wc -l"

# Check latest generated projects
ls -lt ChatDev/WareHouse/*QwenEval* | head -5
```

### Resume from Specific Example
If the script stops, you can resume by modifying the loop:
```bash
# Start from example 50 instead of 0
for ((i=50; i<100; i++)); do
```

## Comparison with Other Models

The logging system now separates results by model:

- **Qwen results**: `data_programdev_v2_qwen/*.log`
- **GPT results**: `data_programdev_v2/*.log`  
- **Claude results**: `data_programdev_v2_claude/*.log`

This makes it easy to compare performance across different models on the same dataset.

## Troubleshooting

### Server Connection Issues
```bash
# Check if server is running
curl http://localhost:12355/v1/models

# Restart your Qwen server if needed
python -m vllm.entrypoints.openai.api_server \
    --model Qwen/Qwen2.5-Coder-32B-Instruct \
    --port 12355 --host 0.0.0.0
```

### Missing Dataset Files
```bash
# Check dataset structure
ls /home/mert/mlsys/programdev_v2/descriptions_*.txt | wc -l
ls /home/mert/mlsys/programdev_v2/names_*.txt | wc -l
```

### Disk Space
The evaluation will generate ~200 projects, ensure you have sufficient disk space:
```bash
df -h .
```

## Expected Runtime

- **Per example**: 2-5 minutes (depends on task complexity)
- **100 examples × 2 samples**: ~8-16 hours total
- **Recommendation**: Run overnight or in screen/tmux session

```bash
# Run in screen session
screen -S qwen_eval
cd ChatDev && ./run_programdev_v2_qwen.sh
# Ctrl+A+D to detach, screen -r qwen_eval to resume
``` 