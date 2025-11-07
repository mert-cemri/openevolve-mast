'''
Expense class to represent individual expense entries.
'''
class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
    def __repr__(self):
        return f"Expense(amount={self.amount}, category='{self.category}', description='{self.description}')"