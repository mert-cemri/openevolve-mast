#!/usr/bin/env python3
"""
Test script to verify the standalone_multi_agent.py fixes
"""

import subprocess
import sys
import os

def test_standalone():
    """Test the standalone multi-agent with different configurations"""
    
    test_cases = [
        {
            "idea": "build me a simple calculator script in python",
            "model": "openai",
            "rounds": 2
        },
        {
            "idea": "create a function to reverse a string",
            "model": "openai", 
            "rounds": 1
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n{'='*60}")
        print(f"Test Case {i}: {test['idea'][:30]}...")
        print(f"Model: {test['model']}, Rounds: {test['rounds']}")
        print('='*60)
        
        cmd = [
            sys.executable,
            "examples/standalone_multi_agent.py",
            "--idea", test["idea"],
            "--model_type", test["model"],
            "--n_round", str(test["rounds"])
        ]
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=30  # 30 second timeout
            )
            
            if result.returncode == 0:
                print("✓ Test passed")
                # Check if log directory was created
                log_dir = os.path.join(os.getcwd(), "metagpt_logs", test["model"].lower())
                if os.path.exists(log_dir):
                    print(f"✓ Log directory created: {log_dir}")
                    # List subdirectories
                    subdirs = [d for d in os.listdir(log_dir) if os.path.isdir(os.path.join(log_dir, d))]
                    if subdirs:
                        print(f"  Found {len(subdirs)} idea directories")
                else:
                    print(f"✗ Log directory not found: {log_dir}")
            else:
                print(f"✗ Test failed with return code: {result.returncode}")
                print(f"Error output:\n{result.stderr[-500:]}")  # Last 500 chars of error
                
        except subprocess.TimeoutExpired:
            print("✗ Test timed out after 30 seconds")
        except Exception as e:
            print(f"✗ Test error: {e}")
    
    print(f"\n{'='*60}")
    print("Testing complete")
    print('='*60)
    
    # Show the final log directory structure
    base_log_dir = os.path.join(os.getcwd(), "metagpt_logs")
    if os.path.exists(base_log_dir):
        print("\nFinal log directory structure:")
        for root, dirs, files in os.walk(base_log_dir):
            level = root.replace(base_log_dir, '').count(os.sep)
            indent = ' ' * 2 * level
            print(f'{indent}{os.path.basename(root)}/')
            subindent = ' ' * 2 * (level + 1)
            for file in files[:3]:  # Show first 3 files
                print(f'{subindent}{file}')
            if len(files) > 3:
                print(f'{subindent}... and {len(files)-3} more files')

if __name__ == "__main__":
    test_standalone()