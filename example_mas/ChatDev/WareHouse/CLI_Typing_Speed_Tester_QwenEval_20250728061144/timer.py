'''
Contains the Timer class which is responsible for handling the timing of the typing test.
'''
import time
class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None
    def start(self):
        self.start_time = time.time()
    def stop(self):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time