'''
Module containing the GUI class for the task scheduler.
Provides a graphical user interface for adding and executing tasks.
'''
import tkinter as tk
from tkinter import messagebox
from scheduler import TaskScheduler, TaskFileHandler
from task import Task
import logging
class GUI:
    def __init__(self, root):
        '''
        Initializes the GUI with the given root window.
        '''
        self.root = root
        self.root.title("Task Scheduler")
        self.scheduler = TaskScheduler()
        self.file_handler = TaskFileHandler("tasks.txt")
        self.load_tasks()
        self.create_widgets()
    def create_widgets(self):
        '''
        Creates and arranges the GUI widgets.
        '''
        self.date_label = tk.Label(self.root, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=0, column=0, padx=10, pady=10)
        self.date_entry = tk.Entry(self.root)
        self.date_entry.grid(row=0, column=1, padx=10, pady=10)
        self.time_label = tk.Label(self.root, text="Time (HH:MM):")
        self.time_label.grid(row=1, column=0, padx=10, pady=10)
        self.time_entry = tk.Entry(self.root)
        self.time_entry.grid(row=1, column=1, padx=10, pady=10)
        self.command_label = tk.Label(self.root, text="Command:")
        self.command_label.grid(row=2, column=0, padx=10, pady=10)
        self.command_entry = tk.Entry(self.root)
        self.command_entry.grid(row=2, column=1, padx=10, pady=10)
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.execute_button = tk.Button(self.root, text="Execute Due Tasks", command=self.execute_tasks)
        self.execute_button.grid(row=5, column=0, columnspan=2, pady=10)
    def add_task(self):
        '''
        Adds a new task based on user input.
        '''
        date = self.date_entry.get()
        time = self.time_entry.get()
        command = self.command_entry.get()
        try:
            task = Task(date, time, command)
            self.scheduler.add_task(task)
            self.file_handler.write_tasks(self.scheduler.tasks)
            self.update_task_listbox()
            self.date_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
            self.command_entry.delete(0, tk.END)
            logging.info(f"Task added: {task}")
        except ValueError as e:
            messagebox.showerror("Error", f"Failed to add task: {e}")
            logging.error(f"Failed to add task: {e}")
    def load_tasks(self):
        '''
        Loads tasks from the file and updates the task listbox.
        '''
        self.scheduler.tasks = self.file_handler.read_tasks()
        self.update_task_listbox()
    def update_task_listbox(self):
        '''
        Updates the task listbox with the current tasks.
        '''
        self.task_listbox.delete(0, tk.END)
        for task in self.scheduler.tasks:
            self.task_listbox.insert(tk.END, str(task))
    def execute_tasks(self):
        '''
        Executes all due tasks and updates the task listbox.
        '''
        try:
            self.scheduler.execute_tasks()
            self.file_handler.write_tasks(self.scheduler.tasks)
            self.update_task_listbox()
            messagebox.showinfo("Task Scheduler", "Due tasks executed.")
            logging.info("Due tasks executed.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to execute tasks: {e}")
            logging.error(f"Failed to execute tasks: {e}")