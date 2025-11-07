'''
Main entry point for the CLI Task Scheduler application.
'''
from task_scheduler import TaskScheduler
from task_gui import TaskGUI
import tkinter as tk
def main():
    scheduler = TaskScheduler()
    scheduler.load_tasks()
    print("Welcome to the CLI Task Scheduler!")
    while True:
        print("\nOptions:")
        print("1. Add a new task (CLI)")
        print("2. View all tasks (CLI)")
        print("3. Open GUI")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            command = input("Enter the command to execute: ")
            date = input("Enter the date (YYYY-MM-DD): ")
            time = input("Enter the time (HH:MM): ")
            scheduler.add_task(command, date, time)
            print("Task added successfully!")
        elif choice == '2':
            print("\nScheduled Tasks:")
            for task in scheduler.tasks:
                print(f"{task[1]}: {task[0]}")
        elif choice == '3':
            root = tk.Tk()
            app = TaskGUI(root, scheduler)
            root.mainloop()
        elif choice == '4':
            print("Exiting the scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()