'''
Main entry point for the CLI Task Scheduler application.
'''
import threading
from scheduler import TaskScheduler
def main():
    scheduler = TaskScheduler()
    threading.Thread(target=scheduler.run, daemon=True).start()  # Start the scheduler in a separate thread
    while True:
        print("\nTask Scheduler CLI")
        print("1. Add Task")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            time_str = input("Enter time (HH:MM): ")
            command = input("Enter command: ")
            scheduler.add_task(date, time_str, command)
            print("Task added successfully!")
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()