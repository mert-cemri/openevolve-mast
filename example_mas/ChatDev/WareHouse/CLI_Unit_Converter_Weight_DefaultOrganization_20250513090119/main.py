'''
Main application file for the CLI unit converter.
'''
from conversion import convert_units
def main():
    try:
        value = float(input("Enter the value to convert: "))
        source_unit = input("Enter the source unit: ").strip().lower()
        target_unit = input("Enter the target unit: ").strip().lower()
        result = convert_units(value, source_unit, target_unit)
        print(f"Result: {result} {target_unit}")
    except ValueError as e:
        print(f"Error: {e}")
        print("Supported conversions are:")
        print(" - kilograms to pounds")
        print(" - pounds to kilograms")
        print(" - grams to ounces")
        print(" - ounces to grams")
if __name__ == "__main__":
    main()