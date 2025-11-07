'''
Conversion logic for the unit converter.
'''
def convert_units(value, source_unit, target_unit):
    conversion_factor = get_conversion_factor(source_unit, target_unit)
    if conversion_factor is None:
        raise ValueError(f"Conversion from {source_unit} to {target_unit} not supported.")
    return value * conversion_factor
def get_conversion_factor(source_unit, target_unit):
    conversion_factors = {
        ('kilograms', 'pounds'): 2.20462,
        ('pounds', 'kilograms'): 0.453592,
        ('grams', 'ounces'): 0.035274,
        ('ounces', 'grams'): 28.3495,
        # Add more conversion factors as needed
    }
    return conversion_factors.get((source_unit, target_unit))