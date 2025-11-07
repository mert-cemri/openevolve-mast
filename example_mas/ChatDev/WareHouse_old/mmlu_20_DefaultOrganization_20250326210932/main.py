'''
Main application file for the multiple-choice question GUI.
'''
import tkinter as tk
from tkinter import messagebox
import os
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application window and its components.
        '''
        self.root = root
        self.root.title("High School Government and Politics Quiz")
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the widgets in the window.
        '''
        # Question
        question_label = tk.Label(self.root, text="People who join a political party other than the one to which their parents belong most often do so because of")
        question_label.pack(pady=10)
        # Answers
        self.answer_var = tk.IntVar()
        answers = [
            "0. peer pressure",
            "1. economic issues",
            "2. religious beliefs",
            "3. pressure from their employers"
        ]
        for idx, answer in enumerate(answers):
            radio_button = tk.Radiobutton(self.root, text=answer, variable=self.answer_var, value=idx)
            radio_button.pack(anchor='w')
        # Submit Button
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check if the selected answer is correct and display the result.
        '''
        selected_answer = self.answer_var.get()
        correct_answer = 1  # Based on the logic provided
        if selected_answer == correct_answer:
            messagebox.showinfo("Result", "Correct! The answer is (1).")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is (1).")
def run_app():
    '''
    Function to start the application.
    '''
    # Check if running in a headless environment
    if not os.environ.get('DISPLAY'):
        os.environ['DISPLAY'] = ':0'  # Set a default display if not set
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
if __name__ == "__main__":
    run_app()