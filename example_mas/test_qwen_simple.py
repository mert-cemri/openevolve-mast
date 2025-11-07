#!/usr/bin/env python3
"""
Simple test script for Qwen integration with MetaGPT.
"""
import sys
import os

# Add MetaGPT to path
sys.path.insert(0, "/data/user_data/mert/example_mas/meta_gpt/MetaGPT")

def test_imports():
    """Test basic imports"""
    try:
        from metagpt.configs.llm_config import LLMConfig, LLMType
        print("✅ Basic MetaGPT imports successful")
        
        # Check if Qwen is in LLM types
        qwen_type = LLMType.QWEN
        print(f"✅ Qwen LLM type found: {qwen_type}")
        
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

def test_qwen_config():
    """Test Qwen configuration"""
    try:
        from metagpt.configs.llm_config import LLMConfig, LLMType
        
        # Create Qwen configuration
        config = LLMConfig()
        config.api_type = LLMType.QWEN
        config.model = "Qwen2.5-Coder-32B-Instruct"
        config.base_url = "http://localhost:12355/v1"
        config.api_key = "fake-key"
        config.temperature = 0.7
        config.max_token = 4096
        
        print("✅ Qwen configuration created successfully")
        print(f"   Model: {config.model}")
        print(f"   API Type: {config.api_type}")
        return True
    except Exception as e:
        print(f"❌ Qwen config failed: {e}")
        return False

def test_qwen_provider():
    """Test Qwen provider import"""
    try:
        from metagpt.provider.qwen_api import QwenLLM
        print("✅ QwenLLM provider imported successfully")
        return True
    except Exception as e:
        print(f"❌ QwenLLM import failed: {e}")
        return False

def test_build_script_params():
    """Test that build script can handle model_type parameter"""
    try:
        # Test the main function signature we modified
        import inspect
        sys.path.append("/data/user_data/mert/example_mas/meta_gpt/MetaGPT/examples")
        
        # Import the modified script
        import build_customized_multi_agents as build_script
        
        # Check if main function has model_type parameter
        sig = inspect.signature(build_script.main)
        params = list(sig.parameters.keys())
        
        if 'model_type' in params:
            print("✅ Build script supports model_type parameter")
            return True
        else:
            print(f"❌ Build script missing model_type parameter. Found: {params}")
            return False
    except Exception as e:
        print(f"❌ Build script test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=== Simple Qwen Integration Test ===\n")
    
    tests = [
        ("Basic Imports", test_imports),
        ("Qwen Configuration", test_qwen_config),
        ("Qwen Provider", test_qwen_provider),
        ("Build Script Parameters", test_build_script_params)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n--- {test_name} ---")
        if test_func():
            passed += 1
        
    print(f"\n=== Results ===")
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("\n🎉 All basic tests passed!")
        print("\nNext steps:")
        print("1. Start your Qwen server: http://localhost:12355/v1")
        print("2. Run the Qwen script:")
        print("   cd meta_gpt/MetaGPT")
        print("   ./run_programdev_v2_qwen.sh")
        return True
    else:
        print(f"\n❌ {total - passed} test(s) failed.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 