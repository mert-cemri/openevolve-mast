'''
Main application entry point. Initializes and runs the application.
'''
import tkinter as tk
from dashboard import Dashboard
import os
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard Application")
        self.dashboard = Dashboard(self.root)
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    # Check if running in a headless environment
    if os.environ.get('DISPLAY', '') == '':
        print("No display found. Running in headless mode.")
    else:
        root = tk.Tk()
        app = MainApp(root)
        app.run()