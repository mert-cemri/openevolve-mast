'''
This is the main file for the high school geography quiz application. It uses tkinter to create a GUI for users to answer a multiple-choice question.
'''
import tkinter as tk
from tkinter import messagebox
class Question:
    def __init__(self, text, options, correct_index):
        '''
        Initialize the Question with text, options, and the index of the correct answer.
        '''
        self.text = text
        self.options = options
        self.correct_index = correct_index
    def get_correct_answer(self):
        '''
        Return the index of the correct answer.
        '''
        return self.correct_index
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application with the root window.
        '''
        self.root = root
        self.root.title("High School Geography Quiz")
        # Define the question
        self.question = Question(
            "China and Vietnam's dispute over the Spratley Islands is",
            [
                "a positional dispute.",
                "a territorial dispute.",
                "a resource dispute.",
                "a functional dispute."
            ],
            1  # Correct answer index
        )
        self.selected_option = tk.IntVar()
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the widgets on the window.
        '''
        # Question label
        question_label = tk.Label(self.root, text=self.question.text)
        question_label.pack(pady=10)
        # Radio buttons for options
        for idx, option in enumerate(self.question.options):
            radio_button = tk.Radiobutton(
                self.root,
                text=option,
                variable=self.selected_option,
                value=idx
            )
            radio_button.pack(anchor='w')
        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check if the selected answer is correct and display the result.
        '''
        selected_index = self.selected_option.get()
        correct_index = self.question.get_correct_answer()
        if selected_index == correct_index:
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", "Incorrect. Try again.")
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()
    except tk.TclError:
        print("Error: Unable to open a GUI window. Please ensure you have a display environment.")