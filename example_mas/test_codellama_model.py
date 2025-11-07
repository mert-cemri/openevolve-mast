#!/usr/bin/env python3
"""
Test script for CodeLlama integration with ChatDev
This script verifies that the CodeLlama model backend works correctly
"""

import os
import sys
import traceback

# Add ChatDev to path
sys.path.append('ChatDev')

def test_imports():
    """Test that all necessary imports work"""
    print("Testing imports...")
    try:
        from camel.typing import ModelType
        from camel.model_backend import ModelFactory, CodeLlamaModel
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False

def test_model_type():
    """Test that CodeLlama model type exists"""
    print("\nTesting ModelType.CODELLAMA_13B_INSTRUCT...")
    try:
        from camel.typing import ModelType
        model_type = ModelType.CODELLAMA_13B_INSTRUCT
        print(f"✅ ModelType.CODELLAMA_13B_INSTRUCT = {model_type.value}")
        return True
    except AttributeError as e:
        print(f"❌ ModelType.CODELLAMA_13B_INSTRUCT not found: {e}")
        return False

def test_model_factory():
    """Test that ModelFactory can create CodeLlama model"""
    print("\nTesting ModelFactory.create for CodeLlama...")
    try:
        from camel.typing import ModelType
        from camel.model_backend import ModelFactory
        
        model_type = ModelType.CODELLAMA_13B_INSTRUCT
        config = {
            "api_key": "fake-key",
            "base_url": "http://localhost:12355/v1",
            "temperature": 0.1,
            "max_tokens": 1024
        }
        
        model = ModelFactory.create(model_type, config)
        print(f"✅ ModelFactory created: {type(model).__name__}")
        return True
    except Exception as e:
        print(f"❌ ModelFactory.create failed: {e}")
        traceback.print_exc()
        return False

def test_token_limit():
    """Test that token limit is implemented for CodeLlama"""
    print("\nTesting token limit...")
    try:
        from camel.typing import ModelType
        from camel.model_backend import ModelFactory
        
        model_type = ModelType.CODELLAMA_13B_INSTRUCT
        config = {}
        
        model = ModelFactory.create(model_type, config)
        token_limit = model.token_limit
        print(f"✅ Token limit: {token_limit}")
        return True
    except Exception as e:
        print(f"❌ Token limit test failed: {e}")
        return False

def test_tokenizer():
    """Test tokenizer functionality"""
    print("\nTesting tokenizer...")
    try:
        from camel.typing import ModelType
        from camel.model_backend import ModelFactory
        
        model_type = ModelType.CODELLAMA_13B_INSTRUCT
        config = {}
        
        model = ModelFactory.create(model_type, config)
        test_text = "def hello_world():\n    print('Hello, World!')"
        token_count = model._count_tokens(test_text)
        print(f"✅ Tokenizer working. Test text tokens: {token_count}")
        return True
    except Exception as e:
        print(f"❌ Tokenizer test failed: {e}")
        return False

def test_message_conversion():
    """Test message to prompt conversion"""
    print("\nTesting message conversion...")
    try:
        from camel.typing import ModelType
        from camel.model_backend import ModelFactory
        
        model_type = ModelType.CODELLAMA_13B_INSTRUCT
        config = {}
        
        model = ModelFactory.create(model_type, config)
        messages = [
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": "Write a simple function that adds two numbers."},
        ]
        
        prompt = model._convert_messages_to_prompt(messages)
        print(f"✅ Message conversion successful")
        print(f"Sample prompt: {prompt[:200]}...")
        return True
    except Exception as e:
        print(f"❌ Message conversion test failed: {e}")
        return False

def test_server_connection():
    """Test connection to CodeLlama server"""
    print("\nTesting server connection...")
    try:
        import requests
        base_url = os.getenv("BASE_URL", "http://localhost:12355/v1")
        response = requests.get(f"{base_url}/models", timeout=5)
        
        if response.status_code == 200:
            models = response.json()
            print(f"✅ Server accessible. Available models: {[m.get('id', 'unknown') for m in models.get('data', [])]}")
            return True
        else:
            print(f"⚠️  Server responded with status {response.status_code}")
            return False
    except Exception as e:
        print(f"⚠️  Could not connect to server: {e}")
        print("   This is expected if CodeLlama server is not running")
        return False

def main():
    """Run all tests"""
    print("=" * 50)
    print("CodeLlama Integration Test Suite")
    print("=" * 50)
    
    # Set environment variables for testing
    os.environ.setdefault("BASE_URL", "http://localhost:12355/v1")
    os.environ.setdefault("OPENAI_API_KEY", "fake-key")
    os.environ.setdefault("CODELLAMA_MAX_TOKENS", "30208")
    
    tests = [
        test_imports,
        test_model_type,
        test_model_factory,
        test_token_limit,
        test_tokenizer,
        test_message_conversion,
        test_server_connection,
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ Test {test.__name__} crashed: {e}")
            results.append(False)
    
    print("\n" + "=" * 50)
    print("Test Results Summary")
    print("=" * 50)
    
    passed = sum(results)
    total = len(results)
    
    for i, (test, result) in enumerate(zip(tests, results)):
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{i+1}. {test.__name__}: {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! CodeLlama integration is ready.")
        return 0
    else:
        print("⚠️  Some tests failed. Check the output above for details.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 