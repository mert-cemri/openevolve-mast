'''
Handles the creation and management of the GUI components using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
class GUIManager:
    def __init__(self, firewall_manager):
        self.firewall_manager = firewall_manager
        self.root = tk.Tk()
        self.root.title("Firewall CLI Utility")
    def create_window(self):
        self.add_widgets()
        self.root.mainloop()
    def add_widgets(self):
        tk.Label(self.root, text="Protocol:").grid(row=0, column=0, padx=10, pady=10)
        self.protocol_entry = tk.Entry(self.root)
        self.protocol_entry.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.root, text="Port:").grid(row=1, column=0, padx=10, pady=10)
        self.port_entry = tk.Entry(self.root)
        self.port_entry.grid(row=1, column=1, padx=10, pady=10)
        tk.Label(self.root, text="Action:").grid(row=2, column=0, padx=10, pady=10)
        self.action_var = tk.StringVar(value="allow")
        tk.Radiobutton(self.root, text="Allow", variable=self.action_var, value="allow").grid(row=2, column=1, padx=10, pady=10)
        tk.Radiobutton(self.root, text="Block", variable=self.action_var, value="block").grid(row=2, column=2, padx=10, pady=10)
        tk.Button(self.root, text="Add Rule", command=self.handle_add_rule).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Remove Rule", command=self.handle_remove_rule).grid(row=3, column=1, padx=10, pady=10)
        tk.Button(self.root, text="List Rules", command=self.handle_list_rules).grid(row=3, column=2, padx=10, pady=10)
    def handle_add_rule(self):
        protocol = self.protocol_entry.get()
        port = self.port_entry.get()
        action = self.action_var.get()
        try:
            self.firewall_manager.add_rule(action, protocol, port)
            messagebox.showinfo("Success", "Rule added successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def handle_remove_rule(self):
        protocol = self.protocol_entry.get()
        port = self.port_entry.get()
        try:
            self.firewall_manager.remove_rule(protocol, port)
            messagebox.showinfo("Success", "Rule removed successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def handle_list_rules(self):
        try:
            rules = self.firewall_manager.list_rules()
            messagebox.showinfo("Rules", rules)
        except Exception as e:
            messagebox.showerror("Error", str(e))