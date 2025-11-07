import json
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()
    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
    def remove_task(self, task):
        self.tasks.remove(task)
        self.save_tasks()
    def mark_task_complete(self, task):
        self.tasks.remove(task)
        self.save_tasks()
    def clear_tasks(self):
        self.tasks = []
        self.save_tasks()
    def load_tasks(self):
        with open("tasks.json", "r") as f:
            self.tasks = json.load(f)
    def save_tasks(self):
        """Save the tasks to a JSON file.
        The tasks are saved in a JSON file named "tasks.json" in the current working directory.
        """
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f)