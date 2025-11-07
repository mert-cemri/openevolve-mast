'''
Main application file for the multiple-choice question GUI using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from question import Question
import os
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clinical Knowledge Quiz")
        # Create a question instance
        self.question = Question(
            "The key attribute in successful marathon running is:",
            ["strength", "power", "stride length", "stamina"],
            3
        )
        # GUI components
        self.question_label = tk.Label(root, text=self.question.text)
        self.question_label.pack(pady=10)
        self.var = tk.IntVar()
        self.radio_buttons = []
        for idx, option in enumerate(self.question.options):
            rb = tk.Radiobutton(root, text=option, variable=self.var, value=idx)
            rb.pack(anchor='w')
            self.radio_buttons.append(rb)
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)
    def check_answer(self):
        selected_index = self.var.get()
        if selected_index == self.question.correct_answer:
            messagebox.showinfo("Result", "Correct! The answer is (3)")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is (3)")
if __name__ == "__main__":
    # Check if running in a headless environment
    if not os.environ.get('DISPLAY'):
        try:
            # Attempt to use Xvfb for a virtual display
            from pyvirtualdisplay import Display
            display = Display(visible=0, size=(800, 600))
            display.start()
        except ImportError:
            print("pyvirtualdisplay is not installed. Please install it to run in a headless environment.")
            exit(1)
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()