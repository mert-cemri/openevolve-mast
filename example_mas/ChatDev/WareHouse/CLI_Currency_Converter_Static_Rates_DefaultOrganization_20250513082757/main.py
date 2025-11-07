'''
Main entry point for the currency converter application. Handles user interactions via CLI.
'''
from converter import CurrencyConverter
def main():
    converter = CurrencyConverter("config.json")
    try:
        amount = float(input("Enter amount: "))
        source_currency = input("Enter source currency: ").upper()
        target_currency = input("Enter target currency: ").upper()
        result = converter.convert(amount, source_currency, target_currency)
        print(f"Converted amount: {result:.2f} {target_currency}")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()