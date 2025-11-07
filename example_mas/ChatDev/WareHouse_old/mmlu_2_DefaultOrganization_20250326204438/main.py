'''
This file contains the main application logic for the business ethics quiz application. It uses tkinter to create a GUI that presents a multiple-choice question to the user.
'''
import tkinter as tk
from tkinter import messagebox
import os
class Question:
    def __init__(self, question_text, options, correct_index):
        '''
        Initializes a Question instance.
        :param question_text: The text of the question.
        :param options: A list of possible answers.
        :param correct_index: The index of the correct answer in the options list.
        '''
        self.question_text = question_text
        self.options = options
        self.correct_index = correct_index
class MainApp:
    def __init__(self, root):
        '''
        Initializes the main application with the given root window.
        :param root: The root window for the tkinter application.
        '''
        self.root = root
        self.root.title("Business Ethics Quiz")
        # Define the question
        self.question = Question(
            "_______ theory can be described as a code of conduct to which all rational beings should adhere. This contrasts with ________ morality which is the code of conduct adopted by a particular group or society.",
            ["Descriptive, Normative", "Normative, Instrumental", "Normative, Descriptive", "Ethical, Descriptive"],
            2
        )
        self.selected_option = tk.IntVar()
        self.create_widgets()
    def create_widgets(self):
        '''
        Creates the GUI components for the application.
        '''
        question_label = tk.Label(self.root, text=self.question.question_text, wraplength=400, justify="left")
        question_label.pack(pady=10)
        for idx, option in enumerate(self.question.options):
            radio_button = tk.Radiobutton(self.root, text=option, variable=self.selected_option, value=idx)
            radio_button.pack(anchor="w")
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Checks if the selected answer is correct and displays a message box with the result.
        '''
        selected_index = self.selected_option.get()
        if selected_index == self.question.correct_index:
            messagebox.showinfo("Result", "Correct! The answer is (2).")
        else:
            messagebox.showerror("Result", f"Incorrect. The correct answer is (2).")
if __name__ == "__main__":
    # Check if running in a headless environment
    if os.environ.get('DISPLAY', '') == '':
        print("No display found. Please run this application in an environment with a graphical interface.")
    else:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()