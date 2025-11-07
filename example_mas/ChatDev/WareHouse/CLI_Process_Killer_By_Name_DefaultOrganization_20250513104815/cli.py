'''
Provides a command-line interface for interacting with the ProcessManager.
'''
from process_manager import ProcessManager
class CLI:
    def __init__(self):
        self.manager = ProcessManager()
    def run(self):
        '''
        Starts the CLI and handles user input.
        '''
        process_name = input("Enter the process name to search: ")
        processes = self.manager.list_processes_by_name(process_name)
        if not processes:
            print("No matching processes found.")
            return
        print("Matching processes:")
        for proc in processes:
            print(f"PID: {proc['pid']}, Name: {proc['name']}")
            confirm = input(f"Do you want to kill process {proc['pid']}? (y/n): ")
            if confirm.lower() == 'y':
                if self.manager.kill_process(proc['pid']):
                    print(f"Successfully killed process {proc['pid']}")
                else:
                    print(f"Failed to kill process {proc['pid']}")