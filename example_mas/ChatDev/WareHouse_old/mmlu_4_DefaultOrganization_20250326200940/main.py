'''
Main application file for the high school microeconomics multiple-choice question solver.
'''
import tkinter as tk
from tkinter import messagebox
import os
class Question:
    def __init__(self, question_text, options, correct_index):
        '''
        Initializes a Question instance with the question text, options, and the index of the correct answer.
        '''
        self.question_text = question_text
        self.options = options
        self.correct_index = correct_index
class MainApp:
    def __init__(self, root):
        '''
        Initializes the main application with the root window, sets up the question, and creates GUI components.
        '''
        self.root = root
        self.root.title("Microeconomics Quiz")
        # Define the question
        self.question = Question(
            "Patents, control of resources, economies of scale, and exclusive licenses are",
            [
                "all requirements for price discrimination",
                "required in order for a firm to earn short-run profits",
                "all sources of elastic demand",
                "all barriers to entry"
            ],
            3
        )
        # Create GUI components
        self.question_label = tk.Label(root, text=self.question.question_text, wraplength=400)
        self.question_label.pack(pady=20)
        self.var = tk.IntVar()
        self.var.set(-1)  # No selection initially
        self.option_buttons = []
        for index, option in enumerate(self.question.options):
            rb = tk.Radiobutton(root, text=option, variable=self.var, value=index)
            rb.pack(anchor='w')
            self.option_buttons.append(rb)
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Checks the selected answer against the correct answer and displays a message box with the result.
        '''
        selected_index = self.var.get()
        if selected_index == -1:
            messagebox.showwarning("No Selection", "Please select an answer before submitting.")
        elif selected_index == self.question.correct_index:
            messagebox.showinfo("Correct", "The answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"The answer is incorrect. The correct answer is option {self.question.correct_index}.")
if __name__ == "__main__":
    # Check if running in a non-GUI environment and set up a virtual display if necessary
    if os.environ.get('DISPLAY', '') == '':
        print('No display found. Using a virtual display.')
        os.environ['DISPLAY'] = ':0'
        try:
            from pyvirtualdisplay import Display
            display = Display(visible=0, size=(800, 600))
            display.start()
        except ImportError:
            print("pyvirtualdisplay is not installed. Please install it to run this application in a headless environment.")
        except FileNotFoundError:
            print("Xvfb is not installed. Please install it to run this application in a headless environment.")
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()