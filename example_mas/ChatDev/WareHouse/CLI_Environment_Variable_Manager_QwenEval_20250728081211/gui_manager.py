'''
Manages the GUI components and interactions.
'''
import tkinter as tk
from tkinter import messagebox
from environment_manager import EnvironmentManager
class GUIManager:
    def __init__(self, root, env_manager):
        self.root = root
        self.env_manager = env_manager
    def create_widgets(self):
        self.list_button = tk.Button(self.root, text="List Variables", command=self.on_list)
        self.list_button.pack(pady=5)
        self.name_label = tk.Label(self.root, text="Variable Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)
        self.value_label = tk.Label(self.root, text="Variable Value:")
        self.value_label.pack(pady=5)
        self.value_entry = tk.Entry(self.root)
        self.value_entry.pack(pady=5)
        self.set_button = tk.Button(self.root, text="Set Variable", command=self.on_set)
        self.set_button.pack(pady=5)
        self.unset_button = tk.Button(self.root, text="Unset Variable", command=self.on_unset)
        self.unset_button.pack(pady=5)
    def on_list(self):
        variables = self.env_manager.list_variables()
        message = "\n".join(f"{key}: {value}" for key, value in variables.items())
        messagebox.showinfo("Environment Variables", message)
    def on_set(self):
        name = self.name_entry.get()
        value = self.value_entry.get()
        if name and value:
            self.env_manager.set_variable(name, value, persistent=True)
            messagebox.showinfo("Success", f"Variable {name} set to {value}.")
        else:
            messagebox.showerror("Error", "Please enter both name and value.")
    def on_unset(self):
        name = self.name_entry.get()
        if name:
            self.env_manager.unset_variable(name)
            messagebox.showinfo("Success", f"Variable {name} unset.")
        else:
            messagebox.showerror("Error", "Please enter the variable name.")