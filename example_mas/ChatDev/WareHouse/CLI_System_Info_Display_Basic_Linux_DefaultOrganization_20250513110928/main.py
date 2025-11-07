'''
DOCSTRING: A CLI tool to display basic system information on Linux, such as OS version, kernel version, CPU model, and total RAM.
'''
import subprocess
def get_os_version():
    '''
    DOCSTRING: Retrieve and return the OS version.
    '''
    try:
        with open("/etc/os-release") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("PRETTY_NAME"):
                    return line.split("=")[1].strip().strip('"')
    except Exception as e:
        return f"Error retrieving OS version: {e}"
def get_kernel_version():
    '''
    DOCSTRING: Retrieve and return the kernel version.
    '''
    try:
        return subprocess.check_output(["uname", "-r"]).decode().strip()
    except Exception as e:
        return f"Error retrieving kernel version: {e}"
def get_cpu_model():
    '''
    DOCSTRING: Retrieve and return the CPU model.
    '''
    try:
        with open("/proc/cpuinfo") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("model name"):
                    return line.split(":")[1].strip()
    except Exception as e:
        return f"Error retrieving CPU model: {e}"
def get_total_ram():
    '''
    DOCSTRING: Retrieve and return the total RAM.
    '''
    try:
        with open("/proc/meminfo") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("MemTotal"):
                    # Convert kB to MB for better readability
                    mem_kb = int(line.split(":")[1].strip().split()[0])
                    mem_mb = mem_kb // 1024
                    return f"{mem_mb} MB"
    except Exception as e:
        return f"Error retrieving total RAM: {e}"
def main():
    '''
    DOCSTRING: Main function to retrieve and print system information.
    '''
    os_version = get_os_version()
    kernel_version = get_kernel_version()
    cpu_model = get_cpu_model()
    total_ram = get_total_ram()
    info_text = (
        f"OS Version: {os_version}\n"
        f"Kernel Version: {kernel_version}\n"
        f"CPU Model: {cpu_model}\n"
        f"Total RAM: {total_ram}\n"
    )
    print(info_text)
if __name__ == "__main__":
    main()