'''
Main file for the CLI to-do list manager.
Handles user input and interacts with the TaskManager.
'''
from task_manager import TaskManager
def main():
    task_manager = TaskManager()
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Remove Task")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            task = input("Enter task description: ").strip()
            if not task:
                print("Task description cannot be empty.")
                continue
            task_manager.add_task(task)
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to mark as complete: ").strip())
                task_manager.mark_task_complete(task_id)
            except ValueError:
                print("Invalid input. Please enter a number for task ID.")
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to remove: ").strip())
                task_manager.remove_task(task_id)
            except ValueError:
                print("Invalid input. Please enter a number for task ID.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()