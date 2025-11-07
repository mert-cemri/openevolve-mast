#!/usr/bin/env python3
"""
Simple verification script for Qwen tokenizer integration.

This script tests the tokenizer functionality without running the full ChatDev pipeline.
"""

def test_tokenizers():
    """Compare Qwen tokenizer vs tiktoken approximation."""
    
    print("Qwen Tokenizer Verification")
    print("=" * 40)
    
    # Test text samples
    test_texts = [
        "Hello, world!",
        "Write a Python function to calculate fibonacci numbers.",
        "Create a simple web scraper using Python and BeautifulSoup.",
        "System: You are a helpful assistant\n\nUser: Write code\n\nAssistant:",
    ]
    
    # Test Qwen tokenizer
    qwen_available = False
    try:
        from transformers import AutoTokenizer
        qwen_tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct", trust_remote_code=True)
        qwen_available = True
        print("✅ Qwen tokenizer loaded successfully")
    except Exception as e:
        print(f"❌ Could not load Qwen tokenizer: {e}")
    
    # Test tiktoken fallback
    tiktoken_available = False
    try:
        import tiktoken
        tiktoken_encoder = tiktoken.get_encoding("cl100k_base")
        tiktoken_available = True
        print("✅ Tiktoken fallback available")
    except Exception as e:
        print(f"❌ Could not load tiktoken: {e}")
    
    if not qwen_available and not tiktoken_available:
        print("❌ No tokenizer available!")
        return False
    
    print("\nTokenization Comparison:")
    print("-" * 40)
    
    for i, text in enumerate(test_texts, 1):
        print(f"\n{i}. Text: \"{text[:50]}{'...' if len(text) > 50 else ''}\"")
        
        if qwen_available:
            qwen_tokens = qwen_tokenizer.encode(text)
            print(f"   Qwen tokenizer: {len(qwen_tokens)} tokens")
        
        if tiktoken_available:
            tiktoken_tokens = tiktoken_encoder.encode(text)
            print(f"   Tiktoken (approx): {len(tiktoken_tokens)} tokens")
        
        if qwen_available and tiktoken_available:
            diff = len(qwen_tokens) - len(tiktoken_tokens)
            print(f"   Difference: {diff:+d} tokens")
    
    return True

def test_qwen_model_backend():
    """Test the QwenModel backend tokenization directly."""
    
    print("\n" + "=" * 40)
    print("QwenModel Backend Test")
    print("=" * 40)
    
    try:
        # Import the QwenModel class
        import sys
        import os
        sys.path.append(os.path.join(os.path.dirname(__file__), 'ChatDev'))
        
        from camel.typing import ModelType
        from camel.model_backend import QwenModel
        
        # Create a QwenModel instance
        model_config = {
            "base_url": "http://localhost:12355/v1",
            "api_key": "fake-key"
        }
        
        qwen_model = QwenModel(ModelType.QWEN_2_5_CODER_32B, model_config)
        
        # Test token counting
        test_text = "This is a test message for token counting."
        token_count = qwen_model._count_tokens(test_text)
        
        print(f"✅ QwenModel backend working")
        print(f"Test text: \"{test_text}\"")
        print(f"Token count: {token_count}")
        
        # Test prompt conversion
        messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Write a hello world program"}
        ]
        
        prompt = qwen_model._convert_messages_to_prompt(messages)
        prompt_tokens = qwen_model._count_tokens(prompt)
        
        print(f"\nPrompt conversion test:")
        print(f"Messages: {len(messages)} messages")
        print(f"Converted prompt: {prompt_tokens} tokens")
        print(f"Prompt preview: \"{prompt[:100]}...\"")
        
        return True
        
    except Exception as e:
        print(f"❌ QwenModel backend test failed: {e}")
        return False

if __name__ == "__main__":
    print("Starting Qwen tokenizer verification...\n")
    
    success1 = test_tokenizers()
    success2 = test_qwen_model_backend()
    
    print("\n" + "=" * 40)
    if success1 and success2:
        print("🎉 All tests passed! Qwen integration is ready.")
    elif success1:
        print("⚠️  Tokenizer works but backend has issues.")
    else:
        print("❌ Tests failed. Please check dependencies.")
        print("\nTo install dependencies:")
        print("pip install transformers>=4.37.0") 