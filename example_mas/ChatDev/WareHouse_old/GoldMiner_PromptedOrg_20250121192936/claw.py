'''
Claw class to represent the claw's movement and grabbing action.
'''
class Claw:
    def __init__(self):
        self.position = 0
        self.direction = 1  # 1 for right, -1 for left
    def move(self):
        # Move the claw back and forth
        self.position += self.direction
        if self.position > 10 or self.position < 0:
            self.direction *= -1  # Change direction
    def grab(self, objects):
        # Attempt to grab an object
        for obj in objects:
            if obj.position == self.position and not obj.is_collected:
                obj.is_collected = True
                return obj
        return None