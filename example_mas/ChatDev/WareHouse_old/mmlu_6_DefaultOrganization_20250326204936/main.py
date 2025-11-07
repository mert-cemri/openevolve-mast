'''
Main application file for the multiple-choice question GUI.
'''
import tkinter as tk
from tkinter import messagebox
import os
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application window and layout.
        '''
        self.root = root
        self.root.title("High School Government and Politics Quiz")
        # Question and options
        self.question = "According to The Federalist Papers, federalism has which of the following effects on political factions?"
        self.options = [
            "It provides a structured environment in which factions may flourish.",
            "It limits the dangers of factionalism by diluting political power.",
            "It allows factions to dominate on the national level while limiting their influence on state governments.",
            "It eliminates any opportunity for factions to form."
        ]
        # Correct answer index
        self.correct_answer_index = 1
        # Display the question and options
        self.display_question()
    def display_question(self):
        '''
        Display the question and options on the GUI.
        '''
        question_label = tk.Label(self.root, text=self.question, wraplength=400, justify="left")
        question_label.pack(pady=10)
        self.var = tk.IntVar()
        for idx, option in enumerate(self.options):
            rb = tk.Radiobutton(self.root, text=option, variable=self.var, value=idx, wraplength=400, justify="left")
            rb.pack(anchor="w")
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check the selected answer and display the result.
        '''
        selected_index = self.var.get()
        if selected_index == self.correct_answer_index:
            messagebox.showinfo("Result", "Correct! The answer is (1).")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is (1).")
def run_app():
    '''
    Function to run the application.
    '''
    # Check if DISPLAY environment variable is set
    if not os.environ.get('DISPLAY'):
        os.environ['DISPLAY'] = ':0'  # Set a default display if not set
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
if __name__ == "__main__":
    run_app()