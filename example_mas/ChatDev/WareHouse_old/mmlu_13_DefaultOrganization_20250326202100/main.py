'''
This file contains the MainApp class which creates the GUI for the physics uncertainty calculator.
'''
import tkinter as tk
from tkinter import messagebox
from physics_calculator import PhysicsCalculator
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Physics Uncertainty Calculator")
        # Label for speed uncertainty input
        self.label = tk.Label(root, text="Enter speed uncertainty (%):")
        self.label.pack(pady=10)
        # Entry for speed uncertainty input
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        # Button to calculate uncertainty
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate_uncertainty)
        self.calculate_button.pack(pady=20)
        # Label to display result
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
    def calculate_uncertainty(self):
        try:
            speed_uncertainty = float(self.entry.get())
            if speed_uncertainty < 0:
                raise ValueError("Uncertainty cannot be negative.")
            # Calculate kinetic energy uncertainty
            kinetic_energy_uncertainty = PhysicsCalculator.calculate_kinetic_energy_uncertainty(speed_uncertainty)
            self.result_label.config(text=f"Kinetic Energy Uncertainty: {kinetic_energy_uncertainty}%")
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()
    except tk.TclError:
        print("Error: Tkinter requires a display. Please run this script in an environment with a graphical display.")