'''
Module to handle the conversion of length units.
'''
class Converter:
    def __init__(self):
        self.conversion_factors = {
            'meters': {'feet': 3.28084, 'inches': 39.3701, 'cm': 100},
            'feet': {'meters': 0.3048, 'inches': 12, 'cm': 30.48},
            'inches': {'meters': 0.0254, 'feet': 0.0833333, 'cm': 2.54},
            'cm': {'meters': 0.01, 'feet': 0.0328084, 'inches': 0.393701}
        }
    def convert(self, value, source_unit, target_unit):
        if source_unit not in self.conversion_factors or target_unit not in self.conversion_factors[source_unit]:
            raise ValueError(f"Invalid source or target unit. Available units: {', '.join(self.conversion_factors.keys())}.")
        return value * self.conversion_factors[source_unit][target_unit]