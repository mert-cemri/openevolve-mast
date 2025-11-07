'''
Class to handle command-line interface interactions.
This class is responsible for displaying the system information in a formatted manner.
'''
class CLI:
    def __init__(self, system_info_fetcher):
        self.system_info_fetcher = system_info_fetcher
    def display_info(self):
        # Display the system information in a formatted manner
        print("System Information:")
        print(f"OS Version: {self.system_info_fetcher.get_os_version()}")
        print(f"Kernel Version: {self.system_info_fetcher.get_kernel_version()}")
        print(f"CPU Model: {self.system_info_fetcher.get_cpu_model()}")
        print(f"Total RAM: {self.system_info_fetcher.get_total_ram()}")