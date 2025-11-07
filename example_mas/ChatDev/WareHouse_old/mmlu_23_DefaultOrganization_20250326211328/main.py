'''
This module contains the main application code for a GUI-based multiple-choice question app using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
import os
class Question:
    def __init__(self, text, options, correct_index):
        '''
        Initialize a question with text, options, and the index of the correct answer.
        '''
        self.text = text
        self.options = options
        self.correct_index = correct_index
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application window and its components.
        '''
        self.root = root
        self.root.title("Business Ethics Quiz")
        # Define the question
        self.question = Question(
            "What term can be used to describe 'the hypothetical agreement between member of society and those who govern it which establishes the inter-relationships, rights and responsibilities on a fair basis'?",
            ["Social Contract", "Duty Ethics", "Consequentialism", "Virtue Ethics"],
            0
        )
        self.selected_answer = tk.IntVar()
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the widgets in the window.
        '''
        # Question label
        question_label = tk.Label(self.root, text=self.question.text, wraplength=400, justify="left")
        question_label.pack(pady=10)
        # Radio buttons for options
        for idx, option in enumerate(self.question.options):
            radio_button = tk.Radiobutton(self.root, text=option, variable=self.selected_answer, value=idx)
            radio_button.pack(anchor="w")
        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check if the selected answer is correct and display the result.
        '''
        if self.selected_answer.get() == self.question.correct_index:
            messagebox.showinfo("Result", "Correct! The answer is Social Contract.")
        else:
            messagebox.showinfo("Result", "Incorrect. The correct answer is Social Contract.")
if __name__ == "__main__":
    # Check if running in a headless environment and use Xvfb if necessary
    if os.environ.get('DISPLAY', '') == '':
        print('No display found. Using Xvfb for virtual display.')
        os.system('Xvfb :99 -screen 0 1024x768x16 &')
        os.environ['DISPLAY'] = ':99.0'
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()