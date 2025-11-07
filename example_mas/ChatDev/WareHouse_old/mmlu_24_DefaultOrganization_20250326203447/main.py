'''
This file contains the main application logic and GUI implementation for the moral scenarios question.
'''
import tkinter as tk
from tkinter import messagebox
from pyvirtualdisplay import Display
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application window and its components.
        '''
        self.root = root
        self.root.title("Moral Scenarios Quiz")
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the widgets in the main window.
        '''
        # Question Label
        question_text = ("For which of these two scenarios does the main character "
                         "(who uses I/me/my) do something clearly morally wrong, "
                         "according to ordinary moral standards in the US as of 2020?\n"
                         "Scenario 1 | I refilled the shampoo bottle with shaving cream "
                         "and put it back in the shower.\n"
                         "Scenario 2 | I kept a distance from an ambulance.")
        self.question_label = tk.Label(self.root, text=question_text, wraplength=400, justify="left")
        self.question_label.pack(pady=10)
        # Answer Options
        self.answer_var = tk.IntVar()
        options = [
            "0. Wrong, Wrong",
            "1. Wrong, Not wrong",
            "2. Not wrong, Wrong",
            "3. Not wrong, Not wrong"
        ]
        for idx, option in enumerate(options):
            tk.Radiobutton(self.root, text=option, variable=self.answer_var, value=idx).pack(anchor="w")
        # Submit Button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check if the selected answer is correct and display the result.
        '''
        correct_answer = 1
        selected_answer = self.answer_var.get()
        if selected_answer == correct_answer:
            messagebox.showinfo("Result", "Correct! The answer is 1.")
        else:
            messagebox.showerror("Result", f"Incorrect. The correct answer is 1.")
def run_app():
    '''
    Instantiate and run the application.
    '''
    try:
        # Start a virtual display
        display = Display(visible=0, size=(800, 600))
        display.start()
    except FileNotFoundError:
        print("Xvfb is not installed. Please install it using 'sudo apt-get install xvfb' on Debian-based systems.")
        return
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
    # Stop the virtual display
    display.stop()
if __name__ == "__main__":
    run_app()