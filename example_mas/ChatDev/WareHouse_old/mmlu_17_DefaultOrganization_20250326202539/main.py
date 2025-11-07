'''
This module contains the main application code for a multiple-choice question GUI using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
class Question:
    def __init__(self, text, options, correct_index):
        '''
        Initialize a question with text, options, and the correct answer index.
        '''
        self.text = text
        self.options = options
        self.correct_index = correct_index
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application window and set up the GUI components.
        '''
        self.root = root
        self.root.title("Multiple Choice Quiz")
        # Define the question
        self.question = Question(
            "The key attribute in successful marathon running is:",
            ["strength", "power", "stride length", "stamina"],
            3
        )
        # Create GUI components
        self.question_label = tk.Label(root, text=self.question.text)
        self.question_label.pack(pady=10)
        self.var = tk.IntVar()
        self.var.set(-1)  # No option selected initially
        self.radio_buttons = []
        for idx, option in enumerate(self.question.options):
            rb = tk.Radiobutton(root, text=option, variable=self.var, value=idx)
            rb.pack(anchor='w')
            self.radio_buttons.append(rb)
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check if the selected answer is correct and display the result.
        '''
        selected_index = self.var.get()
        if selected_index == -1:
            messagebox.showwarning("Warning", "Please select an answer.")
        elif selected_index == self.question.correct_index:
            messagebox.showinfo("Result", "Correct! The answer is (3).")
        else:
            messagebox.showinfo("Result", f"Incorrect. The answer is (3).")
if __name__ == "__main__":
    import os
    # Check if running in a headless environment
    if not os.environ.get('DISPLAY'):
        print("Warning: No display found. Running in headless mode.")
    else:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()