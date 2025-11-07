'''
Main application file for the high school microeconomics quiz application using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
import os
import sys
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application window and its components.
        Parameters:
        root (tk.Tk): The root window of the application.
        '''
        self.root = root
        self.root.title("High School Microeconomics Quiz")
        # Question and options
        self.question = "Patents, control of resources, economies of scale, and exclusive licenses are"
        self.options = [
            "all requirements for price discrimination",
            "required in order for a firm to earn short-run profits",
            "all sources of elastic demand",
            "all barriers to entry"
        ]
        self.correct_answer_index = 3
        # Create widgets
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the widgets on the application window.
        '''
        # Question label
        question_label = tk.Label(self.root, text=self.question, wraplength=400, justify="left")
        question_label.pack(pady=10)
        # Variable to store the selected option
        self.selected_option = tk.IntVar()
        # Radio buttons for options
        for idx, option in enumerate(self.options):
            radio_button = tk.Radiobutton(self.root, text=option, variable=self.selected_option, value=idx)
            radio_button.pack(anchor="w")
        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check the selected answer and display a message indicating whether it is correct.
        '''
        selected_index = self.selected_option.get()
        if selected_index == self.correct_answer_index:
            messagebox.showinfo("Result", "Correct! The answer is (3).")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is (3).")
def run_app():
    '''
    Instantiate and run the application.
    '''
    # Check if running in a headless environment
    if not os.environ.get('DISPLAY'):
        print("No display found. Running in headless mode.")
        sys.exit("This application requires a graphical display to run.")
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
if __name__ == "__main__":
    run_app()