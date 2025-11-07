'''
The Shot class represents a shot fired by the player, handling movement and checking for collisions with aliens.
'''
class Shot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.width = 5
        self.height = 10
    def move(self):
        self.y -= self.speed
    def collides_with(self, alien):
        return (
            self.x < alien.x + alien.width and
            self.x + self.width > alien.x and
            self.y < alien.y + alien.height and
            self.y + self.height > alien.y
        )