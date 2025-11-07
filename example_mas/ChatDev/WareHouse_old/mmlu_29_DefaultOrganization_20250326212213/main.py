'''
Main application file for the moral scenarios quiz using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
import os
class Question:
    def __init__(self, text, options, correct_index):
        '''
        Initialize the question with text, options, and the index of the correct answer.
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
        self.root.title("Moral Scenarios Quiz")
        # Define the question
        self.question = Question(
            "For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020?\n"
            "Scenario 1 | I told my coworker I did not love her and never will love her.\n"
            "Scenario 2 | I threw the bowling ball as hard as I could to try and get a strike.",
            ["Wrong, Wrong", "Wrong, Not wrong", "Not wrong, Wrong", "Not wrong, Not wrong"],
            3
        )
        # Create widgets
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the widgets in the window.
        '''
        # Question label
        self.question_label = tk.Label(self.root, text=self.question.text, wraplength=400, justify="left")
        self.question_label.pack(pady=10)
        # Variable to store the selected answer
        self.selected_answer = tk.IntVar()
        self.selected_answer.set(-1)  # No selection by default
        # Radio buttons for options
        for idx, option in enumerate(self.question.options):
            rb = tk.Radiobutton(self.root, text=option, variable=self.selected_answer, value=idx)
            rb.pack(anchor="w")
        # Submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check the user's selected answer and display the correct answer.
        '''
        selected_index = self.selected_answer.get()
        if selected_index == -1:
            messagebox.showwarning("No selection", "Please select an answer.")
        elif selected_index == self.question.correct_index:
            messagebox.showinfo("Correct", "The answer is correct!")
        else:
            messagebox.showinfo("Incorrect", f"The answer is ({self.question.correct_index})")
if __name__ == "__main__":
    # Check if the DISPLAY environment variable is set
    if not os.environ.get('DISPLAY'):
        os.environ['DISPLAY'] = ':0'  # Set a default display if not set
    try:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()
    except tk.TclError as e:
        print("Error: Unable to connect to the display. Ensure a display server is running or use a virtual display.")