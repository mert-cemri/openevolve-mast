'''
This module contains the main application logic for a GUI-based multiple-choice question solver using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
class MainApp:
    def __init__(self, root):
        '''
        Initializes the main application window and sets up the GUI components.
        Parameters:
        root (Tk): The root window of the tkinter application.
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
        self.correct_answer_index = 1
        # GUI components
        self.display_question()
    def display_question(self):
        '''
        Displays the question and options on the GUI.
        '''
        question_label = tk.Label(self.root, text=self.question, wraplength=400, justify="left")
        question_label.pack(pady=10)
        self.var = tk.IntVar()
        for idx, option in enumerate(self.options):
            radio_button = tk.Radiobutton(self.root, text=option, variable=self.var, value=idx, wraplength=400, justify="left")
            radio_button.pack(anchor="w")
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Checks the selected answer and displays the correct answer.
        '''
        selected_index = self.var.get()
        if selected_index == self.correct_answer_index:
            messagebox.showinfo("Result", f"Correct! The answer is ({self.correct_answer_index})")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is ({self.correct_answer_index})")
def run_app():
    '''
    Instantiates and runs the MainApp.
    '''
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
if __name__ == "__main__":
    # Check if the environment supports GUI
    try:
        run_app()
    except tk.TclError:
        print("Error: No display environment available. Please run this application in a GUI-supported environment.")