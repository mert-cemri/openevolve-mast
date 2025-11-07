'''
Contains the TaskScheduler and Task classes for managing and executing tasks.
'''
import sched
import time
from datetime import datetime
import subprocess
class Task:
    def __init__(self, date, time, command):
        self.date = date
        self.time = time
        self.command = command
class TaskScheduler:
    def __init__(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.tasks = []
        self.load_tasks()
    def add_task(self, date, time_str, command):
        task_time = datetime.strptime(f"{date} {time_str}", "%Y-%m-%d %H:%M")
        delay = (task_time - datetime.now()).total_seconds()
        if delay > 0:
            self.scheduler.enter(delay, 1, self.execute_task, (command,))
            task = Task(date, time_str, command)
            self.tasks.append(task)
            self.save_tasks()
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    date, time_str, command = line.strip().split(',')
                    task_time = datetime.strptime(f"{date} {time_str}", "%Y-%m-%d %H:%M")
                    delay = (task_time - datetime.now()).total_seconds()
                    if delay > 0:
                        self.scheduler.enter(delay, 1, self.execute_task, (command,))
                        task = Task(date, time_str, command)
                        self.tasks.append(task)
        except FileNotFoundError:
            pass
    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task.date},{task.time},{task.command}\n")
    def execute_task(self, command):
        print(f"Executing: {command}")
        subprocess.run(command, shell=True)
    def run(self):
        self.scheduler.run(blocking=True)