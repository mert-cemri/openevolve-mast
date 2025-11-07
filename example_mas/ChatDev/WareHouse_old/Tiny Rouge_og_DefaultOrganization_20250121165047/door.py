'''
Defines the Door class.
'''
class Door:
    def __init__(self, position):
        self.position = position
    def enter(self, game):
        game.map.next_level()