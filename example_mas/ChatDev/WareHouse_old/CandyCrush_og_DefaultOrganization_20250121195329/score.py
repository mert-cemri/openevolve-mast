'''
Score class tracks and updates the player's score.
'''
class Score:
    def __init__(self):
        self.points = 0
    def add_points(self, amount):
        self.points += amount
    def reset(self):
        self.points = 0