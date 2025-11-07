'''
Manages the graphical user interface for the password vault application.
'''
import tkinter as tk
from tkinter import simpledialog, messagebox
from vault import PasswordVault
class VaultGUI:
    def __init__(self, vault):
        self.vault = vault
        self.root = tk.Tk()
        self.root.title("Password Vault")
        self.setup_gui()
    def setup_gui(self):
        self.master_password_label = tk.Label(self.root, text="Enter Master Password:")
        self.master_password_label.pack()
        self.master_password_entry = tk.Entry(self.root, show="*")
        self.master_password_entry.pack()
        self.unlock_button = tk.Button(self.root, text="Unlock", command=self.unlock_vault)
        self.unlock_button.pack()
        self.entries_listbox = tk.Listbox(self.root)
        self.entries_listbox.pack()
        self.add_button = tk.Button(self.root, text="Add Entry", command=self.add_entry)
        self.add_button.pack()
    def unlock_vault(self):
        master_password = self.master_password_entry.get()
        self.vault.create_master_key(master_password)
        self.vault.load_vault()
        self.update_entries_listbox()
    def add_entry(self):
        service = simpledialog.askstring("Service", "Enter service name:")
        username = simpledialog.askstring("Username", "Enter username:")
        password = simpledialog.askstring("Password", "Enter password:")
        if service and username and password:
            self.vault.add_entry(service, username, password)
            self.update_entries_listbox()
    def update_entries_listbox(self):
        self.entries_listbox.delete(0, tk.END)
        for service, credentials in self.vault.get_entries().items():
            entry = f"{service}: {credentials['username']} / {credentials['password']}"
            self.entries_listbox.insert(tk.END, entry)
    def run(self):
        self.root.mainloop()