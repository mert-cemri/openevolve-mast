'''
Main application file for the econometrics multiple choice question GUI.
'''
import tkinter as tk
from tkinter import messagebox
class Question:
    '''
    Class representing a multiple choice question.
    '''
    def __init__(self, text, options, correct_index):
        self.text = text
        self.options = options
        self.correct_index = correct_index
class MainApp:
    '''
    Main application class for the Econometrics Quiz.
    '''
    def __init__(self, root):
        self.root = root
        self.root.title("Econometrics Quiz")
        # Load the question
        self.question = Question(
            "What are the dimensions of \\(\\hat{u}^t \\hat{u}\\)?",
            ["T x k", "T x 1", "k x 1", "1 x 1"],
            3
        )
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and layout the widgets for the quiz.
        '''
        # Question label
        self.question_label = tk.Label(self.root, text=self.question.text, wraplength=400)
        self.question_label.pack(pady=10)
        # Variable to store the selected answer index
        self.selected_answer = tk.IntVar()
        # Radio buttons for each option
        for idx, option in enumerate(self.question.options):
            rb = tk.Radiobutton(self.root, text=option, variable=self.selected_answer, value=idx)
            rb.pack(anchor='w')
        # Submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check the selected answer and display the result.
        '''
        selected_index = self.selected_answer.get()
        if selected_index == self.question.correct_index:
            messagebox.showinfo("Result", "Correct! The answer is (3).")
        else:
            messagebox.showerror("Result", f"Incorrect. The correct answer is (3).")
def main():
    '''
    Main function to run the application.
    '''
    # Check if the environment is headless and handle accordingly
    try:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()
    except tk.TclError as e:
        print("Error: Unable to start the GUI. Ensure you have a display environment.")
        print("Details:", e)
if __name__ == "__main__":
    main()