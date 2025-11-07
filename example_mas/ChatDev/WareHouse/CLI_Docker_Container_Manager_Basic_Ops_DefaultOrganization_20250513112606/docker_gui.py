'''
Creates a GUI for interacting with Docker containers using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from docker_manager import DockerManager
class DockerGUI:
    def __init__(self, docker_manager):
        self.docker_manager = docker_manager
        self.root = tk.Tk()
        self.root.title("Docker CLI Manager")
    def create_main_window(self):
        self.container_list = tk.Listbox(self.root, width=80, height=20)
        self.container_list.pack()
        self.update_container_list()
        start_button = tk.Button(self.root, text="Start Container", command=self.handle_start)
        start_button.pack()
        stop_button = tk.Button(self.root, text="Stop Container", command=self.handle_stop)
        stop_button.pack()
        logs_button = tk.Button(self.root, text="View Logs", command=self.handle_view_logs)
        logs_button.pack()
        self.root.mainloop()
    def update_container_list(self):
        self.container_list.delete(0, tk.END)
        containers = self.docker_manager.list_containers(all_containers=True)
        for container in containers.splitlines():
            self.container_list.insert(tk.END, container)
    def handle_start(self):
        selected = self.container_list.curselection()
        if selected:
            container_info = self.container_list.get(selected[0])
            container_id = container_info.split()[0]
            self.docker_manager.start_container(container_id)
            self.update_container_list()
        else:
            messagebox.showwarning("Warning", "No container selected.")
    def handle_stop(self):
        selected = self.container_list.curselection()
        if selected:
            container_info = self.container_list.get(selected[0])
            container_id = container_info.split()[0]
            self.docker_manager.stop_container(container_id)
            self.update_container_list()
        else:
            messagebox.showwarning("Warning", "No container selected.")
    def handle_view_logs(self):
        selected = self.container_list.curselection()
        if selected:
            container_info = self.container_list.get(selected[0])
            container_id = container_info.split()[0]
            logs = self.docker_manager.view_logs(container_id)
            logs_window = tk.Toplevel(self.root)
            logs_window.title(f"Logs for {container_id}")
            text_area = tk.Text(logs_window, wrap='word')
            text_area.insert(tk.END, logs)
            text_area.pack(expand=True, fill='both')
        else:
            messagebox.showwarning("Warning", "No container selected.")