'''
Handles all operations related to tasks.
'''
from file_handler import FileHandler
class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed
    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"[{status}] {self.description}"
class TaskManager:
    def __init__(self):
        self.file_handler = FileHandler("tasks.txt")
        self.tasks = self.file_handler.read_tasks()
    def add_task(self, description):
        new_task = Task(description)
        self.tasks.append(new_task)
        self.file_handler.write_tasks(self.tasks)
        print("Task added successfully.")
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")
    def mark_task_complete(self, task_id):
        if 0 < task_id <= len(self.tasks):
            self.tasks[task_id - 1].completed = True
            self.file_handler.write_tasks(self.tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task ID. Please enter a valid task number.")
    def remove_task(self, task_id):
        if 0 < task_id <= len(self.tasks):
            removed_task = self.tasks.pop(task_id - 1)
            self.file_handler.write_tasks(self.tasks)
            print(f"Task '{removed_task.description}' removed successfully.")
        else:
            print("Invalid task ID. Please enter a valid task number.")