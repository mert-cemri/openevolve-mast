'''
Manages timing for the Typing Practice Game.
'''
import time
class Timer:
    def __init__(self):
        self.start_time = 0
    def start_timer(self):
        self.start_time = time.time()
    def stop_timer(self):
        return time.time() - self.start_time