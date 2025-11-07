'''
Helper functions for common tasks.
'''
import time
def print_with_delay(text, delay=1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()
    time.sleep(delay)