'''
AppGUI class for creating and managing the GUI using tkinter.
'''
import tkinter as tk
from system_monitor import SystemMonitor
class AppGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("System Resource Monitor")
        self.monitor = SystemMonitor()
        self.create_widgets()
        self.start_auto_update()
    def create_widgets(self):
        '''Initializes and places the GUI widgets.'''
        self.cpu_label = tk.Label(self.root, text="CPU Usage: ")
        self.cpu_label.pack()
        self.memory_label = tk.Label(self.root, text="Memory Usage: ")
        self.memory_label.pack()
        self.disk_label = tk.Label(self.root, text="Disk Usage: ")
        self.disk_label.pack()
    def update_display(self):
        '''Updates the display with the latest system resource data.'''
        cpu_usage = self.monitor.get_cpu_usage()
        memory_usage = self.monitor.get_memory_usage()
        disk_usage = self.monitor.get_disk_usage()
        self.cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
        self.memory_label.config(text=f"Memory Usage: {memory_usage['used'] / (1024**3):.2f} GB used / {memory_usage['total'] / (1024**3):.2f} GB total")
        self.disk_label.config(text=f"Disk Usage: {disk_usage['used'] / (1024**3):.2f} GB used / {disk_usage['total'] / (1024**3):.2f} GB total")
    def start_auto_update(self):
        '''Starts the automatic update of the display every few seconds.'''
        self.update_display()
        self.root.after(5000, self.start_auto_update)
    def run(self):
        '''Runs the tkinter main loop.'''
        self.root.mainloop()