'''
Level class that manages the level state and objectives.
'''
class Level:
    def __init__(self):
        self.time_remaining = 60
        self.score = 0
        self.target_score = 100
    def check_completion(self):
        return self.time_remaining <= 0 or self.score >= self.target_score
    def update_timer(self):
        self.time_remaining -= 1 / 60