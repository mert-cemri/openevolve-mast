'''
This module contains the main application logic for a GUI-based multiple-choice question app using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application window and set up the GUI components.
        '''
        self.root = root
        self.root.title("Moral Disputes Quiz")
        self.question = "Kant's humanity formulation of the categorical imperative makes it impermissible for us to, he argues,"
        self.options = [
            "sell one of our teeth.",
            "engage in prostitution.",
            "both A and B",
            "Neither A nor B"
        ]
        self.correct_answer_index = 1  # The correct answer is "engage in prostitution."
        self.selected_answer = tk.IntVar()
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the widgets (labels, buttons, etc.) in the window.
        '''
        question_label = tk.Label(self.root, text=self.question, wraplength=400, justify="left")
        question_label.pack(pady=10)
        for idx, option in enumerate(self.options):
            radio_btn = tk.Radiobutton(self.root, text=option, variable=self.selected_answer, value=idx)
            radio_btn.pack(anchor="w")
        submit_btn = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_btn.pack(pady=20)
    def check_answer(self):
        '''
        Check the selected answer against the correct answer and display the result.
        '''
        selected_index = self.selected_answer.get()
        if selected_index == self.correct_answer_index:
            messagebox.showinfo("Result", "Correct! The answer is (1).")
        else:
            messagebox.showerror("Result", f"Incorrect. The correct answer is (1).")
def run_app():
    '''
    Instantiate the MainApp class and start the application.
    '''
    try:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()
    except tk.TclError:
        print("Error: No display environment found. Please ensure you are running this on a system with a graphical interface or use a virtual display server like Xvfb.")
if __name__ == "__main__":
    run_app()