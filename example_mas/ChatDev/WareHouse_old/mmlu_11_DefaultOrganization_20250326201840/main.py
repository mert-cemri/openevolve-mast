'''
Main application file for the legal question analyzer with GUI.
'''
import tkinter as tk
from tkinter import messagebox
from analyzer import QuestionAnalyzer
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Legal Question Analyzer")
        self.question_label = tk.Label(root, text="Enter the legal question:")
        self.question_label.pack()
        self.question_text = tk.Text(root, height=10, width=50)
        self.question_text.pack()
        self.analyze_button = tk.Button(root, text="Analyze", command=self.analyze_question)
        self.analyze_button.pack()
        self.answer_label = tk.Label(root, text="", fg="blue")
        self.answer_label.pack()
    def analyze_question(self):
        question = self.question_text.get("1.0", tk.END).strip()
        if not question:
            messagebox.showwarning("Input Error", "Please enter a legal question.")
            return
        # Example answers for demonstration purposes
        possible_answers = [
            "lose, because the daughter did not have good and marketable title at the time she purported to convey the 100-acre tract to the buyer.",
            "lose, because the doctrine of after-acquired title controls.",
            "win, because the deed from the farmer to the buyer was a quitclaim deed.",
            "win, because the quitclaim deed from the farmer to the buyer was subsequent to the deed from the daughter to the buyer and to the mortgage."
        ]
        analyzer = QuestionAnalyzer(question, possible_answers)
        answer_index = analyzer.determine_answer()
        self.display_answer(answer_index)
    def display_answer(self, answer_index):
        self.answer_label.config(text=f"The answer is ({answer_index})")
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()
    except tk.TclError as e:
        print("Error: Unable to start the GUI. This environment may not support graphical interfaces.")
        print(e)