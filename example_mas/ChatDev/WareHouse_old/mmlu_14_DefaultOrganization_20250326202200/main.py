'''
This is the main file for the nutrition quiz application. It uses tkinter to create a GUI for displaying a multiple-choice question about nutrition.
'''
import tkinter as tk
from tkinter import messagebox
class Question:
    '''
    A class to represent a multiple-choice question.
    '''
    def __init__(self, question_text, options, correct_index):
        self.question_text = question_text
        self.options = options
        self.correct_index = correct_index
class MainApp:
    '''
    The main application class for the nutrition quiz.
    '''
    def __init__(self, root):
        self.root = root
        self.root.title("Nutrition Quiz")
        # Create a Question instance
        self.question = Question(
            "Which of these factors increases the risk for postmenopausal breast cancer?",
            ["Red meat", "Dietary fat", "Fish", "Obesity"],
            3
        )
        # Display the question
        self.display_question()
    def display_question(self):
        '''
        Display the question and answer options in the GUI.
        '''
        question_label = tk.Label(self.root, text=self.question.question_text, wraplength=400)
        question_label.pack(pady=10)
        self.var = tk.IntVar()
        self.var.set(-1)  # No option selected initially
        for idx, option in enumerate(self.question.options):
            rb = tk.Radiobutton(self.root, text=option, variable=self.var, value=idx)
            rb.pack(anchor='w')
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check the selected answer and display the result.
        '''
        selected_index = self.var.get()
        if selected_index == -1:
            messagebox.showwarning("Selection Error", "Please select an answer.")
        elif selected_index == self.question.correct_index:
            messagebox.showinfo("Result", "Correct! The answer is Obesity.")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is Obesity.")
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()
    except tk.TclError:
        print("Error: Tkinter requires a display environment. Please run this script on a machine with a graphical interface or use a virtual display.")