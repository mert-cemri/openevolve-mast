'''
Functions to retrieve system information from Linux system files and commands.
'''
import subprocess
def get_os_version():
    '''Retrieve the OS version.'''
    try:
        with open("/etc/os-release") as f:
            for line in f:
                if line.startswith("PRETTY_NAME"):
                    return line.split("=")[1].strip().strip('"')
    except FileNotFoundError:
        return "Unknown OS Version"
def get_kernel_version():
    '''Retrieve the kernel version.'''
    try:
        return subprocess.check_output(["uname", "-r"]).decode().strip()
    except subprocess.CalledProcessError:
        return "Unknown Kernel Version"
def get_cpu_model():
    '''Retrieve the CPU model.'''
    try:
        with open("/proc/cpuinfo") as f:
            for line in f:
                if line.startswith("model name"):
                    return line.split(":")[1].strip()
    except FileNotFoundError:
        return "Unknown CPU Model"
def get_total_ram():
    '''Retrieve the total RAM.'''
    try:
        with open("/proc/meminfo") as f:
            for line in f:
                if line.startswith("MemTotal"):
                    return f"{int(line.split()[1]) // 1024} MB"
    except FileNotFoundError:
        return "Unknown Total RAM"