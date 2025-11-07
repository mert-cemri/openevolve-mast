'''
Manages the graphical user interface for the system resource monitor.
'''
import tkinter as tk
from system_monitor import SystemMonitor
class AppGUI:
    def __init__(self, root):
        '''Initializes the GUI components.'''
        self.root = root
        self.monitor = SystemMonitor()
        self.cpu_label = tk.Label(root, text="CPU Usage: ")
        self.cpu_label.pack()
        self.memory_label = tk.Label(root, text="Memory Usage: ")
        self.memory_label.pack()
        self.disk_label = tk.Label(root, text="Disk Usage: ")
        self.disk_label.pack()
        self.update_button = tk.Button(root, text="Update Now", command=self.update_display)
        self.update_button.pack()
        self.auto_update = False
        self.auto_update_button = tk.Button(root, text="Start Auto Update", command=self.toggle_auto_update)
        self.auto_update_button.pack()
        self.update_display()
    def update_display(self):
        '''Updates the display with the latest system resource usage.'''
        cpu_usage = self.monitor.get_cpu_usage()
        memory_total, memory_used, memory_free = self.monitor.get_memory_usage()
        disk_total, disk_used, disk_free = self.monitor.get_disk_usage()
        self.cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
        self.memory_label.config(text=f"Memory Usage: Total: {memory_total} Used: {memory_used} Free: {memory_free}")
        self.disk_label.config(text=f"Disk Usage: Total: {disk_total} Used: {disk_used} Free: {disk_free}")
        if self.auto_update:
            self.root.after(5000, self.update_display)
    def toggle_auto_update(self):
        '''Toggles the automatic update of the display.'''
        self.auto_update = not self.auto_update
        if self.auto_update:
            self.auto_update_button.config(text="Stop Auto Update")
            self.update_display()
        else:
            self.auto_update_button.config(text="Start Auto Update")