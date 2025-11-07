'''
Main application file for the conceptual physics multiple-choice question GUI.
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
        self.root.title("Conceptual Physics Quiz")
        self.question = "The surface of Planet Earth loses energy to outer space due mostly to"
        self.options = [
            "conduction.",
            "convection.",
            "radiation.",
            "radioactivity."
        ]
        self.correct_answer_index = 2
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the widgets in the application window.
        '''
        # Question Label
        question_label = tk.Label(self.root, text=self.question, wraplength=400, justify="left")
        question_label.pack(pady=10)
        # Variable to store the selected answer
        self.selected_answer = tk.IntVar()
        self.selected_answer.set(-1)  # No selection initially
        # Radio buttons for options
        for idx, option in enumerate(self.options):
            radio_button = tk.Radiobutton(self.root, text=option, variable=self.selected_answer, value=idx)
            radio_button.pack(anchor="w")
        # Submit Button
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
            messagebox.showinfo("Result", "Correct! The answer is (2) radiation.")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is (2) radiation.")
def run_app():
    '''
    Create an instance of the MainApp class and start the application.
    '''
    # Check for display environment
    if not os.environ.get('DISPLAY'):
        os.environ['DISPLAY'] = ':99'  # Use a virtual display
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
if __name__ == "__main__":
    run_app()