#!/usr/bin/env python3
"""
Test script for Qwen integration with MetaGPT.
This script verifies that the Qwen provider can be imported and configured correctly.
"""
import sys
import os

# Add MetaGPT to path
sys.path.append("meta_gpt/MetaGPT")

def test_qwen_import():
    """Test that Qwen provider can be imported"""
    try:
        from metagpt.provider.qwen_api import QwenLLM
        from metagpt.configs.llm_config import LLMConfig, LLMType
        print("✅ QwenLLM imported successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to import QwenLLM: {e}")
        return False

def test_qwen_config():
    """Test that Qwen can be configured"""
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
        
        print("✅ QwenLLM configuration created successfully")
        print(f"   Model: {config.model}")
        print(f"   API Type: {config.api_type}")
        print(f"   Base URL: {config.base_url}")
        return True
    except Exception as e:
        print(f"❌ Failed to configure QwenLLM: {e}")
        return False

def test_qwen_provider_registry():
    """Test that Qwen provider is registered"""
    try:
        from metagpt.provider.llm_provider_registry import LLM_REGISTRY
        from metagpt.configs.llm_config import LLMType
        
        # Check if Qwen is in the registry
        qwen_provider = LLM_REGISTRY.get_provider(LLMType.QWEN)
        print("✅ QwenLLM provider found in registry")
        print(f"   Provider class: {qwen_provider.__name__}")
        return True
    except Exception as e:
        print(f"❌ Failed to find QwenLLM in provider registry: {e}")
        return False

def test_qwen_instantiation():
    """Test that Qwen provider can be instantiated"""
    try:
        from metagpt.configs.llm_config import LLMConfig, LLMType
        from metagpt.provider.llm_provider_registry import create_llm_instance
        
        # Create Qwen configuration
        config = LLMConfig()
        config.api_type = LLMType.QWEN
        config.model = "Qwen2.5-Coder-32B-Instruct"
        config.base_url = "http://localhost:12355/v1"
        config.api_key = "fake-key"
        config.temperature = 0.7
        config.max_token = 4096
        
        # Create LLM instance
        llm = create_llm_instance(config)
        print("✅ QwenLLM instance created successfully")
        print(f"   Instance type: {type(llm).__name__}")
        print(f"   Model: {llm.model}")
        return True
    except Exception as e:
        print(f"❌ Failed to instantiate QwenLLM: {e}")
        return False

def test_build_script_import():
    """Test that the modified build script can import necessary modules"""
    try:
        # Add the examples directory to path
        examples_path = "meta_gpt/MetaGPT/examples"
        if examples_path not in sys.path:
            sys.path.append(examples_path)
        
        # Test imports used in build_customized_multi_agents.py
        from metagpt.configs.llm_config import LLMConfig, LLMType
        from metagpt.context import Context
        
        print("✅ Build script imports work correctly")
        return True
    except Exception as e:
        print(f"❌ Failed to import modules for build script: {e}")
        return False

def main():
    """Run all tests"""
    print("=== Testing Qwen Integration with MetaGPT ===\n")
    
    tests = [
        ("Import Test", test_qwen_import),
        ("Configuration Test", test_qwen_config),
        ("Registry Test", test_qwen_provider_registry),
        ("Instantiation Test", test_qwen_instantiation),
        ("Build Script Import Test", test_build_script_import)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n--- {test_name} ---")
        if test_func():
            passed += 1
        else:
            print(f"Test failed: {test_name}")
    
    print(f"\n=== Test Results ===")
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed! Qwen integration is working correctly.")
        print("\nYou can now run:")
        print("  cd meta_gpt/MetaGPT")
        print("  ./run_programdev_v2_qwen.sh")
        return True
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 