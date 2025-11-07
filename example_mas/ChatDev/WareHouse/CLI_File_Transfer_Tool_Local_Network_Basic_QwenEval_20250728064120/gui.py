'''
GUI module to provide a user-friendly interface for the File Transfer Application.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from server import Server
from client import Client
class FileTransferApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Transfer Application")
        self.root.geometry("400x200")
        self.server = Server()
        self.client = Client()
        self.status_label = tk.Label(self.root, text="Status: Ready", wraplength=300)
        self.status_label.pack(pady=10)
        self.start_server_button = tk.Button(self.root, text="Start Server", command=self.start_server)
        self.start_server_button.pack(pady=5)
        self.send_file_button = tk.Button(self.root, text="Send File", command=self.send_file)
        self.send_file_button.pack(pady=5)
    def run(self):
        self.root.mainloop()
    def start_server(self):
        try:
            status = self.server.start_server()
            self.update_status(status)
        except Exception as e:
            self.update_status(f"Error starting server: {e}")
    def send_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                status = self.client.send_file(file_path)
                self.update_status(status)
            except Exception as e:
                self.update_status(f"Error sending file: {e}")
    def update_status(self, message):
        self.status_label.config(text=f"Status: {message}")