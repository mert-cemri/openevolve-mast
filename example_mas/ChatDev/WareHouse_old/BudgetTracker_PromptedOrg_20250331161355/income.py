'''
Class to represent an individual income entry.
'''
class Income:
    def __init__(self, amount, source, date):
        self.amount = amount
        self.source = source
        self.date = date