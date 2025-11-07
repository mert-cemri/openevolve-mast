'''
This file contains the Dashboard class, which provides a GUI for interacting with the BudgetTracker, including robust input validation, error handling, and graceful handling of headless environments.
'''
import tkinter as tk
from tkinter import messagebox
import os
import sys
from budget_tracker import BudgetTracker
class Dashboard:
    def __init__(self, budget_tracker):
        self.budget_tracker = budget_tracker
        # Check for graphical display environment
        if not os.environ.get('DISPLAY'):
            print("Error: No graphical display found. Please run the application in a GUI-enabled environment.")
            sys.exit(1)
        self.root = tk.Tk()
        self.root.title("Budget Tracker Dashboard")
        # Income Entry
        tk.Label(self.root, text="Income Amount:").grid(row=0, column=0)
        self.income_amount = tk.Entry(self.root)
        self.income_amount.grid(row=0, column=1)
        tk.Label(self.root, text="Income Source:").grid(row=1, column=0)
        self.income_source = tk.Entry(self.root)
        self.income_source.grid(row=1, column=1)
        tk.Label(self.root, text="Income Description:").grid(row=2, column=0)
        self.income_description = tk.Entry(self.root)
        self.income_description.grid(row=2, column=1)
        tk.Button(self.root, text="Add Income", command=self.add_income).grid(row=3, column=1)
        # Expense Entry
        tk.Label(self.root, text="Expense Amount:").grid(row=4, column=0)
        self.expense_amount = tk.Entry(self.root)
        self.expense_amount.grid(row=4, column=1)
        tk.Label(self.root, text="Expense Category:").grid(row=5, column=0)
        self.expense_category = tk.Entry(self.root)
        self.expense_category.grid(row=5, column=1)
        tk.Label(self.root, text="Expense Description:").grid(row=6, column=0)
        self.expense_description = tk.Entry(self.root)
        self.expense_description.grid(row=6, column=1)
        tk.Button(self.root, text="Add Expense", command=self.add_expense).grid(row=7, column=1)
        # Summary Button
        tk.Button(self.root, text="Show Summary", command=self.show_summary).grid(row=8, column=1)
    def add_income(self):
        try:
            amount = float(self.income_amount.get())
            source = self.income_source.get()
            description = self.income_description.get()
            self.budget_tracker.add_income(amount, source, description)
            messagebox.showinfo("Success", "Income added successfully!")
            self.clear_income_fields()
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    def add_expense(self):
        try:
            amount = float(self.expense_amount.get())
            category = self.expense_category.get()
            description = self.expense_description.get()
            self.budget_tracker.add_expense(amount, category, description)
            messagebox.showinfo("Success", "Expense added successfully!")
            self.clear_expense_fields()
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    def show_summary(self):
        summary = self.budget_tracker.get_summary()
        message = (f"Total Income: ${summary['total_income']:.2f}\n"
                   f"Total Expenses: ${summary['total_expense']:.2f}\n"
                   f"Current Balance: ${summary['balance']:.2f}")
        messagebox.showinfo("Budget Summary", message)
    def clear_income_fields(self):
        self.income_amount.delete(0, tk.END)
        self.income_source.delete(0, tk.END)
        self.income_description.delete(0, tk.END)
    def clear_expense_fields(self):
        self.expense_amount.delete(0, tk.END)
        self.expense_category.delete(0, tk.END)
        self.expense_description.delete(0, tk.END)
    def run(self):
        self.root.mainloop()