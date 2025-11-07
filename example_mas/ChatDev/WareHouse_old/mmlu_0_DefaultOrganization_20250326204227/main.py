'''
Main application file for the professional accounting question-answering software.
'''
import tkinter as tk
from question_processor import QuestionProcessor
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Accounting Q&A")
        self.create_widgets()
    def create_widgets(self):
        # Create and place widgets
        self.question_label = tk.Label(self.root, text="Enter your question:")
        self.question_label.pack()
        self.question_entry = tk.Entry(self.root, width=100)
        self.question_entry.pack()
        self.answer_button = tk.Button(self.root, text="Get Answer", command=self.calculate_answer)
        self.answer_button.pack()
        self.answer_label = tk.Label(self.root, text="")
        self.answer_label.pack()
    def calculate_answer(self):
        question_text = self.question_entry.get()
        processor = QuestionProcessor(question_text)
        answer_index = processor.process_question()
        self.answer_label.config(text=f"The answer is ({answer_index})")
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()
    except tk.TclError:
        print("GUI environment not available. Please run this script on a system with a graphical interface.")