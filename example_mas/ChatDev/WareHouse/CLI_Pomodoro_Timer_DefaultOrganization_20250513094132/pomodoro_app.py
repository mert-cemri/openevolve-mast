'''
Defines the PomodoroApp class which manages the CLI interaction.
'''
from pomodoro_timer import PomodoroTimer
from notification_manager import NotificationManager
import time
import threading
class PomodoroApp:
    def __init__(self):
        self.timer = PomodoroTimer()
        self.notification_manager = NotificationManager()
        self.timer_thread = None
    def start_timer(self):
        if not self.timer.is_running:
            self.timer.start()
            self.timer_thread = threading.Thread(target=self.update_clock)
            self.timer_thread.start()
    def stop_timer(self):
        self.timer.stop()
        if self.timer_thread and self.timer_thread.is_alive():
            self.timer_thread.join()
    def reset_timer(self):
        self.timer.reset()
        if self.timer_thread and self.timer_thread.is_alive():
            self.timer_thread.join()
    def update_clock(self):
        while self.timer.is_running:
            if self.timer.tick():
                session_type = "Work Session" if self.timer.is_work() else "Break Session"
                self.notification_manager.notify(session_type)
            print(f"Time Remaining: {self.timer.get_time()}", end='\r')
            time.sleep(1)
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
                print("Unknown command. Please enter 'start', 'stop', 'reset', or 'exit'.")