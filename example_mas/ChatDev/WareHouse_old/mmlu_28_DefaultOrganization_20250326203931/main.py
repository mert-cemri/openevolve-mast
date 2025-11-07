'''
This file contains the main application logic and GUI setup for the legal question-answering application.
'''
import tkinter as tk
from legal_reasoning import LegalReasoning
import os
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Legal Question Answering")
        self.create_widgets()
    def create_widgets(self):
        # Question input
        self.question_label = tk.Label(self.root, text="Enter the question:")
        self.question_label.pack()
        self.question_text = tk.Text(self.root, height=10, width=50)
        self.question_text.pack()
        # Answer options input
        self.options_label = tk.Label(self.root, text="Enter the options (separated by new lines):")
        self.options_label.pack()
        self.options_text = tk.Text(self.root, height=10, width=50)
        self.options_text.pack()
        # Submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_question)
        self.submit_button.pack()
        # Answer display
        self.answer_label = tk.Label(self.root, text="")
        self.answer_label.pack()
    def submit_question(self):
        question = self.question_text.get("1.0", tk.END).strip()
        options = self.options_text.get("1.0", tk.END).strip().split("\n")
        legal_reasoning = LegalReasoning(question, options)
        answer_index = legal_reasoning.determine_answer()
        self.answer_label.config(text=f"The answer is ({answer_index})")
if __name__ == "__main__":
    # Check if the script is running in a headless environment
    if not os.environ.get("DISPLAY"):
        # Use a virtual display for headless environments
        try:
            from pyvirtualdisplay import Display
            display = Display(visible=0, size=(1024, 768))
            display.start()
        except ImportError:
            print("pyvirtualdisplay is not installed. Please install it to run in headless mode.")
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()