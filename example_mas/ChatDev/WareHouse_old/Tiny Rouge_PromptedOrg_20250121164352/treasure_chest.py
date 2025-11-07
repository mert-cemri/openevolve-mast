'''
TreasureChest class to represent treasure chests in the game.
'''
import random
class TreasureChest:
    def open(self, player):
        hp_restored = random.randint(20, 30)
        player.change_hp(hp_restored)
        print(f"Treasure chest opened! Player HP restored by {hp_restored}.")