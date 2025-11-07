'''
Main application file for the multiple choice question GUI.
'''
import tkinter as tk
from tkinter import messagebox
import os
class Question:
    def __init__(self, question_text, options, correct_index):
        '''
        Initialize a Question instance.
        :param question_text: The text of the question.
        :param options: A list of answer options.
        :param correct_index: The index of the correct answer in the options list.
        '''
        self.question_text = question_text
        self.options = options
        self.correct_index = correct_index
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application window.
        :param root: The root window of the Tkinter application.
        '''
        self.root = root
        self.root.title("High School Geography Quiz")
        # Example question
        self.question = Question(
            "China and Vietnam's dispute over the Spratley Islands is",
            [
                "a positional dispute.",
                "a territorial dispute.",
                "a resource dispute.",
                "a functional dispute."
            ],
            1  # Correct answer is "a territorial dispute."
        )
        self.selected_answer = tk.IntVar()
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the widgets in the application window.
        '''
        question_label = tk.Label(self.root, text=self.question.question_text)
        question_label.pack(pady=10)
        for idx, option in enumerate(self.question.options):
            radio_button = tk.Radiobutton(
                self.root,
                text=option,
                variable=self.selected_answer,
                value=idx
            )
            radio_button.pack(anchor='w')
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check if the selected answer is correct and display the result.
        '''
        selected_index = self.selected_answer.get()
        if selected_index == self.question.correct_index:
            messagebox.showinfo("Result", "Correct! The answer is (1).")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is (1).")
if __name__ == "__main__":
    # Check if the DISPLAY environment variable is set
    if os.environ.get('DISPLAY', '') == '':
        print("No display found. Please ensure you are running this on a system with a graphical display.")
    else:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()