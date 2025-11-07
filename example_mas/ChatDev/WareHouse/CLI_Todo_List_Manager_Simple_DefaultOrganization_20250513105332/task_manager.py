'''
task_manager.py
This file contains the TaskManager class which handles the logic for managing tasks.
'''
from task import Task
class TaskManager:
    def __init__(self, filename='tasks.txt'):
        '''
        Initialize the TaskManager with a filename for storing tasks.
        '''
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    def add_task(self, description):
        '''
        Add a new task to the list.
        '''
        task = Task(description)
        self.tasks.append(task)
        self.save_tasks()
    def remove_task(self, index):
        '''
        Remove a task by its index.
        '''
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
    def mark_task_complete(self, index):
        '''
        Mark a task as complete by its index.
        '''
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()
    def load_tasks(self):
        '''
        Load tasks from the file.
        '''
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    description, completed = line.strip().split('|')
                    task = Task(description, completed == 'True')
                    self.tasks.append(task)
        except FileNotFoundError:
            pass
    def save_tasks(self):
        '''
        Save tasks to the file.
        '''
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.description}|{task.completed}\n")