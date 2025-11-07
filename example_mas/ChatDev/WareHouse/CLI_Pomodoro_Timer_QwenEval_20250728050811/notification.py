'''
Handles the notification functionality when the timer completes a session or break.
'''
import os
import platform
class Notification:
    @staticmethod
    def show(message):
        '''
        Shows a notification based on the operating system.
        '''
        system = platform.system()
        if system == "Darwin":
            os.system(f"osascript -e 'display notification \"{message}\" with title \"Pomodoro Timer\"'")
        elif system == "Linux":
            os.system(f"notify-send 'Pomodoro Timer' '{message}'")
        elif system == "Windows":
            try:
                from plyer import notification
            except ImportError:
                print("Plyer library is not installed. Please install it using 'pip install plyer'.")
                return
            notification.notify(
                title='Pomodoro Timer',
                message=message,
                app_name='Pomodoro Timer',
                timeout=10
            )