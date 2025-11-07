'''
GUI class to handle graphical user interface operations.
'''
import tkinter as tk
class GUI:
    def __init__(self, monitor):
        self.monitor = monitor
    def create_main_window(self):
        '''Sets up the main window and widgets.'''
        self.root = tk.Tk()
        self.root.title("Memory Usage Monitor")
        self.memory_info_label = tk.Label(self.root, text="Overall Memory Usage:")
        self.memory_info_label.pack()
        self.processes_label = tk.Label(self.root, text="Top Memory-Consuming Processes:")
        self.processes_label.pack()
        self.update_display()
        self.root.mainloop()
    def update_display(self):
        '''Updates the display with current memory usage and top processes.'''
        meminfo = self.monitor.get_memory_info()
        meminfo_text = "\n".join([f"{key}: {value} kB" for key, value in meminfo.items()])
        self.memory_info_label.config(text=f"Overall Memory Usage:\n{meminfo_text}")
        top_processes = self.monitor.get_top_processes(5)
        processes_text = "\n".join([f"PID: {pid}, Memory Usage: {mem_usage} kB" for pid, mem_usage in top_processes])
        self.processes_label.config(text=f"Top Memory-Consuming Processes:\n{processes_text}")
        self.root.after(5000, self.update_display)  # Update every 5 seconds