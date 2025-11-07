'''
Handles the temperature conversion logic.
'''
class TemperatureConverter:
    def convert(self, value, source_unit, target_unit):
        if source_unit == target_unit:
            return value  # No conversion needed if source and target units are the same
        elif source_unit == 'C':
            if target_unit == 'F':
                return self.celsius_to_fahrenheit(value)
            elif target_unit == 'K':
                return self.celsius_to_kelvin(value)
        elif source_unit == 'F':
            if target_unit == 'C':
                return self.fahrenheit_to_celsius(value)
            elif target_unit == 'K':
                return self.fahrenheit_to_kelvin(value)
        elif source_unit == 'K':
            if target_unit == 'C':
                return self.kelvin_to_celsius(value)
            elif target_unit == 'F':
                return self.kelvin_to_fahrenheit(value)
        raise ValueError("Invalid source or target unit")
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32
    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15
    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9
    def fahrenheit_to_kelvin(self, fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15
    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15
    def kelvin_to_fahrenheit(self, kelvin):
        return (kelvin - 273.15) * 9/5 + 32