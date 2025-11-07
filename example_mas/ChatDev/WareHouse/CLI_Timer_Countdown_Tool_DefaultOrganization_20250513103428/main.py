'''
Main application file for the CLI timer and countdown tool.
'''
import argparse
import time
from time_converter import TimeConverter
def start_timer():
    seconds = 0
    try:
        while True:
            print(f"Timer: {format_time(seconds)}", end='\r')
            time.sleep(1)
            seconds += 1
    except KeyboardInterrupt:
        print("\nTimer stopped.")
def start_countdown(duration):
    countdown_seconds = TimeConverter.convert_to_seconds(duration)
    try:
        while countdown_seconds > 0:
            print(f"Countdown: {format_time(countdown_seconds)}", end='\r')
            time.sleep(1)
            countdown_seconds -= 1
        print("\nCountdown Complete!")
    except KeyboardInterrupt:
        print("\nCountdown stopped.")
def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI Timer and Countdown Tool")
    parser.add_argument('--timer', action='store_true', help="Start the timer")
    parser.add_argument('--countdown', type=str, help="Start the countdown with specified duration (e.g., 5m, 1h30s)")
    args = parser.parse_args()
    if args.timer:
        start_timer()
    elif args.countdown:
        start_countdown(args.countdown)
    else:
        print("Please specify --timer to start the timer or --countdown <duration> to start the countdown.")