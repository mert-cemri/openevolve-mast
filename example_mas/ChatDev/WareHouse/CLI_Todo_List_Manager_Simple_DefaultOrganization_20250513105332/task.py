'''
task.py
This file contains the Task class which represents a single task in the to-do list.
'''
class Task:
    def __init__(self, description, completed=False):
        '''
        Initialize a new task with a description and completion status.
        '''
        self.description = description
        self.completed = completed
    def __str__(self):
        '''
        Return a string representation of the task.
        '''
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"