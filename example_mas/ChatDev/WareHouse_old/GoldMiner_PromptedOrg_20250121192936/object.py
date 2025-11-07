'''
Object class to represent objects in the game.
'''
class Object:
    def __init__(self, type, value, position):
        self.type = type
        self.value = value
        self.position = position
        self.is_collected = False
    def get_value(self):
        return self.value if self.is_collected else 0