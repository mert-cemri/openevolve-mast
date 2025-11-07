'''
Score class for managing the game score.
'''
class Score:
    def __init__(self):
        self.points = 0
    def add_points(self, lines_cleared):
        self.points += lines_cleared * 100
    def get_score(self):
        return self.points