'''
Main application file for the accounting question GUI.
'''
import tkinter as tk
from tkinter import messagebox
import os
class Question:
    '''
    Class to represent the accounting question and its answers.
    '''
    def __init__(self):
        self.question_text = ("Mast Co. converted from the FIFO method for inventory valuation to the LIFO method "
                              "for financial statement and tax purposes. During a period of inflation would Mast's "
                              "ending inventory and income tax payable using LIFO be higher or lower than FIFO?")
        self.answers = [
            "Lower Lower",
            "Higher Higher",
            "Lower Higher",
            "Higher Lower"
        ]
        self.correct_answer_index = 0
    def get_correct_answer(self):
        '''
        Returns the index of the correct answer.
        '''
        return self.correct_answer_index
class MainApp:
    '''
    Main application class to create the GUI and handle user interactions.
    '''
    def __init__(self, root):
        self.root = root
        self.root.title("Accounting Question")
        self.question = Question()
        self.selected_answer = tk.IntVar()
        self.create_widgets()
    def create_widgets(self):
        '''
        Creates the widgets for the GUI.
        '''
        tk.Label(self.root, text=self.question.question_text, wraplength=400).pack(pady=10)
        for idx, answer in enumerate(self.question.answers):
            tk.Radiobutton(self.root, text=answer, variable=self.selected_answer, value=idx).pack(anchor='w')
        tk.Button(self.root, text="Submit", command=self.evaluate_answer).pack(pady=10)
    def evaluate_answer(self):
        '''
        Evaluates the selected answer and displays a message box with the result.
        '''
        selected_index = self.selected_answer.get()
        correct_index = self.question.get_correct_answer()
        if selected_index == correct_index:
            messagebox.showinfo("Result", f"Correct! The answer is ({correct_index})")
        else:
            messagebox.showerror("Result", f"Incorrect. The correct answer is ({correct_index})")
if __name__ == "__main__":
    # Check if running in a headless environment and use Xvfb if necessary
    if os.environ.get('DISPLAY', '') == '':
        print('No display found. Using Xvfb...')
        try:
            from pyvirtualdisplay import Display
            display = Display(visible=0, size=(800, 600))
            display.start()
        except ImportError:
            print("Xvfb is not installed. Please install it using 'sudo apt-get install xvfb'.")
            exit(1)
        except FileNotFoundError:
            print("Xvfb executable not found. Please ensure it is installed and accessible.")
            exit(1)
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()