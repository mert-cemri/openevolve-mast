'''
Conversion logic for the unit converter.
'''
def convert_length(value, from_unit, to_unit):
    # Conversion factors relative to meters
    unit_conversion_factors = {
        "meters": 1.0,
        "feet": 0.3048,
        "inches": 0.0254,
        "cm": 0.01
    }
    # Convert from source unit to meters
    value_in_meters = value * unit_conversion_factors[from_unit]
    # Convert from meters to target unit
    converted_value = value_in_meters / unit_conversion_factors[to_unit]
    return converted_value