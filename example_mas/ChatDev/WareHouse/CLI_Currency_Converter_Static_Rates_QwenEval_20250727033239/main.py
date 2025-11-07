'''
Handles the command-line interface for the currency converter.
'''
import converter
def main():
    try:
        amount = float(input("Enter the amount: "))
        source_currency = input("Enter the source currency (e.g., USD): ").upper()
        target_currency = input("Enter the target currency (e.g., EUR): ").upper()
        result = converter.convert(amount, source_currency, target_currency)
        print(f"{amount} {source_currency} is {result:.2f} {target_currency}")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
if __name__ == "__main__":
    main()