'''
This module contains the VaultGUI class, which handles the graphical user interface for the password vault.
'''
import tkinter as tk
from tkinter import messagebox
class VaultGUI:
    def __init__(self, vault):
        self.vault = vault
        self.root = tk.Tk()
        self.root.title("Password Vault")
        self.master_password = None
        self.create_widgets()
    def create_widgets(self):
        self.master_password_label = tk.Label(self.root, text="Master Password:")
        self.master_password_label.pack()
        self.master_password_entry = tk.Entry(self.root, show="*")
        self.master_password_entry.pack()
        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.pack()
    def login(self):
        self.master_password = self.master_password_entry.get()
        if self.vault.load_vault(self.master_password):
            messagebox.showinfo("Success", "Vault loaded successfully!")
            self.show_vault()
        else:
            messagebox.showerror("Error", "Invalid master password!")
    def show_vault(self):
        self.master_password_entry.destroy()
        self.login_button.destroy()
        self.service_label = tk.Label(self.root, text="Service:")
        self.service_label.pack()
        self.service_entry = tk.Entry(self.root)
        self.service_entry.pack()
        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        self.add_button = tk.Button(self.root, text="Add Entry", command=self.add_entry)
        self.add_button.pack()
        self.get_button = tk.Button(self.root, text="Get Entry", command=self.get_entry)
        self.get_button.pack()
        self.remove_button = tk.Button(self.root, text="Remove Entry", command=self.remove_entry)
        self.remove_button.pack()
        self.save_button = tk.Button(self.root, text="Save Vault", command=self.save_vault)
        self.save_button.pack()
    def add_entry(self):
        service = self.service_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.vault.add_entry(service, username, password)
        messagebox.showinfo("Success", "Entry added successfully!")
    def get_entry(self):
        service = self.service_entry.get()
        entry = self.vault.get_entry(service)
        if entry:
            messagebox.showinfo("Entry", f"Username: {entry['username']}\nPassword: {entry['password']}")
        else:
            messagebox.showerror("Error", "Entry not found!")
    def remove_entry(self):
        service = self.service_entry.get()
        self.vault.remove_entry(service)
        messagebox.showinfo("Success", "Entry removed successfully!")
    def save_vault(self):
        self.vault.save_vault(self.master_password)
        messagebox.showinfo("Success", "Vault saved successfully!")
    def start(self):
        self.root.mainloop()