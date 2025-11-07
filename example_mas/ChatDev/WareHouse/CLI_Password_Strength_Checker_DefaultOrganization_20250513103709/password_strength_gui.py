'''
This module contains the PasswordStrengthGUI class, which creates a Tkinter-based GUI for password strength checking.
'''
import tkinter as tk
from password_strength_checker import PasswordStrengthChecker
class PasswordStrengthGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Strength Checker")
        self.label = tk.Label(self.root, text="Enter Password:")
        self.label.pack()
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.pack()
        self.check_button = tk.Button(self.root, text="Check Strength", command=self.check_password_strength)
        self.check_button.pack()
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()
        self.checker = PasswordStrengthChecker()
    def check_password_strength(self):
        password = self.password_entry.get()
        strength = self.checker.evaluate_password_strength(password)
        self.result_label.config(text=f"Password Strength: {strength}")
    def run(self):
        self.root.mainloop()