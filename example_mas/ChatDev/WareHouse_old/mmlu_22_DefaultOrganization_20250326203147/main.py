'''
This module contains the main application code for displaying a multiple-choice question about philosophy and checking the user's answer.
'''
import tkinter as tk
from tkinter import messagebox
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application window and set up the GUI components.
        '''
        self.root = root
        self.root.title("Philosophy Question")
        # Question and options
        self.question = "Before his conversion, what was Tolstoy surrounded by?"
        self.options = [
            "what is considered complete happiness",
            "things that no one would want",
            "what is considered heavenly bliss",
            "what is considered deep insight"
        ]
        self.correct_answer_index = 0
        # Create GUI components
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the widgets in the main window.
        '''
        # Display the question
        question_label = tk.Label(self.root, text=self.question, wraplength=400, justify="left")
        question_label.pack(pady=10)
        # Variable to store the selected answer
        self.selected_answer = tk.IntVar()
        self.selected_answer.set(-1)  # No selection initially
        # Display the options as radio buttons
        for idx, option in enumerate(self.options):
            radio_button = tk.Radiobutton(self.root, text=option, variable=self.selected_answer, value=idx)
            radio_button.pack(anchor="w")
        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check the selected answer and display the correct answer.
        '''
        selected_index = self.selected_answer.get()
        if selected_index == -1:
            messagebox.showinfo("Selection Error", "Please select an answer.")
        elif selected_index == self.correct_answer_index:
            messagebox.showinfo("Result", "Correct! The answer is (0).")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is (0).")
def run_app():
    '''
    Create an instance of MainApp and start the main loop.
    '''
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
if __name__ == "__main__":
    run_app()