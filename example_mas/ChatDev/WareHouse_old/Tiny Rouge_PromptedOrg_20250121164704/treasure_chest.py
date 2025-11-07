'''
TreasureChest class to represent treasure chests that restore player's health.
'''
import random
class TreasureChest:
    def restore_hp(self):
        return random.randint(20, 30)