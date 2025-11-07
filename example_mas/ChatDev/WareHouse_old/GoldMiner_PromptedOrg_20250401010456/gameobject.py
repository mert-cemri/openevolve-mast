'''
Defines the GameObject class representing objects in the game.
'''
class GameObject:
    def __init__(self, type, value, position, weight):
        self.type = type
        self.value = value
        self.position = position
        self.weight = weight