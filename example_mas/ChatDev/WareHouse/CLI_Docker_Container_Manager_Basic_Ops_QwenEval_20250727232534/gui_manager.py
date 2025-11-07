'''
Handles the GUI operations using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
class GUIManager:
    def __init__(self, root, docker_manager):
        self.root = root
        self.docker_manager = docker_manager
        self.root.title("Docker Container Manager")
    def create_gui(self):
        tk.Label(self.root, text="Docker Container Manager").pack(pady=10)
        tk.Button(self.root, text="List Containers", command=self.list_containers_callback).pack(pady=5)
        tk.Button(self.root, text="Start Container", command=self.start_container_callback).pack(pady=5)
        tk.Button(self.root, text="Stop Container", command=self.stop_container_callback).pack(pady=5)
        tk.Button(self.root, text="View Logs", command=self.view_logs_callback).pack(pady=5)
    def list_containers_callback(self):
        containers = self.docker_manager.list_containers(all_containers=True)
        messagebox.showinfo("Containers", containers)
    def start_container_callback(self):
        container_id_or_name = tk.simpledialog.askstring("Input", "Enter Container ID or Name:")
        if container_id_or_name:
            result = self.docker_manager.start_container(container_id_or_name)
            messagebox.showinfo("Result", result)
    def stop_container_callback(self):
        container_id_or_name = tk.simpledialog.askstring("Input", "Enter Container ID or Name:")
        if container_id_or_name:
            result = self.docker_manager.stop_container(container_id_or_name)
            messagebox.showinfo("Result", result)
    def view_logs_callback(self):
        container_id_or_name = tk.simpledialog.askstring("Input", "Enter Container ID or Name:")
        if container_id_or_name:
            logs = self.docker_manager.view_logs(container_id_or_name)
            messagebox.showinfo("Logs", logs)