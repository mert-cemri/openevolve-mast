'''
DockerGUI class to create the GUI using tkinter.
'''
import tkinter as tk
from tkinter import messagebox, scrolledtext
from docker_manager import DockerManager
class DockerGUI:
    def __init__(self):
        self.manager = DockerManager()
        self.root = tk.Tk()
        self.root.title("Docker CLI Manager")
        self.container_listbox = None
    def create_main_window(self):
        '''
        Set up the main window and layout.
        '''
        self.root.geometry("600x400")
        # Container list
        self.container_listbox = tk.Listbox(self.root, width=80, height=15)
        self.container_listbox.pack(pady=10)
        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack()
        tk.Button(btn_frame, text="List Running Containers", command=self.update_container_list).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Start Container", command=self.start_container).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Stop Container", command=self.stop_container).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="View Logs", command=self.show_logs).pack(side=tk.LEFT, padx=5)
        self.update_container_list()
        self.root.mainloop()
    def update_container_list(self):
        '''
        Refresh the list of containers displayed.
        '''
        self.container_listbox.delete(0, tk.END)
        containers = self.manager.list_containers()
        for container in containers:
            self.container_listbox.insert(tk.END, f"{container.id[:12]}: {container.name} (Status: {container.status})")
    def start_container(self):
        '''
        Start the selected container.
        '''
        selected = self.container_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "No container selected")
            return
        container_info = self.container_listbox.get(selected[0])
        container_id = container_info.split(":")[0]
        try:
            self.manager.start_container(container_id)
            messagebox.showinfo("Success", "Container started")
            self.update_container_list()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def stop_container(self):
        '''
        Stop the selected container.
        '''
        selected = self.container_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "No container selected")
            return
        container_info = self.container_listbox.get(selected[0])
        container_id = container_info.split(":")[0]
        try:
            self.manager.stop_container(container_id)
            messagebox.showinfo("Success", "Container stopped")
            self.update_container_list()
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def show_logs(self):
        '''
        Display logs of the selected container.
        '''
        selected = self.container_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "No container selected")
            return
        container_info = self.container_listbox.get(selected[0])
        container_id = container_info.split(":")[0]
        try:
            logs = self.manager.view_logs(container_id)
            log_window = tk.Toplevel(self.root)
            log_window.title(f"Logs for {container_id}")
            log_text = scrolledtext.ScrolledText(log_window, width=80, height=20)
            log_text.pack()
            log_text.insert(tk.END, logs)
        except Exception as e:
            messagebox.showerror("Error", str(e))