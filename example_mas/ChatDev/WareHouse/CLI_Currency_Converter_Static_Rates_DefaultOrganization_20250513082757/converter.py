'''
Handles currency conversion using predefined exchange rates.
'''
import json
class CurrencyConverter:
    def __init__(self, config_file):
        self.exchange_rates = self.load_exchange_rates(config_file)
    def load_exchange_rates(self, config_file):
        '''
        Loads exchange rates from a configuration file.
        The rates are assumed to be relative to USD.
        '''
        try:
            with open(config_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise ValueError("Configuration file not found.")
        except json.JSONDecodeError:
            raise ValueError("Configuration file contains invalid JSON.")
    def convert(self, amount, source_currency, target_currency):
        '''
        Converts an amount from the source currency to the target currency.
        '''
        if source_currency not in self.exchange_rates or target_currency not in self.exchange_rates:
            raise ValueError("Currency not supported.")
        if source_currency == target_currency:
            return amount
        rate = self.exchange_rates[target_currency] / self.exchange_rates[source_currency]
        return amount * rate