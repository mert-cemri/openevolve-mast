'''
Saving class to represent individual saving entries.
'''
class Saving:
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description
    def __repr__(self):
        return f"Saving(amount={self.amount}, description='{self.description}')"