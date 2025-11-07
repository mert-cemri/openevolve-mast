'''
This file contains the MainApp class which sets up the GUI for the multiple-choice question application.
'''
import tkinter as tk
from tkinter import messagebox
from question import Question
import os
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Law Quiz")
        # Initialize question
        self.question = Question(
            "The authorities arrested a man without a warrant and held him imprisoned for 14 days without a determination of probable cause. He finally saw a public defender who filed a motion to dismiss alleging an unconstitutional detention in violation of due process. The prosecution countered that the state's rules allowed for detention without a probable cause hearing for up to 30 days, and that the procedure was constitutional. Will the court most likely decide that this detention is unconstitutional?",
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
        # Display question
        question_label = tk.Label(self.root, text=self.question.text, wraplength=400, justify="left")
        question_label.pack(pady=10)
        # Display answer options
        for idx, option in enumerate(self.question.options):
            radio_button = tk.Radiobutton(self.root, text=option, variable=self.selected_answer, value=idx)
            radio_button.pack(anchor="w")
        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        selected_index = self.selected_answer.get()
        correct_index = self.question.get_correct_answer()
        if selected_index == correct_index:
            messagebox.showinfo("Result", "Correct! The answer is (2).")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is (2).")
if __name__ == "__main__":
    # Check if DISPLAY environment variable is set
    if os.environ.get('DISPLAY', '') == '':
        print("No display found. Please ensure you are running this on a system with a graphical interface.")
    else:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()