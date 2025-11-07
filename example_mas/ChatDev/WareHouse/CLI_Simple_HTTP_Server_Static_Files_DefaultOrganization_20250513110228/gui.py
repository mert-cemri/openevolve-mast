'''
Defines the ServerGUI class to provide a GUI for configuring the server.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from server import StaticFileServer
import threading
class ServerGUI:
    def __init__(self):
        '''
        Initializes the GUI components.
        '''
        self.root = tk.Tk()
        self.root.title("Static File Server")
        self.directory_label = tk.Label(self.root, text="Directory:")
        self.directory_label.pack()
        self.directory_entry = tk.Entry(self.root, width=50)
        self.directory_entry.pack()
        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_directory)
        self.browse_button.pack()
        self.port_label = tk.Label(self.root, text="Port:")
        self.port_label.pack()
        self.port_entry = tk.Entry(self.root, width=10)
        self.port_entry.pack()
        self.start_button = tk.Button(self.root, text="Start Server", command=self.start_server)
        self.start_button.pack()
    def browse_directory(self):
        '''
        Opens a dialog to select a directory.
        '''
        directory = filedialog.askdirectory()
        if directory:
            self.directory_entry.delete(0, tk.END)
            self.directory_entry.insert(0, directory)
    def start_server(self):
        '''
        Retrieves user input and starts the server.
        '''
        directory = self.directory_entry.get()
        port = self.port_entry.get()
        if not directory or not port:
            messagebox.showerror("Error", "Please specify both directory and port.")
            return
        try:
            port = int(port)
        except ValueError:
            messagebox.showerror("Error", "Port must be an integer.")
            return
        server = StaticFileServer(directory, port)
        threading.Thread(target=server.start, daemon=True).start()
        messagebox.showinfo("Info", f"Server started on port {port}")
    def run(self):
        '''
        Runs the GUI main loop.
        '''
        self.root.mainloop()