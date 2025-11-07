'''
Module to handle the command-line interface for the tool.
'''
import logging
class CLIInterface:
    def __init__(self, process_finder, process_killer):
        self.process_finder = process_finder
        self.process_killer = process_killer
    def run(self):
        """Runs the CLI tool."""
        process_name = input("Enter the name of the process to find and kill: ").strip()
        if not process_name:
            print("Process name cannot be empty.")
            logging.warning("Process name was empty.")
            return
        processes = self.process_finder.find_processes(process_name)
        if not processes:
            print("No processes found with that name.")
            logging.info(f"No processes found with name: {process_name}")
            return
        self.list_processes(processes)
        for proc in processes:
            if self.confirm_kill(proc['pid']):
                if self.process_killer.kill_process(proc['pid']):
                    print(f"Process {proc['pid']} killed successfully.")
                else:
                    print(f"Failed to kill process {proc['pid']}.")
        logging.info("Process selection and killing completed.")
    def list_processes(self, processes):
        """Lists the processes found."""
        print("Found the following processes:")
        for proc in processes:
            print(f"PID: {proc['pid']}, Name: {proc['name']}")
    def confirm_kill(self, pid):
        """Asks for confirmation before killing a process with a limited number of attempts."""
        max_attempts = 3
        attempts = 0
        while attempts < max_attempts:
            confirm = input(f"Are you sure you want to kill process {pid}? (y/n): ").strip().lower()
            if confirm in ['y', 'n']:
                logging.info(f"User confirmed kill for process {pid}: {confirm == 'y'}")
                return confirm == 'y'
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
                logging.warning(f"Invalid confirmation input for process {pid}.")
                attempts += 1
        print("Too many invalid attempts. Exiting confirmation for process {pid}.")
        logging.warning(f"Too many invalid attempts for process {pid}.")
        return False