'''
Handles reading from and writing to the text file.
'''
import json
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
    def read_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                task_dicts = json.load(file)
                return [Task(task['description'], task['completed']) for task in task_dicts]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    def write_tasks(self, tasks):
        task_dicts = [{'description': task.description, 'completed': task.completed} for task in tasks]
        try:
            with open(self.filename, 'w') as file:
                json.dump(task_dicts, file, indent=4)
        except IOError:
            print("Error writing to file.")