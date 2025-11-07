'''
Timer class for counting up from zero.
'''
import time
class Timer:
    def __init__(self):
        self.start_time = None
        self.running = False
    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
    def stop(self):
        self.running = False
    def reset(self):
        self.start_time = None
        self.running = False
    def get_time(self):
        if self.running:
            elapsed_time = int(time.time() - self.start_time)
            hours, remainder = divmod(elapsed_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{hours:02}:{minutes:02}:{seconds:02}"
        return "00:00:00"