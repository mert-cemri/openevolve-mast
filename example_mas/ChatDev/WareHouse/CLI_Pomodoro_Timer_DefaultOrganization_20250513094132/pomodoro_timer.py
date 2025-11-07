'''
Defines the PomodoroTimer class which manages the timer logic.
'''
import time
class PomodoroTimer:
    def __init__(self, work_duration=25*60, break_duration=5*60):
        self.work_duration = work_duration
        self.break_duration = break_duration
        self.current_time = work_duration
        self.is_running = False
        self.is_work_session = True
    def start(self):
        self.is_running = True
    def stop(self):
        self.is_running = False
    def reset(self):
        self.is_running = False
        self.current_time = self.work_duration if self.is_work_session else self.break_duration
    def tick(self):
        if self.is_running:
            self.current_time -= 1
            if self.current_time <= 0:
                self.is_work_session = not self.is_work_session
                self.current_time = self.work_duration if self.is_work_session else self.break_duration
                return True
        return False
    def get_time(self):
        minutes, seconds = divmod(self.current_time, 60)
        return f"{minutes:02}:{seconds:02}"
    def is_work(self):
        return self.is_work_session