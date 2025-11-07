'''
This file contains the main application logic for a GUI-based multiple-choice question app using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
class Question:
    def __init__(self, text, options, correct_index):
        self.text = text
        self.options = options
        self.correct_index = correct_index
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Macroeconomics Quiz")
        # Define the question
        self.question = Question(
            "Which component of a nation's balance of payments recognizes the purchase and sale of real and financial assets between nations?",
            [
                "The capital account",
                "The official reserves account",
                "The current account",
                "The trade deficit account"
            ],
            0
        )
        self.selected_answer = tk.IntVar()
        self.create_widgets()
    def create_widgets(self):
        # Create question label
        question_label = tk.Label(self.root, text=self.question.text, wraplength=400, justify="left")
        question_label.pack(pady=10)
        # Create radio buttons for each option
        for idx, option in enumerate(self.question.options):
            radio_button = tk.Radiobutton(
                self.root,
                text=option,
                variable=self.selected_answer,
                value=idx
            )
            radio_button.pack(anchor="w")
        # Create submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        selected_index = self.selected_answer.get()
        if selected_index == self.question.correct_index:
            messagebox.showinfo("Result", "Correct! The answer is (0).")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is (0).")
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()
    except tk.TclError:
        print("Error: Unable to open display. Please ensure you are running this on a system with a graphical interface or use X11 forwarding.")