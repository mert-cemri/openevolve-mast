'''
This module contains the PasswordStrengthGUI class,
which provides a graphical user interface for the Password Strength Checker tool.
'''
import tkinter as tk
from password_evaluator import PasswordEvaluator
class PasswordStrengthGUI:
    def __init__(self):
        self.evaluator = PasswordEvaluator()
        self.root = tk.Tk()
        self.root.title("Password Strength Checker")
        self.root.geometry("350x250")
        self.root.configure(bg="#f0f0f0")
        self.label = tk.Label(self.root, text="Enter a password:", bg="#f0f0f0", font=("Arial", 12))
        self.label.pack(pady=10)
        self.entry = tk.Entry(self.root, show="*", width=30, font=("Arial", 12))
        self.entry.pack(pady=5)
        self.submit_button = tk.Button(self.root, text="Check Strength", command=self.on_submit, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.submit_button.pack(pady=10)
        self.result_label = tk.Label(self.root, text="", bg="#f0f0f0", font=("Arial", 12))
        self.result_label.pack(pady=5)
        self.feedback_label = tk.Label(self.root, text="", bg="#f0f0f0", font=("Arial", 12))
        self.feedback_label.pack(pady=5)
    def run(self):
        '''
        Main method to run the GUI tool.
        Starts the Tkinter event loop.
        '''
        self.root.mainloop()
    def on_submit(self):
        '''
        Event handler for the "Check Strength" button.
        Evaluates the entered password and displays the strength score.
        '''
        password = self.entry.get()
        score = self.evaluator.evaluate(password)
        self.display_strength(score)
    def display_strength(self, score):
        '''
        Displays the password strength score in the GUI.
        '''
        self.result_label.config(text=f"Password strength score: {score}/5")
        feedback = self.get_feedback(score)
        self.feedback_label.config(text=feedback)
    def get_feedback(self, score):
        '''
        Provides feedback based on the password strength score.
        '''
        if score == 5:
            return "Your password is very strong! It meets all the criteria."
        elif score == 4:
            return "Your password is strong. Consider adding a special character or a number."
        elif score == 3:
            return "Your password is moderate. Consider adding more complexity."
        elif score == 2:
            return "Your password is weak. Please make it stronger by adding uppercase letters, numbers, and special characters."
        else:
            return "Your password is very weak. Please make it stronger by adding uppercase letters, numbers, and special characters."