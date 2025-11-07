'''
Handles the core functionality of the Pomodoro timer.
'''
import time
from threading import Thread
class PomodoroTimer:
    def __init__(self, work_duration=25, break_duration=5):
        '''
        Initializes the PomodoroTimer with specified work and break durations.
        '''
        self.work_duration = work_duration
        self.break_duration = break_duration
        self.current_duration = work_duration
        self.is_running = False
        self.is_break = False
        self.on_update = None
        self.on_complete = None
    def start(self):
        '''
        Starts the timer in a separate thread.
        '''
        if not self.is_running:
            self.is_running = True
            self.thread = Thread(target=self._run_timer)
            self.thread.start()
    def stop(self):
        '''
        Stops the timer.
        '''
        self.is_running = False
    def reset(self):
        '''
        Resets the timer to the initial work duration.
        '''
        self.is_running = False
        self.is_break = False
        self.current_duration = self.work_duration
        if self.on_update:
            self.on_update(self.current_duration)
    def _run_timer(self):
        '''
        Internal method to run the timer.
        '''
        while self.is_running:
            time.sleep(1)
            self.current_duration -= 1
            if self.on_update:
                self.on_update(self.current_duration)
            if self.current_duration == 0:
                self.is_break = not self.is_break
                self.current_duration = self.break_duration if self.is_break else self.work_duration
                if self.on_complete:
                    self.on_complete(self.is_break)
                if self.on_update:
                    self.on_update(self.current_duration)