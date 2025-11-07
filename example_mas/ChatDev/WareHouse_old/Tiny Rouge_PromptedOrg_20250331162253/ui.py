'''
UI class to handle the display of the player's current HP and monster stats.
'''
class UI:
    def __init__(self, player):
        self.player = player
    def display(self):
        print(f"Player HP: {self.player.hp}")