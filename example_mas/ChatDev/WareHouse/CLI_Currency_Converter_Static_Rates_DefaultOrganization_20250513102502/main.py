'''
Main entry point for the CLI currency converter application.
'''
from converter import CurrencyConverter
from exchange_rates import load_rates
def main():
    converter = CurrencyConverter(load_rates('config.json'))
    try:
        amount = float(input("Enter amount: "))
        source_currency = input("Enter source currency: ").upper()
        target_currency = input("Enter target currency: ").upper()
        result = converter.convert(amount, source_currency, target_currency)
        print(f"Converted Amount: {result:.2f} {target_currency}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()