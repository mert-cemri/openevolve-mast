'''
This is the main file for the high school macroeconomics quiz application. It uses Tkinter to create a GUI for displaying questions and checking answers.
'''
import tkinter as tk
from tkinter import messagebox
import os
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
            ["The capital account", "The official reserves account", "The current account", "The trade deficit account"],
            0
        )
        # Create GUI components
        self.question_label = tk.Label(root, text=self.question.text, wraplength=400)
        self.question_label.pack(pady=20)
        self.var = tk.IntVar()
        self.var.set(-1)  # No selection initially
        self.radio_buttons = []
        for idx, option in enumerate(self.question.options):
            rb = tk.Radiobutton(root, text=option, variable=self.var, value=idx)
            rb.pack(anchor='w')
            self.radio_buttons.append(rb)
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)
    def check_answer(self):
        selected_index = self.var.get()
        if selected_index == -1:
            messagebox.showwarning("Selection Error", "Please select an option.")
        elif selected_index == self.question.correct_index:
            messagebox.showinfo("Result", "Correct! The answer is (0).")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is (0).")
if __name__ == "__main__":
    # Check if running in a headless environment
    if os.environ.get('DISPLAY', '') == '':
        print("No display found. Please run this script in an environment with a graphical display.")
    else:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()