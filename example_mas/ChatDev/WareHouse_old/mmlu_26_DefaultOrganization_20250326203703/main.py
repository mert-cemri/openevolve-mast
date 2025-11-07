'''
Main application file for the legal question evaluator.
'''
import tkinter as tk
from tkinter import messagebox
from legal_evaluator import LegalEvaluator
class MainApp:
    def __init__(self, master):
        '''
        Initialize the main application window.
        :param master: The root window.
        '''
        self.master = master
        self.master.title("Legal Question Evaluator")
        self.label = tk.Label(master, text="Enter your legal question:")
        self.label.pack(pady=10)
        self.text_entry = tk.Entry(master, width=100)
        self.text_entry.pack(pady=10)
        self.evaluate_button = tk.Button(master, text="Evaluate", command=self.evaluate_question)
        self.evaluate_button.pack(pady=10)
        self.result_label = tk.Label(master, text="", fg="blue")
        self.result_label.pack(pady=10)
        self.legal_evaluator = LegalEvaluator()
    def evaluate_question(self):
        '''
        Evaluate the input question and display the answer or a message.
        '''
        question = self.text_entry.get()
        if question:
            answer = self.legal_evaluator.evaluate(question)
            if isinstance(answer, int):
                self.result_label.config(text=f"The answer is ({answer})")
            else:
                messagebox.showinfo("Information", answer)
        else:
            messagebox.showwarning("Input Error", "Please enter a legal question.")
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()
    except tk.TclError:
        print("Error: This application requires a graphical display environment.")