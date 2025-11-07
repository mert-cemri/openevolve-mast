'''
main.py
This module provides a CLI interface for the to-do list manager application, allowing users to interact with the TaskManager class through command-line inputs.
'''
from task_manager import TaskManager
def display_menu():
    print("\nTo-Do List Manager")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Complete")
    print("5. Exit")
def main():
    task_manager = TaskManager()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            for i, task in enumerate(task_manager.tasks):
                status = "Completed" if task['completed'] else "Pending"
                print(f"{i + 1}. {task['task']} [{status}]")
        elif choice == '2':
            task = input("Enter the task: ")
            task_manager.add_task(task)
        elif choice == '3':
            try:
                index = int(input("Enter the task number to remove: ")) - 1
                task_manager.remove_task(index)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        elif choice == '4':
            try:
                index = int(input("Enter the task number to mark as complete: ")) - 1
                task_manager.mark_task_complete(index)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()