'''
Defines the Monster class.
'''
class Monster:
    def __init__(self, position, hp):
        self.position = position
        self.hp = hp
    def attack(self, player):
        player.hp -= self.hp