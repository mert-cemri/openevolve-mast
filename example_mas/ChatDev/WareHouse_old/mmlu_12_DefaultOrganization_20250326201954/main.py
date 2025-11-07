'''
Main application file for the moral scenarios quiz using Tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from question import create_question
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Moral Scenarios Quiz")
        # Create a question
        self.question = create_question()
        # Display the question
        self.question_label = tk.Label(root, text=self.question.text, wraplength=400, justify="left")
        self.question_label.pack(pady=10)
        # Variable to store the selected answer
        self.selected_answer = tk.IntVar()
        # Display the options
        for idx, option in enumerate(self.question.options):
            radio_button = tk.Radiobutton(root, text=option, variable=self.selected_answer, value=idx)
            radio_button.pack(anchor="w")
        # Submit button
        submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=10)
    def check_answer(self):
        selected_index = self.selected_answer.get()
        if selected_index == self.question.correct_answer:
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", "Incorrect. Try again.")
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()
    except tk.TclError:
        print("Tkinter cannot be initialized. Ensure a display environment is available.")