'''
Countdown class for counting down from a specified duration.
'''
import time
class Countdown:
    def __init__(self):
        self.duration = 0
        self.end_time = None
        self.running = False
    def start(self, duration):
        self.duration = duration
        self.end_time = time.time() + duration
        self.running = True
    def stop(self):
        self.running = False
    def reset(self):
        self.duration = 0
        self.end_time = None
        self.running = False
    def get_time(self):
        if self.running:
            remaining_time = int(self.end_time - time.time())
            if remaining_time <= 0:
                self.running = False
                return "00:00:00"
            hours, remainder = divmod(remaining_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{hours:02}:{minutes:02}:{seconds:02}"
        return "00:00:00"