'''
Class to represent an individual expense.
'''
class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date