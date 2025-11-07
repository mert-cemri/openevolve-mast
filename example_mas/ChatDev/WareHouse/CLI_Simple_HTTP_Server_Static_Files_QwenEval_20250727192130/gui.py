'''
Module containing the logic for the graphical user interface.
'''
import tkinter as tk
from tkinter import messagebox
from server import SimpleHTTPServer
class ServerGUI:
    def __init__(self, server):
        self.server = server
        self.root = tk.Tk()
        self.root.title("Simple HTTP Server")
        self.root.geometry("300x150")
        self.status_label = tk.Label(self.root, text="Server stopped", font=("Helvetica", 12))
        self.status_label.pack(pady=10)
        self.start_button = tk.Button(self.root, text="Start Server", command=self.start_button_click)
        self.start_button.pack(side=tk.LEFT, padx=10)
        self.stop_button = tk.Button(self.root, text="Stop Server", command=self.stop_button_click)
        self.stop_button.pack(side=tk.RIGHT, padx=10)
    def run(self):
        self.root.mainloop()
    def start_button_click(self):
        try:
            self.server.start_server()
            self.update_status("Server running")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.update_status("Server stopped")
    def stop_button_click(self):
        self.server.stop_server()
        self.update_status("Server stopped")
    def update_status(self, status):
        self.status_label.config(text=status)