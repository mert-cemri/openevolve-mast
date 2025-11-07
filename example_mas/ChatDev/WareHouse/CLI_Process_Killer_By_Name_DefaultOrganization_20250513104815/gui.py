'''
Provides a graphical user interface for interacting with the ProcessManager.
'''
import tkinter as tk
from tkinter import messagebox
from process_manager import ProcessManager
class GUI:
    def __init__(self):
        self.manager = ProcessManager()
        self.root = tk.Tk()
        self.root.title("Process Manager")
    def start(self):
        '''
        Initializes and starts the GUI application.
        '''
        tk.Label(self.root, text="Enter Process Name:").pack()
        self.process_name_entry = tk.Entry(self.root)
        self.process_name_entry.pack()
        tk.Button(self.root, text="Find Processes", command=self.find_processes).pack()
        self.process_listbox = tk.Listbox(self.root)
        self.process_listbox.pack()
        tk.Button(self.root, text="Kill Selected Process", command=self.kill_selected_process).pack()
        self.root.mainloop()
    def find_processes(self):
        '''
        Finds and lists processes matching the entered name.
        '''
        process_name = self.process_name_entry.get()
        processes = self.manager.list_processes_by_name(process_name)
        self.process_listbox.delete(0, tk.END)
        for proc in processes:
            self.process_listbox.insert(tk.END, f"PID: {proc['pid']}, Name: {proc['name']}")
    def kill_selected_process(self):
        '''
        Kills the selected process from the listbox.
        '''
        selected = self.process_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "No process selected.")
            return
        process_info = self.process_listbox.get(selected[0])
        pid = int(process_info.split(",")[0].split(":")[1].strip())
        if self.manager.kill_process(pid):
            messagebox.showinfo("Success", f"Successfully killed process {pid}")
            self.find_processes()  # Refresh the list
        else:
            messagebox.showerror("Error", f"Failed to kill process {pid}")