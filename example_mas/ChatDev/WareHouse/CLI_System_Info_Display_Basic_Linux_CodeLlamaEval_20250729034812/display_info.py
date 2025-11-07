#!/usr/bin/env python3
import subprocess
def display_os_version():
    version = subprocess.check_output(['uname', '-s']).decode().strip()
    print(f'OS version: {version}')
def display_kernel_version():
    version = subprocess.check_output(['uname', '-r']).decode().strip()
    print(f'Kernel version: {version}')
def display_cpu_model():
    model = subprocess.check_output(['cat', '/proc/cpuinfo']).decode().strip()
    print(f'CPU model: {model}')
def display_total_ram():
    total_ram = subprocess.check_output(['cat', '/proc/meminfo']).decode().strip()
    print(f'Total RAM: {total_ram}')