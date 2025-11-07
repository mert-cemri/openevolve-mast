'''
This file contains the main application logic for the moral scenarios quiz using Tkinter.
'''
import tkinter as tk
from tkinter import messagebox
import os
try:
    from pyvirtualdisplay import Display
except ImportError:
    Display = None
class Question:
    def __init__(self, text, options, correct_index):
        '''
        Initialize a Question instance.
        :param text: The question text.
        :param options: A list of answer options.
        :param correct_index: The index of the correct answer.
        '''
        self.text = text
        self.options = options
        self.correct_index = correct_index
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application window and widgets.
        :param root: The root window object.
        '''
        self.root = root
        self.root.title("Moral Scenarios Quiz")
        # Define the question
        self.question = Question(
            "For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020?\n"
            "Scenario 1 | I told my coworker I did not love her and never will love her.\n"
            "Scenario 2 | I threw the bowling ball as hard as I could to try and get a strike.",
            ["Wrong, Wrong", "Wrong, Not wrong", "Not wrong, Wrong", "Not wrong, Not wrong"],
            3
        )
        self.selected_option = tk.IntVar()
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the widgets in the main window.
        '''
        # Question label
        question_label = tk.Label(self.root, text=self.question.text, wraplength=400, justify="left")
        question_label.pack(pady=10)
        # Radio buttons for options
        for idx, option in enumerate(self.question.options):
            radio_button = tk.Radiobutton(self.root, text=option, variable=self.selected_option, value=idx)
            radio_button.pack(anchor="w")
        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=10)
    def check_answer(self):
        '''
        Check the selected answer and display the result.
        '''
        selected_index = self.selected_option.get()
        if selected_index == self.question.correct_index:
            messagebox.showinfo("Result", "Correct! The answer is (3).")
        else:
            messagebox.showerror("Result", f"Incorrect. The correct answer is (3).")
if __name__ == "__main__":
    # Check if running in a headless environment and set up a virtual display if necessary
    if os.environ.get('DISPLAY', '') == '' and Display is not None:
        print('No display found. Using Xvfb for virtual display.')
        try:
            display = Display(visible=0, size=(800, 600))
            display.start()
        except FileNotFoundError:
            print("Xvfb is not installed. Please install it using your package manager, e.g., 'sudo apt-get install xvfb'.")
    elif Display is None:
        print("pyvirtualdisplay is not installed. Please install it using 'pip install pyvirtualdisplay'.")
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()