'''
Handles the CLI aspects of the Pomodoro Timer application.
'''
from pomodoro_timer import PomodoroTimer
from notification import Notification
import sys
import argparse
import time
class TimerApp:
    def __init__(self, work_duration=25, break_duration=5):
        '''
        Initializes the TimerApp with specified work and break durations.
        '''
        self.timer = PomodoroTimer(work_duration, break_duration)
        self.timer.on_update = self.update_timer_label
        self.timer.on_complete = self.on_timer_complete
        self.is_running = False
    def run(self):
        '''
        Runs the Pomodoro Timer CLI, accepting user commands.
        '''
        print("Pomodoro Timer CLI")
        print("Commands: start, stop, reset, exit")
        while True:
            command = input("Enter command: ").strip().lower()
            if command == "start":
                if not self.is_running:
                    self.start_timer()
                else:
                    print("Timer is already running.")
            elif command == "stop":
                self.stop_timer()
            elif command == "reset":
                self.reset_timer()
            elif command == "exit":
                break
            else:
                print("Invalid command. Please try again.")
    def start_timer(self):
        '''
        Starts the Pomodoro timer.
        '''
        self.timer.start()
        self.is_running = True
        print("Timer started.")
    def stop_timer(self):
        '''
        Stops the Pomodoro timer.
        '''
        self.timer.stop()
        self.is_running = False
        print("Timer stopped.")
    def reset_timer(self):
        '''
        Resets the Pomodoro timer.
        '''
        self.timer.reset()
        self.is_running = False
        print("Timer reset.")
    def update_timer_label(self, remaining):
        '''
        Updates the timer label in the CLI.
        '''
        minutes, seconds = divmod(remaining, 60)
        print(f"Time remaining: {minutes:02}:{seconds:02}", end="\r")
    def on_timer_complete(self, is_break):
        '''
        Handles the completion of a work or break session.
        '''
        message = "Break time!" if is_break else "Work time!"
        Notification.show(message)
        print(message)
def main():
    '''
    Main function to parse command-line arguments and run the TimerApp.
    '''
    parser = argparse.ArgumentParser(description="Pomodoro Timer CLI")
    parser.add_argument("--work", type=int, default=25, help="Work duration in minutes (default: 25)")
    parser.add_argument("--break", type=int, default=5, help="Break duration in minutes (default: 5)")
    args = parser.parse_args()
    app = TimerApp(args.work, args.break)
    app.run()
if __name__ == "__main__":
    main()