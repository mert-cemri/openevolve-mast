'''
This module contains the main application logic for evaluating a multiple-choice question about string comparisons.
'''
import tkinter as tk
from tkinter import messagebox
def compare_strings(strA, strB, strC):
    '''
    Compare the given strings according to the problem statement and return the index of the correct answer.
    '''
    # Perform the comparisons using compareTo logic
    condition_0 = (strA < strB) and (strB > strC)
    condition_1 = (strC < strB) and (strB < strA)
    condition_2 = (strB < strC) and (strB > strA)
    condition_3 = (strA != strB) and (strB < strA)
    # Determine which condition is true
    if condition_0:
        return 0
    elif condition_1:
        return 1
    elif condition_2:
        return 2
    elif condition_3:
        return 3
    else:
        return None
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application window and its components.
        '''
        self.root = root
        self.root.title("String Comparison Evaluator")
        # Labels and entries for input
        self.labelA = tk.Label(root, text="String A:")
        self.labelA.pack()
        self.entryA = tk.Entry(root)
        self.entryA.pack()
        self.labelB = tk.Label(root, text="String B:")
        self.labelB.pack()
        self.entryB = tk.Entry(root)
        self.entryB.pack()
        self.labelC = tk.Label(root, text="String C:")
        self.labelC.pack()
        self.entryC = tk.Entry(root)
        self.entryC.pack()
        # Button to evaluate the question
        self.evaluate_button = tk.Button(root, text="Evaluate", command=self.evaluate_question)
        self.evaluate_button.pack()
    def evaluate_question(self):
        '''
        Evaluate the multiple-choice question based on user input and display the result.
        '''
        # Get user input
        strA = self.entryA.get()
        strB = self.entryB.get()
        strC = self.entryC.get()
        # Compare strings and get the answer
        answer = compare_strings(strA, strB, strC)
        # Display the result
        if answer is not None:
            messagebox.showinfo("Result", f"The answer is ({answer})")
        else:
            messagebox.showerror("Error", "No valid condition met.")
if __name__ == "__main__":
    import os
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()