'''
This file contains the main application code for the professional law multiple-choice question GUI.
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
        self.root.title("Professional Law Quiz")
        # Define the question
        self.question = Question(
            "The authorities arrested a man without a warrant and held him imprisoned for 14 days without a determination of probable cause. "
            "He finally saw a public defender who filed a motion to dismiss alleging an unconstitutional detention in violation of due process. "
            "The prosecution countered that the state's rules allowed for detention without a probable cause hearing for up to 30 days, and that the procedure was constitutional. "
            "Will the court most likely decide that this detention is unconstitutional?",
            [
                "No, because the Supreme Court has ruled that detentions can properly last up to 30 days without a probable cause determination.",
                "No, because each case must be decided on its own facts and there may be many good reasons why the state has not yet provided a probable cause determination.",
                "Yes, because when the state arrests someone without a warrant it must provide a prompt probable cause determination.",
                "No, because it is constitutional to hold someone for up to 15 days without a probable cause determination."
            ],
            2
        )
        self.selected_answer = tk.IntVar()
        self.create_widgets()
    def create_widgets(self):
        # Display the question
        question_label = tk.Label(self.root, text=self.question.text, wraplength=500, justify="left")
        question_label.pack(pady=10)
        # Display the answer options
        for idx, option in enumerate(self.question.options):
            radio_button = tk.Radiobutton(self.root, text=option, variable=self.selected_answer, value=idx, wraplength=500, justify="left")
            radio_button.pack(anchor="w", padx=20)
        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.evaluate_answer)
        submit_button.pack(pady=20)
    def evaluate_answer(self):
        selected_index = self.selected_answer.get()
        if selected_index == self.question.correct_index:
            messagebox.showinfo("Result", "Correct! The answer is (2).")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is (2).")
if __name__ == "__main__":
    # Check if running in a headless environment
    if not os.environ.get('DISPLAY'):
        # Ensure Xvfb is installed and started before running this script
        print("Please ensure Xvfb is installed and running. Use 'sudo apt-get install xvfb' to install.")
    else:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()