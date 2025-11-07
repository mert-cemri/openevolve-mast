'''
Currency conversion logic using predefined exchange rates.
'''
class CurrencyConverter:
    def __init__(self, rates):
        self.rates = rates
    def convert(self, amount, source_currency, target_currency):
        if source_currency not in self.rates or target_currency not in self.rates:
            raise ValueError("Invalid currency code.")
        if source_currency == target_currency:
            return amount
        # Convert to base currency (e.g., USD) first
        base_amount = amount / self.rates[source_currency]
        # Convert from base currency to target currency
        return base_amount * self.rates[target_currency]