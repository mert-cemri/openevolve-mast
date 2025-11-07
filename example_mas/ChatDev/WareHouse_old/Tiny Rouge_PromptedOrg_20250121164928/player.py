'''
Player class to handle player actions and state.
'''
class Player:
    def __init__(self, start_position):
        self.position = start_position
        self.hp = 100  # Initial HP
    def move(self, direction, game_map):
        new_position = self.position
        if direction == 'W':
            new_position = (self.position[0] - 1, self.position[1])
        elif direction == 'S':
            new_position = (self.position[0] + 1, self.position[1])
        elif direction == 'A':
            new_position = (self.position[0], self.position[1] - 1)
        elif direction == 'D':
            new_position = (self.position[0], self.position[1] + 1)
        if game_map.is_walkable(new_position):
            self.position = new_position
            game_map.interact(self)
    def adjust_hp(self, amount):
        self.hp += amount
        print(f"Player HP: {self.hp}")