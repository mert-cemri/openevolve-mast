'''
Contains the GUI class for the graphical user interface.
'''
import tkinter as tk
from tkinter import messagebox
from env_manager import EnvVarManager
class GUI:
    def __init__(self, env_manager):
        self.env_manager = env_manager
        self.root = tk.Tk()
        self.root.title("Environment Variable Manager")
    def create_main_window(self):
        '''Set up the main window with buttons and input fields.'''
        self.var_name_entry = tk.Entry(self.root, width=30)
        self.var_name_entry.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.root, text="Variable Name").grid(row=0, column=0)
        self.var_value_entry = tk.Entry(self.root, width=30)
        self.var_value_entry.grid(row=1, column=1, padx=10, pady=10)
        tk.Label(self.root, text="Variable Value").grid(row=1, column=0)
        self.persistent_var = tk.IntVar()
        tk.Checkbutton(self.root, text="Persistent", variable=self.persistent_var).grid(row=2, column=1)
        tk.Button(self.root, text="Set Variable", command=self.handle_set_var).grid(row=3, column=0, pady=10)
        tk.Button(self.root, text="Unset Variable", command=self.handle_unset_var).grid(row=3, column=1, pady=10)
        self.var_listbox = tk.Listbox(self.root, width=50)
        self.var_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.update_display()
        self.root.mainloop()
    def update_display(self):
        '''Update the display with the current list of environment variables.'''
        self.var_listbox.delete(0, tk.END)
        for name, value in self.env_manager.list_vars():
            self.var_listbox.insert(tk.END, f"{name}={value}")
    def handle_set_var(self):
        '''Handle setting a new environment variable from the GUI.'''
        name = self.var_name_entry.get()
        value = self.var_value_entry.get()
        persistent = bool(self.persistent_var.get())
        if name and value:
            self.env_manager.set_var(name, value, persistent)
            self.update_display()
            messagebox.showinfo("Success", f"Variable '{name}' set successfully.")
        else:
            messagebox.showwarning("Input Error", "Please enter both name and value.")
    def handle_unset_var(self):
        '''Handle unsetting an environment variable from the GUI.'''
        name = self.var_name_entry.get()
        persistent = bool(self.persistent_var.get())
        if name:
            self.env_manager.unset_var(name, persistent)
            self.update_display()
            messagebox.showinfo("Success", f"Variable '{name}' unset successfully.")
        else:
            messagebox.showwarning("Input Error", "Please enter the variable name.")