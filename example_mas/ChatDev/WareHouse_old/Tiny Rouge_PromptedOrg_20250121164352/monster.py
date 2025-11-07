'''
Monster class to represent monsters in the game.
'''
class Monster:
    def __init__(self):
        self.hp = 50
    def attack(self, player):
        player.change_hp(-self.hp)
        print("Monster attacked! Player HP decreased.")