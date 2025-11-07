'''
Main application file for the machine learning multiple-choice question GUI.
'''
import tkinter as tk
from tkinter import messagebox
class Question:
    '''
    A class to represent a multiple-choice question.
    '''
    def __init__(self, text, options, correct_index):
        self.text = text
        self.options = options
        self.correct_index = correct_index
class MainApp:
    '''
    Main application class to create and manage the GUI.
    '''
    def __init__(self, root):
        self.root = root
        self.root.title("Machine Learning Quiz")
        # Define the question
        self.question = Question(
            "Statement 1| The SVM learning algorithm is guaranteed to find the globally optimal hypothesis with respect to its object function. "
            "Statement 2| After being mapped into feature space Q through a radial basis kernel function, a Perceptron may be able to achieve better classification performance than in its original space (though we can’t guarantee this).",
            ["True, True", "False, False", "True, False", "False, True"],
            3
        )
        # Create GUI components
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and place the GUI components.
        '''
        # Question label
        question_label = tk.Label(self.root, text=self.question.text, wraplength=400, justify="left")
        question_label.pack(pady=10)
        # Radio buttons for options
        self.selected_option = tk.IntVar()
        self.selected_option.set(-1)  # No option selected initially
        for idx, option in enumerate(self.question.options):
            radio_button = tk.Radiobutton(self.root, text=option, variable=self.selected_option, value=idx)
            radio_button.pack(anchor="w")
        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=10)
    def check_answer(self):
        '''
        Check the selected answer and display the correct answer.
        '''
        selected_index = self.selected_option.get()
        if selected_index == -1:
            messagebox.showwarning("Warning", "Please select an option.")
        elif selected_index == self.question.correct_index:
            messagebox.showinfo("Result", "Correct! The answer is (3).")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is (3).")
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()
    except tk.TclError as e:
        print("Error: Unable to access the display. Ensure you are running this script in an environment with GUI support.")