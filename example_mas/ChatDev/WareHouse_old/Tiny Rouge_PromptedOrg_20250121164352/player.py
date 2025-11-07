'''
Player class to represent the player character and handle movement and interactions.
'''
class Player:
    def __init__(self, start_position):
        self.position = start_position
        self.hp = 100
    def move(self, direction, game_map):
        x, y = self.position
        if direction == 'W':
            new_position = (x, y - 1)
        elif direction == 'S':
            new_position = (x, y + 1)
        elif direction == 'A':
            new_position = (x - 1, y)
        elif direction == 'D':
            new_position = (x + 1, y)
        if game_map.is_walkable(*new_position):
            self.position = new_position
    def interact_with_object(self, obj):
        if isinstance(obj, Monster):
            obj.attack(self)
        elif isinstance(obj, TreasureChest):
            obj.open(self)
        elif isinstance(obj, Door):
            obj.go_to_next_level(self)
    def change_hp(self, amount):
        self.hp += amount
        print(f"Player HP: {self.hp}")