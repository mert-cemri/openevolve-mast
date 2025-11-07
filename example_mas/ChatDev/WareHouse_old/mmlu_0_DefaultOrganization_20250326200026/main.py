'''
Main application file for the accounting question GUI.
'''
import tkinter as tk
from tkinter import messagebox
import os
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application window.
        Parameters:
        root (tk.Tk): The root window object.
        '''
        self.root = root
        self.root.title("Accounting Question")
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the widgets in the application window.
        '''
        # Question Label
        question_label = tk.Label(self.root, text="Mast Co. converted from the FIFO method for inventory valuation to the LIFO method for financial statement and tax purposes. During a period of inflation would Mast's ending inventory and income tax payable using LIFO be higher or lower than FIFO?")
        question_label.pack(pady=10)
        # Answer Options
        self.answer_var = tk.IntVar()
        options = [
            "0. Lower Lower",
            "1. Higher Higher",
            "2. Lower Higher",
            "3. Higher Lower"
        ]
        for idx, option in enumerate(options):
            radio_button = tk.Radiobutton(self.root, text=option, variable=self.answer_var, value=idx)
            radio_button.pack(anchor='w')
        # Submit Button
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=10)
    def check_answer(self):
        '''
        Check the selected answer and display the correct answer.
        '''
        # Correct answer logic
        correct_answer = 0  # During inflation, LIFO results in lower ending inventory and lower income tax payable compared to FIFO.
        if self.answer_var.get() == correct_answer:
            messagebox.showinfo("Result", "Correct! The answer is 0.")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is 0.")
def run_app():
    '''
    Instantiate and run the application.
    '''
    # Check if running in a headless environment
    if os.environ.get('DISPLAY', '') == '':
        print("No display found. Please run this application in an environment with a graphical display.")
    else:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()
if __name__ == "__main__":
    run_app()