'''
BudgetTracker class to manage expenses and savings with input validation.
'''
from expense import Expense
from saving import Saving
from collections import defaultdict
class BudgetTracker:
    def __init__(self):
        self.expenses = []
        self.savings = []
    def add_expense(self, amount, category, description):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Expense amount must be a positive number.")
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
    def add_saving(self, amount, description):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Saving amount must be a positive number.")
        saving = Saving(amount, description)
        self.savings.append(saving)
    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)
    def get_total_savings(self):
        return sum(saving.amount for saving in self.savings)
    def get_balance(self):
        return self.get_total_savings() - self.get_total_expenses()
    def get_expenses_by_category(self):
        categories = defaultdict(float)
        for expense in self.expenses:
            categories[expense.category] += expense.amount
        return dict(categories)