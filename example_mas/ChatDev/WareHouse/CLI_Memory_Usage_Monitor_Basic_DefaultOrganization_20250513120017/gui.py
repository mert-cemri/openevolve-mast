'''
Creates a graphical user interface for the memory usage monitor using Tkinter.
'''
import tkinter as tk
from memory_monitor import MemoryMonitor
def create_gui():
    '''Sets up the GUI components and displays memory information.'''
    try:
        root = tk.Tk()
        root.title("Memory Usage Monitor")
        monitor = MemoryMonitor()
        memory_info = monitor.get_memory_info()
        top_processes = monitor.get_top_processes()
        memory_frame = tk.Frame(root)
        memory_frame.pack(pady=10)
        tk.Label(memory_frame, text="Overall Memory Usage:").pack()
        for key, value in memory_info.items():
            tk.Label(memory_frame, text=f"{key}: {value}").pack()
        process_frame = tk.Frame(root)
        process_frame.pack(pady=10)
        tk.Label(process_frame, text="Top Memory-Consuming Processes:").pack()
        for name, memory in top_processes:
            tk.Label(process_frame, text=f"{name}: {memory} KB").pack()
        root.mainloop()
    except tk.TclError as e:
        print("Error: Unable to create GUI. Ensure you are running in a GUI-enabled environment.")
        print(f"Details: {e}")