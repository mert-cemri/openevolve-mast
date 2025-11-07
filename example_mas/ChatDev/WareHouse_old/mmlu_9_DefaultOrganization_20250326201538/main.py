'''
This is the main file for the conceptual physics quiz application. It uses tkinter to create a GUI
that presents a multiple-choice question to the user and checks the answer.
'''
import tkinter as tk
from tkinter import messagebox
import os
class Question:
    def __init__(self, question_text, answers, correct_index):
        '''
        Initialize a Question instance.
        :param question_text: The text of the question.
        :param answers: A list of possible answers.
        :param correct_index: The index of the correct answer in the answers list.
        '''
        self.question_text = question_text
        self.answers = answers
        self.correct_index = correct_index
class MainApp:
    def __init__(self, root, question):
        '''
        Initialize the main application window.
        :param root: The root window.
        :param question: A Question instance containing the question and answers.
        '''
        self.root = root
        self.root.title("Conceptual Physics Quiz")
        self.question = question
        self.selected_answer = tk.IntVar()
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the widgets in the application window.
        '''
        # Display the question
        question_label = tk.Label(self.root, text=self.question.question_text)
        question_label.pack(pady=10)
        # Display the answer options as radio buttons
        for idx, answer in enumerate(self.question.answers):
            radio_button = tk.Radiobutton(self.root, text=answer, variable=self.selected_answer, value=idx)
            radio_button.pack(anchor='w')
        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check if the selected answer is correct and display a message.
        '''
        if self.selected_answer.get() == self.question.correct_index:
            messagebox.showinfo("Result", "Correct! The answer is {}".format(self.selected_answer.get()))
        else:
            messagebox.showerror("Result", "Incorrect. Try again.")
if __name__ == "__main__":
    # Check if running in a headless environment
    if not os.environ.get('DISPLAY'):
        print("Error: No display found. Please run this application in an environment with a graphical interface.")
    else:
        # Define the question and answers
        question_text = "The surface of Planet Earth loses energy to outer space due mostly to"
        answers = ["conduction", "convection", "radiation", "radioactivity"]
        correct_index = 2
        # Create a Question instance
        question = Question(question_text, answers, correct_index)
        # Create the main application window
        root = tk.Tk()
        app = MainApp(root, question)
        try:
            root.mainloop()
        except tk.TclError:
            print("Error: Unable to start the GUI. Ensure you have a graphical environment available.")