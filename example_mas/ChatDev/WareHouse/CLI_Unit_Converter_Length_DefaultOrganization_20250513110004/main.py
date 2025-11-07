'''
Main application file for the CLI unit converter.
'''
from converter import convert_length
def main():
    try:
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the source unit (meters, feet, inches, cm): ").strip().lower()
        to_unit = input("Enter the target unit (meters, feet, inches, cm): ").strip().lower()
        if from_unit not in ["meters", "feet", "inches", "cm"] or to_unit not in ["meters", "feet", "inches", "cm"]:
            print("Invalid unit. Please enter a valid unit (meters, feet, inches, cm).")
            return
        result = convert_length(value, from_unit, to_unit)
        print(f"Result: {result:.2f} {to_unit}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
if __name__ == "__main__":
    main()