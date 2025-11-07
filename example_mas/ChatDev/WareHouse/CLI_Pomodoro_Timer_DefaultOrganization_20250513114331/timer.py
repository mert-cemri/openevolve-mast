'''
Contains the PomodoroTimer class for managing the timer logic.
'''
import time
import threading
class PomodoroTimer:
    def __init__(self, work_duration, break_duration, update_callback, notify_callback):
        self.work_duration = work_duration
        self.break_duration = break_duration
        self.update_callback = update_callback
        self.notify_callback = notify_callback
        self.is_running = False
        self.current_time = 0
        self.timer_thread = None
        self.is_work_session = True
    def start_timer(self, is_work_session=True):
        self.is_running = True
        self.is_work_session = is_work_session
        self.current_time = self.work_duration if self.is_work_session else self.break_duration
        self.timer_thread = threading.Thread(target=self.countdown)
        self.timer_thread.start()
    def countdown(self):
        while self.current_time > 0 and self.is_running:
            mins, secs = divmod(self.current_time, 60)
            self.update_callback(f"{mins:02d}:{secs:02d}")
            time.sleep(1)
            self.current_time -= 1
        if self.is_running:
            self.notify_callback()
            self.start_timer(not self.is_work_session)
    def reset_timer(self):
        self.is_running = False
        if self.timer_thread and self.timer_thread.is_alive():
            self.timer_thread.join()
        self.current_time = 0