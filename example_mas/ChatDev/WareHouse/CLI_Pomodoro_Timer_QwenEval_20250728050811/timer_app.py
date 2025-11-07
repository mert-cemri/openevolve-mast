'''
Handles the CLI aspects of the Pomodoro Timer application.
'''
from pomodoro_timer import PomodoroTimer
from notification import Notification
class TimerApp:
    def __init__(self):
        self.timer = PomodoroTimer()
        self.timer.on_update = self.update_timer_label
        self.timer.on_complete = self.on_timer_complete
    def run(self):
        print("Pomodoro Timer CLI")
        print("Commands: start, stop, reset, exit")
        while True:
            command = input("Enter command: ").strip().lower()
            if command == "start":
                self.start_timer()
            elif command == "stop":
                self.stop_timer()
            elif command == "reset":
                self.reset_timer()
            elif command == "exit":
                break
            else:
                print("Invalid command. Please try again.")
    def start_timer(self):
        self.timer.start()
        print("Timer started.")
    def stop_timer(self):
        self.timer.stop()
        print("Timer stopped.")
    def reset_timer(self):
        self.timer.reset()
        print("Timer reset.")
    def update_timer_label(self, remaining):
        minutes, seconds = divmod(remaining, 60)
        print(f"Time remaining: {minutes:02}:{seconds:02}", end="\r")
    def on_timer_complete(self, is_break):
        message = "Break time!" if is_break else "Work time!"
        Notification.show(message)
        print(message)