'''
Handles the graphical user interface for the SSH Alias Manager using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from ssh_alias_manager import SSHAliasManager
class SSHAliasGUI:
    def __init__(self, manager):
        self.manager = manager
    def create_main_window(self):
        self.root = tk.Tk()
        self.root.title("SSH Alias Manager")
        add_button = tk.Button(self.root, text="Add Alias", command=self.add_alias_gui)
        add_button.pack(pady=5)
        list_button = tk.Button(self.root, text="List Aliases", command=self.list_aliases_gui)
        list_button.pack(pady=5)
        remove_button = tk.Button(self.root, text="Remove Alias", command=self.remove_alias_gui)
        remove_button.pack(pady=5)
        self.root.mainloop()
    def add_alias_gui(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Alias")
        tk.Label(add_window, text="Alias Name").grid(row=0, column=0)
        tk.Label(add_window, text="Hostname").grid(row=1, column=0)
        tk.Label(add_window, text="User").grid(row=2, column=0)
        tk.Label(add_window, text="Port").grid(row=3, column=0)
        tk.Label(add_window, text="Key File").grid(row=4, column=0)
        alias_name_entry = tk.Entry(add_window)
        hostname_entry = tk.Entry(add_window)
        user_entry = tk.Entry(add_window)
        port_entry = tk.Entry(add_window)
        key_file_entry = tk.Entry(add_window)
        alias_name_entry.grid(row=0, column=1)
        hostname_entry.grid(row=1, column=1)
        user_entry.grid(row=2, column=1)
        port_entry.grid(row=3, column=1)
        key_file_entry.grid(row=4, column=1)
        def add_alias_action():
            alias_name = alias_name_entry.get()
            hostname = hostname_entry.get()
            user = user_entry.get()
            try:
                port = int(port_entry.get())  # Convert port to integer
            except ValueError:
                messagebox.showerror("Error", "Port must be an integer.")
                return
            key_file = key_file_entry.get()
            self.manager.add_alias(alias_name, hostname, user, port, key_file)
            messagebox.showinfo("Success", "Alias added successfully!")
            add_window.destroy()
        add_button = tk.Button(add_window, text="Add", command=add_alias_action)
        add_button.grid(row=5, columnspan=2)
    def list_aliases_gui(self):
        list_window = tk.Toplevel(self.root)
        list_window.title("List Aliases")
        aliases = self.manager.list_aliases()
        for alias_name, details in aliases.items():
            tk.Label(list_window, text=f"{alias_name}: {details}").pack()
    def remove_alias_gui(self):
        remove_window = tk.Toplevel(self.root)
        remove_window.title("Remove Alias")
        tk.Label(remove_window, text="Alias Name").grid(row=0, column=0)
        alias_name_entry = tk.Entry(remove_window)
        alias_name_entry.grid(row=0, column=1)
        def remove_alias_action():
            alias_name = alias_name_entry.get()
            if alias_name in self.manager.list_aliases():
                self.manager.remove_alias(alias_name)
                messagebox.showinfo("Success", "Alias removed successfully!")
            else:
                messagebox.showerror("Error", f"Alias '{alias_name}' does not exist.")
            remove_window.destroy()
        remove_button = tk.Button(remove_window, text="Remove", command=remove_alias_action)
        remove_button.grid(row=1, columnspan=2)