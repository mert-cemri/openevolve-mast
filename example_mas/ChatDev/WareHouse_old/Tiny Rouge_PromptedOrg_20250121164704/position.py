'''
Position utility class to handle positions on the map.
'''
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def move(self, direction):
        if direction == 'W':
            return Position(self.x, self.y - 1)
        elif direction == 'S':
            return Position(self.x, self.y + 1)
        elif direction == 'A':
            return Position(self.x - 1, self.y)
        elif direction == 'D':
            return Position(self.x + 1, self.y)
        return self