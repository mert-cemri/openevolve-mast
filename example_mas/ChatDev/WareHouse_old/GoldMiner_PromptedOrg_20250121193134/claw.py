'''
Claw class to represent the claw's movement and grabbing action.
'''
import time
class Claw:
    def __init__(self):
        self.position = 0
        self.direction = 1
        self.current_object = None
    def move(self):
        self.position += self.direction
        if self.position > 10 or self.position < 0:  # Assuming a range of 0 to 10
            self.direction *= -1
    def grab(self, objects):
        for obj in objects:
            if obj.position == self.position:
                self.current_object = obj
                return True
        return False