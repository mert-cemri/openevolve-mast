'''
Defines the TreasureChest class for representing treasure chests.
'''
from utils import random_hp_restore
class TreasureChest:
    def __init__(self, position):
        self.position = position
    def restore_hp(self):
        return random_hp_restore()