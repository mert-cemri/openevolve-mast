'''
Unit class for weights/mass
'''
class Unit:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
    def convert(self, target_unit):
        if self.unit == 'kg' and target_unit == 'lb':
            return self.value * 2.20462
        elif self.unit == 'lb' and target_unit == 'kg':
            return self.value / 2.20462
        elif self.unit == 'g' and target_unit == 'oz':
            return self.value * 0.035274
        elif self.unit == 'oz' and target_unit == 'g':
            return self.value / 0.035274
        else:
            raise ValueError(f'Invalid unit: {target_unit}')