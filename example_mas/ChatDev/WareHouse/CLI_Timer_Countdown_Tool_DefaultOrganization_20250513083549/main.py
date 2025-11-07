'''
Main application file for the CLI timer and countdown tool.
'''
import argparse
import time
from timer import Timer
from countdown import Countdown
def main():
    parser = argparse.ArgumentParser(description="CLI Timer and Countdown Tool")
    parser.add_argument('--timer', action='store_true', help="Start a timer that counts up from zero")
    parser.add_argument('--countdown', type=str, help="Start a countdown with a specified duration (e.g., 5m, 1h30s)")
    args = parser.parse_args()
    if args.timer:
        timer = Timer()
        timer.start()
        try:
            while True:
                print(f"Timer: {timer.get_time()}", end='\r')
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nTimer stopped.")
    elif args.countdown:
        countdown = Countdown()
        duration = parse_duration(args.countdown)
        if duration is not None:
            countdown.start(duration)
            try:
                while countdown.running:
                    print(f"Countdown: {countdown.get_time()}", end='\r')
                    time.sleep(1)
                print("\nCountdown finished.")
            except KeyboardInterrupt:
                print("\nCountdown stopped.")
        else:
            print("Failed to start countdown due to invalid duration format.")
def parse_duration(duration_str):
    total_seconds = 0
    try:
        if 'h' in duration_str:
            hours, duration_str = duration_str.split('h')
            total_seconds += int(hours) * 3600
        if 'm' in duration_str:
            minutes, duration_str = duration_str.split('m')
            total_seconds += int(minutes) * 60
        if 's' in duration_str:
            seconds = duration_str.replace('s', '')
            total_seconds += int(seconds)
        return total_seconds
    except ValueError:
        print("Invalid duration format. Please use a format like '1h30m20s'.")
        return None
if __name__ == "__main__":
    main()