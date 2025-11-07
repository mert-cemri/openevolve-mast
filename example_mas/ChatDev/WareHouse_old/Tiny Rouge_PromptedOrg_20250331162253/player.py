'''
Player class to represent the player character, including attributes like position and health.
'''
class Player:
    def __init__(self, start_position):
        self.position = start_position
        self.hp = 100
    def move(self, direction, game_map):
        x, y = self.position
        if direction == 'W':
            new_position = (x, y - 1)
        elif direction == 'A':
            new_position = (x - 1, y)
        elif direction == 'S':
            new_position = (x, y + 1)
        elif direction == 'D':
            new_position = (x + 1, y)
        if game_map.is_floor_tile(new_position):
            self.position = new_position