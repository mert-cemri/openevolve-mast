'''
Main application file for the multiple-choice question GUI.
'''
import tkinter as tk
from tkinter import messagebox
import os
class Question:
    '''
    A class to represent a multiple-choice question.
    '''
    def __init__(self, text, options, correct_index):
        self.text = text
        self.options = options
        self.correct_index = correct_index
class MainApp:
    '''
    Main application class to create and manage the GUI.
    '''
    def __init__(self, root):
        self.root = root
        self.root.title("High School Government and Politics Quiz")
        # Define the question
        self.question = Question(
            "People who join a political party other than the one to which their parents belong most often do so because of",
            ["peer pressure", "economic issues", "religious beliefs", "pressure from their employers"],
            1
        )
        # Create widgets
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the widgets in the main window.
        '''
        # Question label
        self.question_label = tk.Label(self.root, text=self.question.text, wraplength=400, justify="left")
        self.question_label.pack(pady=10)
        # Variable to store the selected option
        self.selected_option = tk.IntVar()
        self.selected_option.set(-1)  # No option selected initially
        # Radio buttons for options
        for idx, option in enumerate(self.question.options):
            rb = tk.Radiobutton(self.root, text=option, variable=self.selected_option, value=idx)
            rb.pack(anchor="w")
        # Submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check if the selected answer is correct and display a message.
        '''
        selected_index = self.selected_option.get()
        if selected_index == -1:
            messagebox.showwarning("No selection", "Please select an answer.")
        elif selected_index == self.question.correct_index:
            messagebox.showinfo("Result", "Correct! The answer is economic issues.")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is {self.question.options[self.question.correct_index]}.")
if __name__ == "__main__":
    # Check if the DISPLAY environment variable is set
    if os.environ.get('DISPLAY', '') == '':
        print("No display environment found. Please ensure you are running this application in a graphical environment.")
    else:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()