'''
main.py
This file contains the CLI class which handles the command-line interface for the to-do list manager.
'''
from task_manager import TaskManager
class CLI:
    def __init__(self):
        '''
        Initialize the CLI with a TaskManager instance.
        '''
        self.task_manager = TaskManager()
    def display_menu(self):
        '''
        Display the menu options to the user.
        '''
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Complete")
        print("5. Exit")
    def view_tasks(self):
        '''
        Display all tasks to the user.
        '''
        print("\nTasks:")
        for index, task in enumerate(self.task_manager.tasks):
            print(f"{index + 1}. {task}")
    def add_task(self):
        '''
        Prompt the user to add a new task.
        '''
        description = input("Enter the task description: ")
        if description:
            self.task_manager.add_task(description)
            print("Task added successfully.")
    def remove_task(self):
        '''
        Prompt the user to remove a task by index.
        '''
        try:
            index = int(input("Enter the task number to remove: ")) - 1
            self.task_manager.remove_task(index)
            print("Task removed successfully.")
        except (ValueError, IndexError):
            print("Invalid task number.")
    def mark_task_complete(self):
        '''
        Prompt the user to mark a task as complete by index.
        '''
        try:
            index = int(input("Enter the task number to mark as complete: ")) - 1
            self.task_manager.mark_task_complete(index)
            print("Task marked as complete.")
        except (ValueError, IndexError):
            print("Invalid task number.")
    def run(self):
        '''
        Run the CLI application.
        '''
        while True:
            self.display_menu()
            choice = input("Choose an option: ")
            if choice == '1':
                self.view_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.remove_task()
            elif choice == '4':
                self.mark_task_complete()
            elif choice == '5':
                print("Exiting the to-do list manager.")
                break
            else:
                print("Invalid choice. Please try again.")
if __name__ == "__main__":
    cli = CLI()
    cli.run()