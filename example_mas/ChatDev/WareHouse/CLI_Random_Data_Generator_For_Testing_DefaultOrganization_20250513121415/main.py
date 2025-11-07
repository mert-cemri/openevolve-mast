'''
Main entry point for the dashboard application. Initializes and runs the GUI.
'''
import tkinter as tk
from data_handler import DataHandler
from visualization import Visualization
class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard Application")
        self.data_handler = DataHandler()
        self.visualization = Visualization()
        self.create_widgets()
    def create_widgets(self):
        # Create and place widgets
        load_button = tk.Button(self.root, text="Load Data", command=self.load_data)
        load_button.pack(pady=10)
        self.chart_canvas = tk.Canvas(self.root, width=400, height=300)
        self.chart_canvas.pack()
    def load_data(self):
        # Load and process data
        data = self.data_handler.load_data()
        processed_data = self.data_handler.process_data(data)
        self.visualization.create_chart(self.chart_canvas, processed_data)
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = DashboardApp(root)
        app.run()
    except tk.TclError as e:
        print("Error: Unable to start the GUI. Ensure you are running in an environment with a display server.")
        print(e)