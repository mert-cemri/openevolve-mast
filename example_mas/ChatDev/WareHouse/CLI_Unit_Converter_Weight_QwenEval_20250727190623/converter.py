'''
This module contains the core conversion logic for weights/mass.
'''
class Converter:
    def __init__(self):
        self.conversion_factors = {
            'kg': {'lb': 2.20462, 'oz': 35.274},
            'g': {'lb': 0.00220462, 'oz': 0.035274},
            'lb': {'kg': 0.453592, 'oz': 16},
            'oz': {'kg': 0.0283495, 'lb': 0.0625}
        }
    def convert(self, value, source_unit, target_unit):
        '''
        Convert a given value from a source unit to a target unit.
        Parameters:
        value (float): The value to be converted.
        source_unit (str): The unit of the input value.
        target_unit (str): The unit to convert the input value to.
        Returns:
        float: The converted value.
        Raises:
        ValueError: If the value is negative or if the conversion is not supported.
        '''
        if value < 0:
            raise ValueError("Value must be non-negative.")
        if source_unit not in self.conversion_factors or target_unit not in self.conversion_factors[source_unit]:
            raise ValueError(f"Conversion from {source_unit} to {target_unit} is not supported.")
        return value * self.conversion_factors[source_unit][target_unit]