#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from task_manager import TaskManager
class ToDoListManager(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("To-Do List Manager")
        self.master.geometry("500x500")
        self.create_widgets()
        self.task_manager = TaskManager()
    def create_widgets(self):
        self.task_list = tk.Listbox(self.master, height=10, width=50)
        self.task_list.grid(row=0, column=0, rowspan=2, padx=5, pady=5)
        self.add_task_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=1, padx=5, pady=5)
        self.remove_task_button = tk.Button(self.master, text="Remove Task", command=self.remove_task)
        self.remove_task_button.grid(row=1, column=1, padx=5, pady=5)
        self.mark_task_button = tk.Button(self.master, text="Mark Task as Complete", command=self.mark_task_complete)
        self.mark_task_button.grid(row=2, column=1, padx=5, pady=5)
        self.clear_tasks_button = tk.Button(self.master, text="Clear Tasks", command=self.clear_tasks)
        self.clear_tasks_button.grid(row=3, column=1, padx=5, pady=5)
        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.destroy)
        self.quit_button.grid(row=4, column=1, padx=5, pady=5)
    def add_task(self):
        task = messagebox.askstring("Add Task", "Enter the task to add:")
        if task:
            self.task_manager.add_task(task)
            self.task_list.insert(tk.END, task)
    def remove_task(self):
        task = self.task_list.get(tk.ACTIVE)
        if task:
            self.task_manager.remove_task(task)
            self.task_list.delete(tk.ACTIVE)
    def mark_task_complete(self):
        task = self.task_list.get(tk.ACTIVE)
        if task:
            self.task_manager.mark_task_complete(task)
            self.task_list.delete(tk.ACTIVE)
    def clear_tasks(self):
        self.task_manager.clear_tasks()
        self.task_list.delete(0, tk.END)
if __name__ == "__main__":
    root = tk.Tk()
    ToDoListManager(root)
    root.mainloop()