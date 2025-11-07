'''
Object class to represent objects that can be grabbed by the claw.
'''
class Object:
    def __init__(self, value, weight, position):
        self.value = value
        self.weight = weight
        self.position = position
        self.grabbed = False
    def get_value(self):
        return self.value
    def get_weight(self):
        return self.weight