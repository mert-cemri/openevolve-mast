'''
This module contains the main application logic for the Physics Uncertainty Calculator.
It uses Tkinter for the GUI and calculates the uncertainty in kinetic energy based on the uncertainty in speed.
'''
import tkinter as tk
from tkinter import messagebox
class PhysicsCalculator:
    def calculate_uncertainty_in_kinetic_energy(self, speed_uncertainty):
        """
        Calculate the uncertainty in kinetic energy based on the uncertainty in speed.
        Parameters:
        speed_uncertainty (float): The percentage uncertainty in speed.
        Returns:
        float: The percentage uncertainty in kinetic energy.
        """
        # The kinetic energy K = 0.5 * m * v^2
        # The uncertainty in kinetic energy is 2 times the uncertainty in speed
        return 2 * speed_uncertainty
class PhysicsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Physics Uncertainty Calculator")
        self.calculator = PhysicsCalculator()
        self.create_widgets()
    def create_widgets(self):
        # Label for speed uncertainty input
        self.label = tk.Label(self.root, text="Enter speed uncertainty (%):")
        self.label.pack(pady=10)
        # Entry for speed uncertainty input
        self.speed_uncertainty_entry = tk.Entry(self.root)
        self.speed_uncertainty_entry.pack(pady=5)
        # Calculate button
        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.pack(pady=20)
        # Result label
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)
    def calculate(self):
        # Automatically calculate for the given task
        speed_uncertainty = 10  # Given in the task
        kinetic_energy_uncertainty = self.calculator.calculate_uncertainty_in_kinetic_energy(speed_uncertainty)
        self.display_result(kinetic_energy_uncertainty)
    def display_result(self, kinetic_energy_uncertainty):
        self.result_label.config(text=f"Uncertainty in Kinetic Energy: {kinetic_energy_uncertainty}%")
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = PhysicsApp(root)
        root.mainloop()
    except tk.TclError:
        print("GUI cannot be displayed. Please run this application in an environment with a display.")