'''
Handles the graphical user interface interactions.
Provides methods to add, list, and remove SSH aliases.
'''
import tkinter as tk
from tkinter import messagebox, simpledialog
from ssh_alias_manager import SSHAliasManager, Alias
from config_file import ConfigFile
class GUIInterface:
    def __init__(self):
        self.manager = SSHAliasManager('ssh_aliases.json')
        self.root = tk.Tk()
        self.root.title("SSH Alias Manager")
        self.setup_ui()
    def setup_ui(self):
        tk.Label(self.root, text="SSH Alias Manager").grid(row=0, column=0, columnspan=2)
        tk.Button(self.root, text="Add Alias", command=self.add_alias).grid(row=1, column=0)
        tk.Button(self.root, text="List Aliases", command=self.list_aliases).grid(row=1, column=1)
        tk.Button(self.root, text="Remove Alias", command=self.remove_alias).grid(row=2, column=0)
        tk.Button(self.root, text="Exit", command=self.root.quit).grid(row=2, column=1)
    def run(self):
        self.root.mainloop()
    def add_alias(self):
        try:
            hostname = simpledialog.askstring("Input", "Enter hostname:")
            user = simpledialog.askstring("Input", "Enter user:")
            port_str = simpledialog.askstring("Input", "Enter port:")
            key_file = simpledialog.askstring("Input", "Enter key file:")
            if not hostname or not user or not port_str or not key_file:
                messagebox.showerror("Error", "Hostname, user, port, and key file are required.")
                return
            try:
                port = int(port_str)
            except ValueError:
                messagebox.showerror("Error", "Port must be a number.")
                return
            if not ConfigFile(key_file).exists():
                messagebox.showerror("Error", f"Key file {key_file} does not exist.")
                return
            alias = Alias(hostname, user, port, key_file)
            self.manager.add_alias(alias)
            messagebox.showinfo("Success", f"Alias {hostname} added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    def list_aliases(self):
        aliases = self.manager.list_aliases()
        if not aliases:
            messagebox.showinfo("Info", "No aliases found.")
        else:
            message = "\n".join([f"Hostname: {alias.hostname}, User: {alias.user}, Port: {alias.port}, Key File: {alias.key_file}" for alias in aliases])
            messagebox.showinfo("Aliases", message)
    def remove_alias(self):
        hostname = simpledialog.askstring("Input", "Enter hostname to remove:")
        if not hostname:
            messagebox.showerror("Error", "Hostname is required.")
            return
        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to remove the alias {hostname}?")
        if not confirm:
            messagebox.showinfo("Info", "Operation cancelled.")
            return
        self.manager.remove_alias(hostname)
        messagebox.showinfo("Success", f"Alias {hostname} removed successfully.")