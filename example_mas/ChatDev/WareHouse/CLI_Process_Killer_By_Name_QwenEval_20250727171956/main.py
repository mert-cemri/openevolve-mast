'''
Main entry point for the process management tool.
Handles CLI execution.
'''
import sys
from process_manager import ProcessManager
def run_cli():
    pm = ProcessManager()
    process_name = input("Enter process name to search: ")
    processes = pm.list_processes(process_name)
    if not processes:
        print("No processes found.")
        return
    print("Found processes:")
    for pid, name in processes:
        print(f"PID: {pid}, Name: {name}")
    pid_to_kill_input = input("Enter PID(s) to kill (separated by spaces or commas) (or 'q' to quit): ")
    if pid_to_kill_input.lower() == 'q':
        return
    pid_to_kill_list = [pid.strip() for pid in pid_to_kill_input.replace(',', ' ').split()]
    for pid_to_kill in pid_to_kill_list:
        if pid_to_kill.lower() == 'q':
            break
        try:
            pid_to_kill = int(pid_to_kill)
            pm.kill_process(pid_to_kill)
        except ValueError:
            print(f"Invalid PID: {pid_to_kill}")
if __name__ == "__main__":
    run_cli()