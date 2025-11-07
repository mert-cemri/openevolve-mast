'''
Contains the PomodoroApp class for managing the CLI components.
'''
from timer import PomodoroTimer
from config import WORK_DURATION, BREAK_DURATION
class PomodoroApp:
    def __init__(self):
        self.timer = PomodoroTimer(WORK_DURATION, BREAK_DURATION, self.update_timer_display, self.notify_user)
    def start_timer(self):
        self.timer.start_timer()
    def reset_timer(self):
        self.timer.reset_timer()
        if self.timer.is_work_session:
            self.update_timer_display(f"{self.timer.work_duration // 60:02d}:00")
        else:
            self.update_timer_display(f"{self.timer.break_duration // 60:02d}:00")
    def update_timer_display(self, time_str):
        print(f"Timer: {time_str}")
    def notify_user(self):
        print("Time's up! Take a break or start a new session.")
    def run(self):
        while True:
            command = input("Enter 'start' to begin the timer or 'reset' to reset it: ").strip().lower()
            if command == 'start':
                self.start_timer()
            elif command == 'reset':
                self.reset_timer()
            else:
                print("Invalid command. Please enter 'start' or 'reset'.")