'''
This script provides a CLI tool to convert temperatures between Celsius, Fahrenheit, and Kelvin.
The user inputs the value, the source unit (C, F, K), and the target unit. The converted temperature is displayed.
'''
import argparse
class TemperatureConverter:
    '''
    A class to perform temperature conversions between Celsius, Fahrenheit, and Kelvin.
    '''
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15
    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15
    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9/5 + 32
    @staticmethod
    def convert(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == 'C':
            if to_unit == 'F':
                return TemperatureConverter.celsius_to_fahrenheit(value)
            elif to_unit == 'K':
                return TemperatureConverter.celsius_to_kelvin(value)
        elif from_unit == 'F':
            if to_unit == 'C':
                return TemperatureConverter.fahrenheit_to_celsius(value)
            elif to_unit == 'K':
                return TemperatureConverter.fahrenheit_to_kelvin(value)
        elif from_unit == 'K':
            if to_unit == 'C':
                return TemperatureConverter.kelvin_to_celsius(value)
            elif to_unit == 'F':
                return TemperatureConverter.kelvin_to_fahrenheit(value)
        raise ValueError("Invalid conversion units")
def main():
    '''
    Main function to handle command-line arguments and perform temperature conversion.
    '''
    parser = argparse.ArgumentParser(description='Convert temperatures between Celsius, Fahrenheit, and Kelvin.')
    parser.add_argument('value', type=float, help='The temperature value to convert')
    parser.add_argument('from_unit', choices=['C', 'F', 'K'], help='The unit of the input temperature (C, F, K)')
    parser.add_argument('to_unit', choices=['C', 'F', 'K'], help='The unit to convert the temperature to (C, F, K)')
    args = parser.parse_args()
    try:
        result = TemperatureConverter.convert(args.value, args.from_unit, args.to_unit)
        print(f"Converted temperature: {result:.2f} {args.to_unit}")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()