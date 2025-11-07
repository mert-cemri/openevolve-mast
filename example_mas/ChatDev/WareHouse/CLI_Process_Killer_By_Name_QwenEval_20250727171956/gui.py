'''
Handles the graphical user interface for the process management tool.
'''
import tkinter as tk
from tkinter import messagebox
from process_manager import ProcessManager
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Process Manager")
        self.pm = ProcessManager()
        self.name_label = tk.Label(self.root, text="Process Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()
        self.search_button = tk.Button(self.root, text="Search", command=self.search_processes)
        self.search_button.pack()
        self.process_listbox = tk.Listbox(self.root, height=10, width=50)
        self.process_listbox.pack()
        self.kill_button = tk.Button(self.root, text="Kill Selected", command=self.kill_selected_process)
        self.kill_button.pack()
    def run(self):
        self.root.mainloop()
    def search_processes(self):
        self.process_listbox.delete(0, tk.END)
        process_name = self.name_entry.get()
        processes = self.pm.list_processes(process_name)
        for pid, name in processes:
            self.process_listbox.insert(tk.END, f"PID: {pid}, Name: {name}")
    def kill_selected_process(self):
        selected_index = self.process_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("No Selection", "Please select a process to kill.")
            return
        selected_text = self.process_listbox.get(selected_index)
        pid = int(selected_text.split(",")[0].split(":")[1].strip())
        if self.pm.kill_process(pid):
            messagebox.showinfo("Process Killed", f"Process {pid} killed.")
            self.search_processes()
        else:
            messagebox.showinfo("Process Not Killed", "Process not killed.")