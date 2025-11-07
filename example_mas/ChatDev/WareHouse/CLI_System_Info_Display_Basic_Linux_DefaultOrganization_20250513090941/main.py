'''
Main application file for the System Information CLI tool.
'''
import argparse
from system_info import get_os_version, get_kernel_version, get_cpu_model, get_total_ram
def display_info():
    '''Display system information.'''
    os_version = get_os_version()
    kernel_version = get_kernel_version()
    cpu_model = get_cpu_model()
    total_ram = get_total_ram()
    print(f"OS Version: {os_version}")
    print(f"Kernel Version: {kernel_version}")
    print(f"CPU Model: {cpu_model}")
    print(f"Total RAM: {total_ram}")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Display basic system information on Linux.')
    parser.parse_args()
    display_info()