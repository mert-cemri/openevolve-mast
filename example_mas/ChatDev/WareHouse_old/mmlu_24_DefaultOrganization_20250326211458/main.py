'''
This module contains the main application code for a GUI-based multiple-choice question about moral scenarios.
'''
import tkinter as tk
from tkinter import messagebox
import os
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application window and its components.
        Parameters:
        root (tk.Tk): The root window of the application.
        '''
        self.root = root
        self.root.title("Moral Scenarios Quiz")
        # Question and options
        self.question = "For which of these two scenarios does the main character do something clearly morally wrong, according to ordinary moral standards in the US as of 2020?"
        self.scenarios = [
            "Scenario 1 | I refilled the shampoo bottle with shaving cream and put it back in the shower.",
            "Scenario 2 | I kept a distance from an ambulance."
        ]
        self.options = [
            "0. Wrong, Wrong",
            "1. Wrong, Not wrong",
            "2. Not wrong, Wrong",
            "3. Not wrong, Not wrong"
        ]
        self.correct_answer = 1  # The correct index based on the moral evaluation
        # Variable to store the user's choice
        self.user_choice = tk.IntVar()
        # Create the GUI components
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and layout the widgets in the application.
        '''
        # Display the question
        question_label = tk.Label(self.root, text=self.question, wraplength=400, justify="left")
        question_label.pack(pady=10)
        # Display the scenarios
        for scenario in self.scenarios:
            scenario_label = tk.Label(self.root, text=scenario, wraplength=400, justify="left")
            scenario_label.pack(anchor="w", padx=20)
        # Display the options as radio buttons
        for index, option in enumerate(self.options):
            radio_button = tk.Radiobutton(self.root, text=option, variable=self.user_choice, value=index)
            radio_button.pack(anchor="w", padx=20)
        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check if the selected answer is correct and display the result.
        '''
        selected_answer = self.user_choice.get()
        if selected_answer == self.correct_answer:
            self.display_result("Correct! The answer is (1).")
        else:
            self.display_result(f"Incorrect. The correct answer is (1).")
    def display_result(self, result):
        '''
        Display the result of the user's selection.
        Parameters:
        result (str): The result message to display.
        '''
        messagebox.showinfo("Result", result)
if __name__ == "__main__":
    # Check if the DISPLAY environment variable is set, if not, set it for virtual display
    if not os.environ.get('DISPLAY'):
        os.environ['DISPLAY'] = ':99'  # Use a different display number for Xvfb
    try:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()
    except tk.TclError:
        print("Error: Could not connect to display. Ensure Xvfb is running for headless environments.")