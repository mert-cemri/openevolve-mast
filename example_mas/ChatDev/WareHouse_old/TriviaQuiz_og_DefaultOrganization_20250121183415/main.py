'''
Main application file for the trivia quiz program. Initializes the GUI and handles user interactions.
'''
import tkinter as tk
from quiz_manager import QuizManager
import os
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Trivia Quiz")
        self.quiz_manager = QuizManager()
        self.current_question = None
        self.score = 0
        self.question_label = tk.Label(root, text="", wraplength=400, justify="center")
        self.question_label.pack(pady=20)
        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(root, textvariable=self.answer_var)
        self.answer_entry.pack(pady=10)
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=10)
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=20)
        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)
        self.choice_buttons = []  # List to hold choice buttons for multiple-choice questions
        self.load_next_question()
    def load_next_question(self):
        self.current_question = self.quiz_manager.get_next_question()
        if self.current_question:
            self.question_label.config(text=self.current_question.text)
            self.answer_var.set("")
            self.result_label.config(text="")
            if self.current_question.choices:
                self.answer_entry.pack_forget()
                for btn in self.choice_buttons:
                    btn.pack_forget()
                self.choice_buttons = []
                for choice in self.current_question.choices:
                    btn = tk.Button(self.root, text=choice, command=lambda c=choice: self.select_choice(c))
                    btn.pack(pady=5)
                    self.choice_buttons.append(btn)
            else:
                for btn in self.choice_buttons:
                    btn.pack_forget()
                self.choice_buttons = []
                self.answer_entry.pack(pady=10)
        else:
            self.end_quiz()
    def select_choice(self, choice):
        self.answer_var.set(choice)
        self.submit_answer()
    def submit_answer(self):
        user_answer = self.answer_var.get().strip()
        if user_answer.lower() == self.current_question.correct_answer.lower():
            self.score += 1
            self.result_label.config(text="Correct!", fg="green")
        else:
            self.result_label.config(text=f"Incorrect! The correct answer was: {self.current_question.correct_answer}", fg="red")
    def next_question(self):
        self.load_next_question()
    def end_quiz(self):
        self.question_label.config(text=f"Quiz Over! Your score: {self.score}/{self.quiz_manager.total_questions()}")
        self.answer_entry.pack_forget()
        self.submit_button.pack_forget()
        self.next_button.pack_forget()
        for btn in self.choice_buttons:
            btn.pack_forget()
if __name__ == "__main__":
    # Check if the DISPLAY environment variable is set, if not, set it for headless environments
    if 'DISPLAY' not in os.environ:
        os.environ['DISPLAY'] = ':0'
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()