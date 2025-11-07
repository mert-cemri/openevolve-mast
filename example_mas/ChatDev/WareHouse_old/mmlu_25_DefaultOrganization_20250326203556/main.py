'''
This file contains the main application code for displaying a GUI to solve a multiple-choice question about string comparison.
'''
import tkinter as tk
from tkinter import messagebox
def compare_strings():
    '''
    Compare strings according to the given rules and return the index of the correct answer.
    '''
    strA = "CARROT"
    strB = "Carrot"
    strC = "car"
    # Check each condition using Python string comparison operators
    if strA < strB and strB > strC:
        return 0
    elif strC < strB and strB < strA:
        return 1
    elif strB < strC and strB > strA:
        return 2
    elif strA != strB and strB < strA:
        return 3
    else:
        return None
class MainApplication(tk.Tk):
    def __init__(self):
        '''
        Initialize the main application window and its components.
        '''
        super().__init__()
        self.title("String Comparison Quiz")
        self.geometry("500x300")
        # Question label
        question_label = tk.Label(self, text="This question is based on the following declarations:\n"
                                             "String strA = 'CARROT', strB = 'Carrot', strC = 'car';\n"
                                             "Given that all uppercase letters precede all lowercase letters when considering alphabetical order, which is true?")
        question_label.pack(pady=10)
        # Answer options
        self.answer_var = tk.IntVar()
        options = [
            "0. strA.compareTo(strB) < 0 && strB.compareTo(strC) > 0",
            "1. strC.compareTo(strB) < 0 && strB.compareTo(strA) < 0",
            "2. strB.compareTo(strC) < 0 && strB.compareTo(strA) > 0",
            "3. !(strA.compareTo(strB) == 0) && strB.compareTo(strA) < 0"
        ]
        for idx, option in enumerate(options):
            tk.Radiobutton(self, text=option, variable=self.answer_var, value=idx).pack(anchor='w')
        # Submit button
        submit_button = tk.Button(self, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check the selected answer and display the correct answer.
        '''
        correct_answer = compare_strings()
        selected_answer = self.answer_var.get()
        if selected_answer == correct_answer:
            messagebox.showinfo("Result", f"Correct! The answer is {correct_answer}.")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is {correct_answer}.")
if __name__ == "__main__":
    try:
        app = MainApplication()
        app.mainloop()
    except tk.TclError as e:
        print("Error: Unable to start the GUI. Please ensure you are running this on a system with a graphical display.")
        print(e)