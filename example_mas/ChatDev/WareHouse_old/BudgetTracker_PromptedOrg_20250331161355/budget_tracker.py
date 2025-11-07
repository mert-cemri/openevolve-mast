'''
Class to manage the budget tracking process, including adding expenses, adding income, and calculating savings.
'''
from excel_handler import ExcelHandler
from expense import Expense
from income import Income
class BudgetTracker:
    def __init__(self):
        self.expenses = []
        self.incomes = []
        self.excel_handler = ExcelHandler()
    def add_expense(self, expense: Expense):
        self.expenses.append(expense)
        self.excel_handler.write_expense(expense)
    def add_income(self, income: Income):
        self.incomes.append(income)
        self.excel_handler.write_income(income)
    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)
    def total_income(self):
        return sum(income.amount for income in self.incomes)
    def calculate_savings(self):
        return self.total_income() - self.total_expenses()