'''
This script is a CLI application for converting lengths between different units.
The user inputs a value, a source unit, and a target unit, and the script outputs
the converted value.
'''
def convert_length(value, from_unit, to_unit):
    '''
    Convert length from one unit to another.
    Parameters:
    value (float): The numerical value to convert.
    from_unit (str): The unit of the input value.
    to_unit (str): The unit to convert the value to.
    Returns:
    float: The converted value.
    '''
    # Conversion factors relative to meters
    conversion_factors = {
        'm': 1.0,
        'cm': 100.0,
        'in': 39.3701,
        'ft': 3.28084
    }
    # Check if the units are valid
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise KeyError("Invalid unit. Please enter a valid unit (m, cm, in, ft).")
    # Convert the input value to meters
    value_in_meters = value / conversion_factors[from_unit]
    # Convert from meters to the target unit
    converted_value = value_in_meters * conversion_factors[to_unit]
    return converted_value
def main():
    '''
    Main function to run the CLI unit converter.
    Prompts the user for input values, source unit, and target unit,
    and displays the converted result.
    '''
    try:
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the source unit (m, cm, in, ft): ").strip().lower()
        to_unit = input("Enter the target unit (m, cm, in, ft): ").strip().lower()
        result = convert_length(value, from_unit, to_unit)
        print(f"Result: {result:.4f} {to_unit}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    except KeyError as e:
        print(e)
if __name__ == "__main__":
    main()