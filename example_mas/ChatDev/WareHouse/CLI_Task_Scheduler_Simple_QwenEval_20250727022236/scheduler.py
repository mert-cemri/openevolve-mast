'''
Module containing the TaskScheduler and TaskFileHandler classes.
Manages tasks and handles file operations.
'''
from task import Task
from datetime import datetime
import os
import logging
class TaskScheduler:
    def __init__(self):
        '''
        Initializes a new task scheduler with an empty list of tasks.
        '''
        self.tasks = []
    def add_task(self, task):
        '''
        Adds a task to the scheduler.
        '''
        self.tasks.append(task)
    def remove_task(self, task):
        '''
        Removes a task from the scheduler.
        '''
        self.tasks.remove(task)
    def get_due_tasks(self):
        '''
        Returns a list of tasks that are due to be executed.
        '''
        now = datetime.now()
        due_tasks = [task for task in self.tasks if task.is_due()]
        return due_tasks
    def execute_tasks(self):
        '''
        Executes all due tasks and removes them from the scheduler.
        '''
        due_tasks = self.get_due_tasks()
        for task in due_tasks:
            try:
                os.system(task.command)
                logging.info(f"Executed task: {task}")
            except Exception as e:
                logging.error(f"Failed to execute task {task}: {e}")
            self.remove_task(task)
class TaskFileHandler:
    def __init__(self, filename):
        '''
        Initializes a new task file handler with the given filename.
        '''
        self.filename = filename
    def read_tasks(self):
        '''
        Reads tasks from the file and returns them as a list of Task objects.
        '''
        tasks = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    date, time, command = line.strip().split(' - ')
                    task = Task(date, time, command)
                    tasks.append(task)
        except FileNotFoundError:
            print(f"File {self.filename} not found. Creating a new file.")
            logging.info(f"File {self.filename} not found. Creating a new file.")
        except Exception as e:
            logging.error(f"Failed to read tasks from file {self.filename}: {e}")
        return tasks
    def write_tasks(self, tasks):
        '''
        Writes the list of tasks to the file.
        '''
        try:
            with open(self.filename, 'w') as file:
                for task in tasks:
                    file.write(f"{task.date} {task.time} - {task.command}\n")
        except Exception as e:
            logging.error(f"Failed to write tasks to file {self.filename}: {e}")