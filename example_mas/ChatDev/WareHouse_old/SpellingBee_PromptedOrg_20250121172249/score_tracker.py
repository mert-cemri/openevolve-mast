'''
DOCSTRING: Tracks and calculates scores based on the length of valid words.
'''
class ScoreTracker:
    def __init__(self):
        self.total_score = 0
    def calculate_score(self, word):
        score = len(word)  # Simple scoring: 1 point per letter
        self.total_score += score
        return score