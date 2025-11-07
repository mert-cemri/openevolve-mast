'''
This module creates a GUI application using tkinter to display a multiple-choice question about computer security and allows the user to select an answer.
'''
import tkinter as tk
from tkinter import messagebox
import os
class Question:
    def __init__(self, text, options, correct_index):
        '''
        Initialize a Question instance.
        :param text: The question text.
        :param options: A list of answer options.
        :param correct_index: The index of the correct answer in the options list.
        '''
        self.text = text
        self.options = options
        self.correct_index = correct_index
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application window.
        :param root: The root window object.
        '''
        self.root = root
        self.root.title("Computer Security Quiz")
        # Define the question
        self.question = Question(
            "What is a replay attack?",
            [
                "When the attacker replies to a message sent to it by the system",
                "An attack that continuously repeats, probing for a weakness",
                "An attack that uses the system's own messages and so cannot be defended against",
                "The attacker resends a captured message, and the site accept its and responds in the attacker's favor"
            ],
            3
        )
        self.selected_answer = tk.IntVar()
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the widgets in the window.
        '''
        # Display the question
        question_label = tk.Label(self.root, text=self.question.text, wraplength=400, justify="left")
        question_label.pack(pady=10)
        # Display the answer options as radio buttons
        for idx, option in enumerate(self.question.options):
            radio_button = tk.Radiobutton(
                self.root,
                text=option,
                variable=self.selected_answer,
                value=idx
            )
            radio_button.pack(anchor="w")
        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check if the selected answer is correct and display the result.
        '''
        if self.selected_answer.get() == self.question.correct_index:
            messagebox.showinfo("Result", "Correct! The answer is (3).")
        else:
            messagebox.showerror("Result", "Incorrect. Try again.")
if __name__ == "__main__":
    # Check if DISPLAY is set, if not, set it to a default value
    if os.environ.get('DISPLAY', '') == '':
        print('no display found. Using :0.0')
        os.environ.__setitem__('DISPLAY', ':0.0')
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()