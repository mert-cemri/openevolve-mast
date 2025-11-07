#!/usr/bin/env python3
"""
Test script for CodeLlama integration with MetaGPT.
This script verifies that the CodeLlama provider can be imported and configured correctly.
"""
import sys
import os
import asyncio

# Add MetaGPT to path
sys.path.insert(0, "/data/user_data/mert/example_mas/meta_gpt/MetaGPT")

def test_codellama_import():
    """Test that CodeLlama provider can be imported"""
    try:
        from metagpt.provider.codellama_api import CodeLlamaLLM
        from metagpt.configs.llm_config import LLMConfig, LLMType
        print("✅ CodeLlamaLLM imported successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to import CodeLlamaLLM: {e}")
        return False

def test_codellama_config():
    """Test that CodeLlama can be configured"""
    try:
        from metagpt.configs.llm_config import LLMConfig, LLMType
        
        # Create CodeLlama configuration
        config = LLMConfig()
        config.api_type = LLMType.CODELLAMA
        config.model = "CodeLlama-13b-Instruct"
        config.base_url = "http://localhost:12355/v1"
        config.api_key = "fake-key"
        config.temperature = 0.7
        config.max_token = 2048
        
        print(f"✅ CodeLlama config created: {config.api_type}")
        print(f"   Model: {config.model}")
        print(f"   Base URL: {config.base_url}")
        return True
    except Exception as e:
        print(f"❌ Failed to create CodeLlama config: {e}")
        return False

async def test_codellama_api():
    """Test CodeLlama API call"""
    try:
        from metagpt.configs.llm_config import LLMConfig, LLMType
        from metagpt.provider.llm_provider_registry import create_llm_instance
        
        # Create CodeLlama configuration
        config = LLMConfig()
        config.api_type = LLMType.CODELLAMA
        config.model = "CodeLlama-13b-Instruct"
        config.base_url = "http://localhost:12355/v1"
        config.api_key = "fake-key"
        config.temperature = 0.7
        config.max_token = 2048
        
        # Create LLM instance
        llm = create_llm_instance(config)
        print(f"✅ Created LLM instance: {type(llm).__name__}")
        
        # Test simple API call
        response = await llm.aask("What is 2 + 2?")
        print(f"✅ CodeLlama API call successful: {response[:50]}...")
        return True
    except Exception as e:
        print(f"❌ CodeLlama API call failed: {e}")
        return False

def test_codellama_enum():
    """Test that CODELLAMA is in LLMType enum"""
    try:
        from metagpt.configs.llm_config import LLMType
        codellama_type = LLMType.CODELLAMA
        print(f"✅ CODELLAMA enum found: {codellama_type}")
        return True
    except Exception as e:
        print(f"❌ CODELLAMA enum not found: {e}")
        return False

async def main():
    """Run all tests"""
    print("🧪 Testing CodeLlama Integration with MetaGPT")
    print("=" * 50)
    
    tests = [
        ("Import Test", test_codellama_import),
        ("Enum Test", test_codellama_enum),
        ("Config Test", test_codellama_config),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n🔍 Running {test_name}...")
        try:
            result = test_func()
            results.append(result)
            if result:
                print(f"✅ {test_name} passed")
            else:
                print(f"❌ {test_name} failed")
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results.append(False)
    
    # Test API call (requires server to be running)
    print(f"\n🔍 Running API Test...")
    try:
        api_result = await test_codellama_api()
        results.append(api_result)
        if api_result:
            print("✅ API Test passed")
        else:
            print("❌ API Test failed")
    except Exception as e:
        print(f"❌ API Test failed with exception: {e}")
        results.append(False)
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Summary:")
    passed = sum(results)
    total = len(results)
    print(f"   ✅ Passed: {passed}/{total}")
    print(f"   ❌ Failed: {total - passed}/{total}")
    
    if passed == total:
        print("\n🎉 All tests passed! CodeLlama integration is working correctly.")
        return True
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    import asyncio
    asyncio.run(main()) 