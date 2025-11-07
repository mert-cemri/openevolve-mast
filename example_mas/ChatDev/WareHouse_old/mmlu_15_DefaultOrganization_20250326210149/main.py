'''
Main application file for the machine learning quiz GUI.
'''
import tkinter as tk
from tkinter import messagebox
from question import Question
import os
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application window and its components.
        '''
        self.root = root
        self.root.title("Machine Learning Quiz")
        # Define the question
        self.question = Question(
            "Statement 1| The SVM learning algorithm is guaranteed to find the globally optimal hypothesis with respect to its object function. "
            "Statement 2| After being mapped into feature space Q through a radial basis kernel function, a Perceptron may be able to achieve better classification performance than in its original space (though we can’t guarantee this).",
            ["True, True", "False, False", "True, False", "False, True"],
            3
        )
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the GUI components.
        '''
        self.question_label = tk.Label(self.root, text=self.question.text, wraplength=400, justify="left")
        self.question_label.pack(pady=10)
        self.var = tk.IntVar()
        self.var.set(-1)  # No selection initially
        for idx, option in enumerate(self.question.options):
            tk.Radiobutton(self.root, text=option, variable=self.var, value=idx).pack(anchor="w")
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Validate the selected answer and display the correct answer.
        '''
        selected = self.var.get()
        if selected == -1:
            messagebox.showwarning("Warning", "Please select an answer.")
        elif selected == self.question.correct_answer:
            messagebox.showinfo("Result", "Correct! The answer is (3).")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is (3).")
if __name__ == "__main__":
    # Check if running in a headless environment and set up virtual display if necessary
    if not os.environ.get('DISPLAY'):
        os.environ['DISPLAY'] = ':0'
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()