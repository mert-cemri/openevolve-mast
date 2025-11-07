'''
Level class to manage level state and goals.
'''
import time
class Level:
    def __init__(self, time_limit, goal):
        self.time_limit = time_limit
        self.goal = goal
        self.time_left = time_limit
        self.current_value = 0
        self.start_time = time.time()
    def check_time(self):
        elapsed_time = time.time() - self.start_time
        self.time_left = max(0, self.time_limit - int(elapsed_time))
        if self.time_left == 0:
            print("Time's up!")
    def check_goal(self):
        if self.current_value >= self.goal:
            print("Goal reached!")
            # Set a flag to stop the game
            return True
        return False
    def update_current_value(self, value):
        self.current_value += value
        print(f"Current Value: {self.current_value}")