#!/usr/bin/env python3
"""
Direct test of Qwen provider to verify it's working correctly.
"""
import sys
import os
import asyncio

# Add MetaGPT to path
sys.path.insert(0, "/data/user_data/mert/example_mas/meta_gpt/MetaGPT")

async def test_qwen_provider():
    """Test Qwen provider directly"""
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
        
        print(f"✅ Created config with api_type: {config.api_type}")
        
        # Create LLM instance
        llm = create_llm_instance(config)
        print(f"✅ Created LLM instance: {type(llm).__name__}")
        
        # Test a simple question
        print("🚀 Testing Qwen API call...")
        response = await llm.aask("What is 2+2? Give a brief answer.")
        print(f"✅ Qwen response: {response}")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

async def main():
    print("=== Direct Qwen Provider Test ===\n")
    
    # Check if server is running
    try:
        import requests
        response = requests.get("http://localhost:12355/v1/models", timeout=5)
        if response.status_code == 200:
            print("✅ Qwen server is accessible")
        else:
            print(f"⚠️ Qwen server returned status {response.status_code}")
    except Exception as e:
        print(f"❌ Cannot connect to Qwen server: {e}")
        return False
    
    success = await test_qwen_provider()
    
    if success:
        print("\n🎉 Direct Qwen provider test successful!")
    else:
        print("\n❌ Direct Qwen provider test failed!")
    
    return success

if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1) 