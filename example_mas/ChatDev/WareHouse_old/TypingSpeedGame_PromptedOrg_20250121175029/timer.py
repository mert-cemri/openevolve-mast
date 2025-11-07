'''
Timer class to handle timing for the typing game.
'''
import time
class Timer:
    def __init__(self):
        self.start_time = 0
    def start(self):
        self.start_time = time.time()
    def stop(self):
        end_time = time.time()
        return end_time - self.start_time