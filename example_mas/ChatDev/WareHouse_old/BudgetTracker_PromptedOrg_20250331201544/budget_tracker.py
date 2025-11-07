'''
This file contains the BudgetTracker class, which manages expenses, income, calculates the balance, and provides persistent data storage using JSON with robust error handling.
'''
import json
import os
class BudgetTracker:
    def __init__(self, data_file='budget_data.json'):
        self.data_file = data_file
        self.expenses = []
        self.incomes = []
        self.load_data()
    def add_expense(self, amount, category, description):
        if amount <= 0:
            raise ValueError("Expense amount must be greater than zero.")
        self.expenses.append({"amount": amount, "category": category, "description": description})
        self.save_data()
    def add_income(self, amount, source, description):
        if amount <= 0:
            raise ValueError("Income amount must be greater than zero.")
        self.incomes.append({"amount": amount, "source": source, "description": description})
        self.save_data()
    def calculate_balance(self):
        total_income = sum(income["amount"] for income in self.incomes)
        total_expense = sum(expense["amount"] for expense in self.expenses)
        return total_income - total_expense
    def get_summary(self):
        total_income = sum(income["amount"] for income in self.incomes)
        total_expense = sum(expense["amount"] for expense in self.expenses)
        balance = self.calculate_balance()
        return {
            "total_income": total_income,
            "total_expense": total_expense,
            "balance": balance
        }
    def save_data(self):
        data = {
            "expenses": self.expenses,
            "incomes": self.incomes
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4)
    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.expenses = data.get("expenses", [])
                    self.incomes = data.get("incomes", [])
            except json.JSONDecodeError:
                # Handle corrupted JSON file by initializing empty data
                self.expenses = []
                self.incomes = []
                print("Warning: Data file corrupted. Initialized with empty data.")