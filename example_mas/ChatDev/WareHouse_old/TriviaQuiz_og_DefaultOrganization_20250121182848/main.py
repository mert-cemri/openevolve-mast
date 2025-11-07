'''
Main application file for the trivia quiz program using tkinter.
'''
import tkinter as tk
from question import Question
from question_bank import QuestionBank
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Trivia Quiz")
        self.question_bank = QuestionBank()
        self.current_question_index = 0
        self.score = 0
        # GUI Elements
        self.question_label = tk.Label(root, text="", wraplength=400)
        self.question_label.pack(pady=20)
        self.options_var = tk.StringVar()
        self.options_frame = tk.Frame(root)
        self.options_frame.pack(pady=10)
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=20)
        self.start_quiz()
    def start_quiz(self):
        # Add questions to the question bank
        self.question_bank.add_question(Question("What is the capital of France?", ["Paris", "London", "Berlin", "Rome"], "Paris"))
        self.question_bank.add_question(Question("What is 2 + 2?", ["3", "4", "5", "6"], "4"))
        self.question_bank.add_question(Question("What is the largest planet in our solar system?", ["Earth", "Mars", "Jupiter", "Saturn"], "Jupiter"))
        self.next_question()
    def next_question(self):
        if self.current_question_index < len(self.question_bank.questions):
            question = self.question_bank.get_question(self.current_question_index)
            self.question_label.config(text=question.text)
            # Clear previous options
            for widget in self.options_frame.winfo_children():
                widget.destroy()
            # Display options
            for option in question.options:
                radio_button = tk.Radiobutton(self.options_frame, text=option, variable=self.options_var, value=option)
                radio_button.pack(anchor='w')
            self.options_var.set(None)
        else:
            self.show_results()
    def check_answer(self):
        selected_option = self.options_var.get()
        correct_answer = self.question_bank.get_question(self.current_question_index).answer
        if selected_option == correct_answer:
            self.score += 1
        self.current_question_index += 1
        self.next_question()
    def show_results(self):
        self.question_label.config(text=f"Quiz Completed! Your score is {self.score}/{len(self.question_bank.questions)}")
        self.options_frame.pack_forget()
        self.submit_button.pack_forget()
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()