#!/usr/bin/env python3
"""
Test script for Qwen2.5-Coder-32B-Instruct integration with ChatDev.

This script demonstrates how to use the locally hosted Qwen model
with ChatDev framework.

Prerequisites:
1. Qwen model server running at http://localhost:12355/v1
2. Environment variables set appropriately
3. transformers package installed for proper tokenization

Usage:
    python test_qwen_model.py
"""

import os
import subprocess
import sys

def check_dependencies():
    """Check if required dependencies are available."""
    print("Checking dependencies...")
    
    # Check transformers
    try:
        from transformers import AutoTokenizer
        print("✅ transformers package available")
    except ImportError:
        print("❌ transformers package not found")
        print("Please install it: pip install transformers>=4.37.0")
        return False
    
    # Check tiktoken (fallback)
    try:
        import tiktoken
        print("✅ tiktoken package available (fallback)")
    except ImportError:
        print("❌ tiktoken package not found (needed for fallback)")
        return False
    
    return True

def test_qwen_tokenizer():
    """Test the Qwen tokenizer directly."""
    print("\nTesting Qwen tokenizer...")
    
    try:
        from transformers import AutoTokenizer
        tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct", trust_remote_code=True)
        
        # Test tokenization
        test_text = "Hello, this is a test message for the Qwen tokenizer."
        tokens = tokenizer.encode(test_text)
        print(f"✅ Qwen tokenizer working: '{test_text}' -> {len(tokens)} tokens")
        return True
        
    except Exception as e:
        print(f"❌ Qwen tokenizer test failed: {e}")
        print("This may be due to network issues or missing dependencies.")
        print("The system will fall back to tiktoken approximation.")
        return False

def test_qwen_integration():
    """Test the Qwen model integration."""
    
    print("Testing Qwen2.5-Coder-32B-Instruct Integration with ChatDev")
    print("=" * 60)
    
    # Check dependencies first
    if not check_dependencies():
        return False
    
    # Test tokenizer
    test_qwen_tokenizer()
    
    # Check if the model server is accessible
    print("\n1. Checking model server accessibility...")
    try:
        import requests
        response = requests.get("http://localhost:12355/v1/models", timeout=5)
        if response.status_code == 200:
            print("✅ Model server is accessible")
            try:
                models_data = response.json()
                print(f"Available models: {[model.get('id', 'unknown') for model in models_data.get('data', [])]}")
            except:
                print("Model server responded but couldn't parse model list")
        else:
            print("❌ Model server returned status:", response.status_code)
            return False
    except Exception as e:
        print(f"❌ Cannot connect to model server: {e}")
        print("Please ensure your Qwen model is running at http://localhost:12355/v1")
        return False
    
    # Set environment variables for the test
    print("\n2. Setting up environment...")
    os.environ["BASE_URL"] = "http://localhost:12355/v1"
    os.environ["OPENAI_API_KEY"] = "fake-key"  # vLLM doesn't require real API key
    print("✅ Environment configured")
    
    # Prepare ChatDev command
    print("\n3. Running ChatDev with Qwen model...")
    
    task = "Create a simple Python calculator that can perform basic arithmetic operations (addition, subtraction, multiplication, division). The calculator should have a command-line interface where users can input expressions and get results."
    
    cmd = [
        "python", "ChatDev/run.py",
        "--task", task,
        "--name", "QwenCalculator_Test",
        "--model", "Qwen2.5-Coder-32B-Instruct",
        "--config", "Default",
        "--org", "QwenTestOrg"
    ]
    
    print(f"Command: {' '.join(cmd)}")
    print("\nExecuting ChatDev with Qwen model...")
    print("This may take several minutes depending on the task complexity.")
    print("-" * 60)
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        
        if result.returncode == 0:
            print("✅ ChatDev completed successfully with Qwen model!")
            print("\nOutput directory: WareHouse/QwenCalculator_Test_QwenTestOrg_*")
            return True
        else:
            print("❌ ChatDev failed:")
            print("STDERR:", result.stderr[-500:])  # Last 500 chars
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ ChatDev execution timed out (10 minutes)")
        return False
    except Exception as e:
        print(f"❌ Error running ChatDev: {e}")
        return False

def show_usage_examples():
    """Show usage examples for the Qwen integration."""
    
    print("\n" + "=" * 60)
    print("USAGE EXAMPLES")
    print("=" * 60)
    
    print("\n1. Install dependencies:")
    print("pip install transformers>=4.37.0")
    
    print("\n2. Basic usage with Qwen model:")
    print('python ChatDev/run.py \\')
    print('    --task "Create a simple web scraper" \\')
    print('    --name "WebScraper" \\')
    print('    --model "Qwen2.5-Coder-32B-Instruct" \\')
    print('    --config "Default"')
    
    print("\n3. With custom configuration:")
    print('python ChatDev/run.py \\')
    print('    --task "Build a todo list application" \\')
    print('    --name "TodoApp" \\')
    print('    --model "Qwen2.5-Coder-32B-Instruct" \\')
    print('    --config "Prompted" \\')
    print('    --org "MyCompany"')
    
    print("\n4. Environment variables:")
    print('export BASE_URL="http://localhost:12355/v1"')
    print('export OPENAI_API_KEY="fake-key"')
    
    print("\n5. Evaluation with Qwen:")
    print('python ChatDev/eval.py \\')
    print('    --name "HumanEval/0" \\')
    print('    --sample_num 0 \\')
    print('    --model "Qwen2.5-Coder-32B-Instruct"')

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--examples":
        show_usage_examples()
    else:
        success = test_qwen_integration()
        show_usage_examples()
        
        if success:
            print("\n🎉 Qwen integration test completed successfully!")
        else:
            print("\n❌ Qwen integration test failed. Please check the errors above.")
            sys.exit(1) 