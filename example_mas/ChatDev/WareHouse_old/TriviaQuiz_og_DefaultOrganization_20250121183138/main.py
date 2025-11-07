'''
Main entry point for the Trivia Quiz application. Initializes the GUI and starts the quiz.
'''
import tkinter as tk
from quiz_manager import QuizManager
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Trivia Quiz")
        self.quiz_manager = QuizManager()
        self.current_question_index = 0
        self.score = 0
        self.question_label = tk.Label(root, text="", wraplength=400)
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
        self.display_question()
    def display_question(self):
        question = self.quiz_manager.get_current_question()
        self.question_label.config(text=question.text)
        self.answer_var.set("")
        self.result_label.config(text="")
    def submit_answer(self):
        user_answer = self.answer_var.get()
        if not user_answer.strip():
            self.result_label.config(text="Please enter an answer.", fg="orange")
            return
        if self.quiz_manager.check_answer(user_answer):
            self.score += 1
            self.result_label.config(text="Correct!", fg="green")
        else:
            correct_answer = self.quiz_manager.get_current_question().correct_answer
            self.result_label.config(text=f"Incorrect! The correct answer is: {correct_answer}", fg="red")
    def next_question(self):
        if self.quiz_manager.next_question():
            self.display_question()
        else:
            self.question_label.config(text=f"Quiz finished! Your score: {self.score}/{self.quiz_manager.total_questions()}")
            self.answer_entry.pack_forget()
            self.submit_button.pack_forget()
            self.next_button.pack_forget()
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = QuizApp(root)
        root.mainloop()
    except tk.TclError as e:
        print("Error: Unable to start the GUI. Please ensure you have a display environment available.")
        print(e)