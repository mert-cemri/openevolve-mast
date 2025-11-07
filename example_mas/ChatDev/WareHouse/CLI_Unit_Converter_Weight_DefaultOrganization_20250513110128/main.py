'''
This script implements a CLI unit converter for weights/mass. 
It allows the user to input a value, source unit, and target unit, 
and then performs the conversion.
'''
def convert_units(value, source_unit, target_unit):
    '''
    Converts the given value from the source unit to the target unit.
    :param value: The numerical value to convert.
    :param source_unit: The unit of the input value.
    :param target_unit: The unit to convert the value to.
    :return: The converted value.
    '''
    # Conversion factors relative to 1 kilogram
    conversion_factors = {
        'kg': 1,
        'lb': 2.20462,
        'g': 1000,
        'oz': 35.274
    }
    # Convert the source value to kilograms
    value_in_kg = value / conversion_factors[source_unit]
    # Convert from kilograms to the target unit
    converted_value = value_in_kg * conversion_factors[target_unit]
    return converted_value
def main():
    '''
    Main function to handle user input and perform unit conversion.
    '''
    try:
        value = float(input("Enter the value to convert: "))
        source_unit = input("Enter the source unit (kg, lb, g, oz): ").strip().lower()
        target_unit = input("Enter the target unit (kg, lb, g, oz): ").strip().lower()
        # Validate units
        valid_units = ['kg', 'lb', 'g', 'oz']
        if source_unit not in valid_units or target_unit not in valid_units:
            print("Invalid unit. Please enter one of the following units: kg, lb, g, oz.")
            return
        # Perform conversion
        result = convert_units(value, source_unit, target_unit)
        print(f"Result: {result:.4f} {target_unit}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
if __name__ == "__main__":
    main()