'''
Handles the graphical user interface for the memory usage monitor using tkinter.
'''
import tkinter as tk
from tkinter import ttk
from memory_monitor import MemoryMonitor
class GUIMonitor:
    def __init__(self):
        '''
        Initializes the GUI monitor.
        '''
        self.root = tk.Tk()
        self.root.title("Memory Usage Monitor")
        self.monitor = MemoryMonitor()
        self.create_widgets()
    def create_widgets(self):
        '''
        Creates the GUI widgets.
        '''
        self.memory_frame = ttk.Frame(self.root, padding="10")
        self.memory_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.memory_label = ttk.Label(self.memory_frame, text="Memory Usage:")
        self.memory_label.grid(row=0, column=0, sticky=tk.W)
        self.memory_info = ttk.Label(self.memory_frame, text="")
        self.memory_info.grid(row=1, column=0, sticky=tk.W)
        self.processes_frame = ttk.Frame(self.root, padding="10")
        self.processes_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.processes_label = ttk.Label(self.processes_frame, text="Top Memory-Consuming Processes:")
        self.processes_label.grid(row=0, column=0, sticky=tk.W)
        self.processes_tree = ttk.Treeview(self.processes_frame, columns=("PID", "Name", "Memory (MB)"), show="headings")
        self.processes_tree.heading("PID", text="PID")
        self.processes_tree.heading("Name", text="Name")
        self.processes_tree.heading("Memory (MB)", text="Memory (MB)")
        self.processes_tree.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.update_memory_usage()
        self.update_top_processes()
    def update_memory_usage(self):
        '''
        Updates the memory usage information in the GUI.
        '''
        total, available, percent = self.monitor.fetch_system_memory()
        memory_text = f"Total Memory: {total / (1024 ** 3):.2f} GB\nAvailable Memory: {available / (1024 ** 3):.2f} GB\nMemory Usage: {percent}%"
        self.memory_info.config(text=memory_text)
        self.root.after(1000, self.update_memory_usage)
    def update_top_processes(self):
        '''
        Updates the top memory-consuming processes in the GUI.
        '''
        processes = self.monitor.fetch_top_processes()
        for item in self.processes_tree.get_children():
            self.processes_tree.delete(item)
        for pid, name, mem in processes:
            self.processes_tree.insert("", tk.END, values=(pid, name, f"{mem / (1024 ** 2):.2f}"))
        self.root.after(1000, self.update_top_processes)
    def run(self):
        '''
        Runs the GUI memory usage monitor.
        '''
        self.root.mainloop()