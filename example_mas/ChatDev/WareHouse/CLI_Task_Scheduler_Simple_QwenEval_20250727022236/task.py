'''
Module containing the Task class.
Represents a task with a specific date, time, and command.
'''
from datetime import datetime
class Task:
    def __init__(self, date, time, command):
        '''
        Initializes a new task with the given date, time, and command.
        '''
        try:
            self.datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        except ValueError:
            raise ValueError("Date and time must be in the format YYYY-MM-DD HH:MM")
        self.date = date
        self.time = time
        self.command = command
    def __str__(self):
        '''
        Returns a string representation of the task.
        '''
        return f"{self.date} {self.time} - {self.command}"
    def is_due(self):
        '''
        Checks if the task is due to be executed.
        '''
        return datetime.now() >= self.datetime