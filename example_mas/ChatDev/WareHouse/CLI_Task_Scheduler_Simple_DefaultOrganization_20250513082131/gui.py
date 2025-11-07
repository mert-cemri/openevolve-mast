'''
Implements the GUI for the Task Scheduler using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
import threading
from scheduler import TaskScheduler
class TaskSchedulerGUI:
    def __init__(self):
        self.scheduler = TaskScheduler()
        threading.Thread(target=self.scheduler.run, daemon=True).start()  # Start the scheduler in a separate thread
        self.root = tk.Tk()
        self.root.title("Task Scheduler")
        self.date_label = tk.Label(self.root, text="Date (YYYY-MM-DD):")
        self.date_label.pack()
        self.date_entry = tk.Entry(self.root)
        self.date_entry.pack()
        self.time_label = tk.Label(self.root, text="Time (HH:MM):")
        self.time_label.pack()
        self.time_entry = tk.Entry(self.root)
        self.time_entry.pack()
        self.command_label = tk.Label(self.root, text="Command:")
        self.command_label.pack()
        self.command_entry = tk.Entry(self.root)
        self.command_entry.pack()
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()
    def add_task(self):
        date = self.date_entry.get()
        time_str = self.time_entry.get()
        command = self.command_entry.get()
        if date and time_str and command:
            self.scheduler.add_task(date, time_str, command)
            messagebox.showinfo("Success", "Task added successfully!")
        else:
            messagebox.showwarning("Input Error", "Please fill all fields.")
    def run(self):
        self.root.mainloop()