'''
This file contains the main application logic for the nutrition quiz GUI.
'''
import tkinter as tk
from tkinter import messagebox
import os
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application window and setup GUI components.
        '''
        self.root = root
        self.root.title("Nutrition Quiz")
        self.question = "Which of these factors increases the risk for postmenopausal breast cancer?"
        self.options = ["Red meat", "Dietary fat", "Fish", "Obesity"]
        self.correct_answer_index = 3
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the widgets in the window.
        '''
        # Create question label
        self.question_label = tk.Label(self.root, text=self.question, wraplength=400, justify="left")
        self.question_label.pack(pady=10)
        # Create radio buttons for options
        self.selected_option = tk.IntVar()
        self.selected_option.set(-1)  # No option selected initially
        for idx, option in enumerate(self.options):
            rb = tk.Radiobutton(self.root, text=option, variable=self.selected_option, value=idx)
            rb.pack(anchor="w")
        # Create submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=20)
    def submit_answer(self):
        '''
        Handle the logic for when the user submits their answer.
        '''
        selected_index = self.selected_option.get()
        if selected_index == -1:
            messagebox.showwarning("No Selection", "Please select an option before submitting.")
        elif selected_index == self.correct_answer_index:
            messagebox.showinfo("Correct!", "The answer is correct!")
        else:
            messagebox.showinfo("Incorrect", f"The correct answer is: {self.options[self.correct_answer_index]}")
def run_app():
    '''
    Start the application.
    '''
    # Check if running in a headless environment and set up a virtual display if necessary
    if not os.environ.get('DISPLAY'):
        os.environ['DISPLAY'] = ':0'
        from pyvirtualdisplay import Display
        display = Display(visible=0, size=(800, 600))
        display.start()
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
if __name__ == "__main__":
    run_app()