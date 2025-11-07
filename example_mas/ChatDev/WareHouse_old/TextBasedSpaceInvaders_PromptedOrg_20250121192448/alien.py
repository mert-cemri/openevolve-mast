'''
The Alien class represents an alien, handling movement and checking for collisions with shots.
'''
class Alien:
    def __init__(self, x, y):
        self.x = x * 80
        self.y = y * 60
        self.speed = 1
        self.width = 40
        self.height = 30
    def move(self):
        self.y += self.speed
    def reaches_bottom(self):
        return self.y >= 600