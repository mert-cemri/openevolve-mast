'''
Provides a graphical user interface for the task scheduler.
'''
import tkinter as tk
from tkinter import messagebox
class TaskGUI:
    def __init__(self, master, scheduler):
        self.master = master
        self.scheduler = scheduler
        self.create_widgets()
        self.scheduler.start_scheduler()
    def create_widgets(self):
        self.command_label = tk.Label(self.master, text="Command:")
        self.command_label.grid(row=0, column=0)
        self.command_entry = tk.Entry(self.master)
        self.command_entry.grid(row=0, column=1)
        self.date_label = tk.Label(self.master, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=1, column=0)
        self.date_entry = tk.Entry(self.master)
        self.date_entry.grid(row=1, column=1)
        self.time_label = tk.Label(self.master, text="Time (HH:MM):")
        self.time_label.grid(row=2, column=0)
        self.time_entry = tk.Entry(self.master)
        self.time_entry.grid(row=2, column=1)
        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=3, column=0, columnspan=2)
        self.task_list = tk.Listbox(self.master)
        self.task_list.grid(row=4, column=0, columnspan=2)
        self.update_task_list()
    def add_task(self):
        command = self.command_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        if command and date and time:
            self.scheduler.add_task(command, date, time)
            self.update_task_list()
            messagebox.showinfo("Success", "Task added successfully!")
        else:
            messagebox.showwarning("Input Error", "Please fill all fields.")
    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for command, task_time in self.scheduler.tasks:
            self.task_list.insert(tk.END, f"{task_time}: {command}")