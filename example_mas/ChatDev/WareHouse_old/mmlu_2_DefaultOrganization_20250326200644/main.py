'''
Main application file for the business ethics multiple-choice question GUI.
'''
import tkinter as tk
from tkinter import messagebox
import os
import subprocess
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application window and setup the question and options.
        '''
        self.root = root
        self.root.title("Business Ethics Quiz")
        # Question and options
        self.question = "_______ theory can be described as a code of conduct to which all rational beings should adhere. This contrasts with ________ morality which is the code of conduct adopted by a particular group or society."
        self.options = [
            "Descriptive, Normative",
            "Normative, Instrumental",
            "Normative, Descriptive",
            "Ethical, Descriptive"
        ]
        self.correct_answer_index = 2
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the widgets (labels, buttons) in the window.
        '''
        # Question label
        question_label = tk.Label(self.root, text=self.question, wraplength=400, justify="left")
        question_label.pack(pady=10)
        # Radio buttons for options
        self.selected_option = tk.IntVar()
        self.selected_option.set(-1)  # No option selected initially
        for idx, option in enumerate(self.options):
            rb = tk.Radiobutton(self.root, text=option, variable=self.selected_option, value=idx)
            rb.pack(anchor="w")
        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check if the selected answer is correct and display the result.
        '''
        selected_index = self.selected_option.get()
        if selected_index == -1:
            messagebox.showinfo("Selection Error", "Please select an option.")
        elif selected_index == self.correct_answer_index:
            messagebox.showinfo("Result", "Correct! The answer is (2).")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is (2).")
def run_app():
    '''
    Function to start the application.
    '''
    # Check if running in a headless environment
    if not os.environ.get('DISPLAY'):
        # Start Xvfb if not already running
        subprocess.Popen(['Xvfb', ':99', '-screen', '0', '1024x768x16'])
        os.environ['DISPLAY'] = ':99'  # Use a different display number for Xvfb
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
if __name__ == "__main__":
    run_app()