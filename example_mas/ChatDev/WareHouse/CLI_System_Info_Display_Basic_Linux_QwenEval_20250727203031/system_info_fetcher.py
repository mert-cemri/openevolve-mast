'''
Class to fetch system information such as OS version, kernel version, CPU model, and total RAM.
This class uses system commands and files to gather the necessary information.
'''
import subprocess
class SystemInfoFetcher:
    def get_os_version(self):
        # Use lsb_release -ds to get the OS version
        try:
            return subprocess.check_output(['lsb_release', '-ds']).decode().strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            # Fallback to /etc/os-release if lsb_release is not available
            try:
                with open('/etc/os-release', 'r') as f:
                    for line in f:
                        if line.startswith('PRETTY_NAME='):
                            return line.split('=')[1].strip().strip('"')
            except FileNotFoundError:
                return 'Unknown'
        return 'Unknown'
    def get_kernel_version(self):
        # Use uname -r to get the kernel version
        try:
            return subprocess.check_output(['uname', '-r']).decode().strip()
        except subprocess.CalledProcessError:
            return 'Unknown'
    def get_cpu_model(self):
        # Read /proc/cpuinfo to get the CPU model
        try:
            with open('/proc/cpuinfo', 'r') as f:
                for line in f:
                    if line.startswith('model name'):
                        model_name = line.split(':')[1].strip()
                        if model_name:
                            return model_name
        except FileNotFoundError:
            return 'Unknown'
        return 'Unknown'
    def get_total_ram(self):
        # Read /proc/meminfo to get the total RAM and convert it to GB
        try:
            with open('/proc/meminfo', 'r') as f:
                for line in f:
                    if line.startswith('MemTotal'):
                        return f"{int(line.split(':')[1].strip().split()[0]) / 1024 / 1024:.2f} GB"
        except FileNotFoundError:
            return 'Unknown'
        return 'Unknown'