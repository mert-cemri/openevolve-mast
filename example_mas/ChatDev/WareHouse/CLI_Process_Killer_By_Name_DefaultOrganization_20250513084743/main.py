'''
This is the main module that initializes the CLI application for finding and killing processes by name.
'''
import psutil
from process_manager import ProcessManager
def main():
    '''
    Main function to handle the CLI operations for finding and killing processes.
    '''
    process_manager = ProcessManager()
    process_name = input("Enter Process Name: ")
    processes = process_manager.find_processes_by_name(process_name)
    if not processes:
        print("No matching processes found.")
        return
    print("Matching processes:")
    for i, proc in enumerate(processes):
        print(f"{i + 1}. {proc.info['name']} (PID: {proc.info['pid']})")
    try:
        choice = input("Enter the number of the process to kill (or 0 to cancel): ")
        if not choice.isdigit():
            raise ValueError("Non-integer input")
        choice = int(choice)
        if choice == 0:
            print("Operation cancelled.")
            return
        if choice < 1 or choice > len(processes):
            print("Invalid selection. Please enter a number corresponding to a listed process.")
            return
        selected_proc = processes[choice - 1]
        pid = selected_proc.info['pid']
        confirm = input(f"Are you sure you want to kill the process: {selected_proc.info['name']} (PID: {pid})? (yes/no): ")
        if confirm.lower() == 'yes':
            success = process_manager.kill_process(pid)
            if success:
                print("Process killed successfully.")
            else:
                print("Failed to kill the process.")
        else:
            print("Operation cancelled.")
    except ValueError as ve:
        if str(ve) == "Non-integer input":
            print("Invalid input. Please enter a number.")
        else:
            print("Invalid selection. Operation cancelled.")
    except IndexError:
        print("Invalid selection. Operation cancelled.")
if __name__ == "__main__":
    main()