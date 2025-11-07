'''
Handles task scheduling and execution.
'''
import time
import threading
import os
from datetime import datetime
class TaskScheduler:
    def __init__(self):
        self.tasks = []
    def add_task(self, command, date, time):
        task_time_str = f"{date} {time}"
        task_time = datetime.strptime(task_time_str, "%Y-%m-%d %H:%M")
        now = datetime.now()
        delay = (task_time - now).total_seconds()
        if delay > 0:
            timer = threading.Timer(delay, self.execute_command, [command])
            timer.start()
            self.tasks.append((command, task_time_str))
            self.save_tasks()
        else:
            print("The specified time is in the past. Task not scheduled.")
    def execute_command(self, command):
        print(f"Executing: {command}")
        os.system(command)  # Execute the command using the system shell
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    command, task_time_str = line.strip().split(',')
                    task_time = datetime.strptime(task_time_str, "%Y-%m-%d %H:%M")
                    now = datetime.now()
                    delay = (task_time - now).total_seconds()
                    if delay > 0:
                        timer = threading.Timer(delay, self.execute_command, [command])
                        timer.start()
                    self.tasks.append((command, task_time_str))
        except FileNotFoundError:
            pass
    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for command, task_time in self.tasks:
                file.write(f"{command},{task_time}\n")
    def run_pending(self):
        while True:
            time.sleep(1)
    def start_scheduler(self):
        thread = threading.Thread(target=self.run_pending)
        thread.start()