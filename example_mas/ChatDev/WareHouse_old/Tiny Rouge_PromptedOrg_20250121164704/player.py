'''
Player class to represent the player character.
'''
from position import Position
class Player:
    def __init__(self, start_position):
        self.position = start_position
        self.hp = 100
    def move(self, direction, game_map):
        new_position = self.position.move(direction)
        if game_map.is_valid_move(new_position):
            self.position = new_position
    def fight(self, monster):
        self.hp -= monster.hp
        if self.hp > 0:
            print(f"Defeated the monster! Remaining HP: {self.hp}")
        else:
            print("You were defeated by the monster!")
    def collect_treasure(self, treasure):
        restored_hp = treasure.restore_hp()
        self.hp += restored_hp
        print(f"Collected treasure! Restored {restored_hp} HP. Current HP: {self.hp}")