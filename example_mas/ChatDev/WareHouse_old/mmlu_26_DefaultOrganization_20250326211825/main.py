'''
Main application file for the legal question evaluator GUI.
'''
import tkinter as tk
from legal_evaluator import LegalEvaluator
import os
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Legal Question Evaluator")
        self.question_label = tk.Label(root, text="Enter your legal question:")
        self.question_label.pack()
        self.question_entry = tk.Entry(root, width=100)
        self.question_entry.pack()
        self.evaluate_button = tk.Button(root, text="Evaluate", command=self.evaluate_question)
        self.evaluate_button.pack()
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
        self.legal_evaluator = LegalEvaluator()
    def evaluate_question(self):
        question = self.question_entry.get()
        answer = self.legal_evaluator.evaluate(question)
        self.result_label.config(text=f"The answer is {answer}")
if __name__ == "__main__":
    # Check if running in a headless environment and set up a virtual display if necessary
    if os.environ.get('DISPLAY', '') == '':
        print('No display found. Using Xvfb for virtual display.')
        try:
            from pyvirtualdisplay import Display
            display = Display(visible=0, size=(800, 600))
            display.start()
        except FileNotFoundError:
            print("Xvfb is not installed. Please install it using 'sudo apt-get install xvfb' and try again.")
            exit(1)
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()