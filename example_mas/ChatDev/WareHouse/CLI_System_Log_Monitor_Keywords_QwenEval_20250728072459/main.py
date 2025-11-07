'''
Main entry point for the Log Monitor application.
This file initializes the CLI and starts the application.
'''
import re
import subprocess
import sys
import threading
class LogMonitor:
    def __init__(self, log_file, keywords):
        '''
        Initialize the LogMonitor with the log file path and keywords.
        '''
        self.log_file = log_file
        self.keywords = [re.escape(keyword) for keyword in keywords]  # Escape special characters in keywords
        self.process = None
    def start(self):
        '''
        Start tailing the log file and reading logs in a separate thread.
        '''
        try:
            self.process = subprocess.Popen(['tail', '-f', self.log_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            threading.Thread(target=self.read_logs).start()
        except Exception as e:
            print(f"Error starting subprocess: {e}")
            sys.exit(1)
    def read_logs(self):
        '''
        Continuously read lines from the log file and highlight keywords.
        '''
        try:
            while True:
                line = self.process.stdout.readline()
                if not line:
                    break
                self.highlight_keywords(line)
        except KeyboardInterrupt:
            print("\nLog monitoring stopped by user.")
            self.stop()
        except Exception as e:
            print(f"Error reading logs: {e}")
            self.stop()
    def highlight_keywords(self, line):
        '''
        Highlight lines containing any of the specified keywords.
        '''
        for keyword in self.keywords:
            if re.search(keyword, line, re.IGNORECASE):
                print(f"\033[1;31m{line}\033[0m", end='')  # Highlight in red
                break
        else:
            print(line, end='')
    def stop(self):
        '''
        Stop the log monitoring process.
        '''
        if self.process:
            try:
                self.process.terminate()
                self.process.wait(timeout=5)  # Wait for the process to terminate
            except subprocess.TimeoutExpired:
                self.process.kill()  # Force kill if it doesn't terminate in time
            except Exception as e:
                print(f"Error stopping subprocess: {e}")
def main():
    '''
    Main function to parse command line arguments and start the log monitor.
    '''
    if len(sys.argv) < 3:
        print("Usage: python main.py <log_file_path> <keyword1,keyword2,...>")
        sys.exit(1)
    log_file = sys.argv[1]
    keywords = sys.argv[2].split(',')
    log_monitor = LogMonitor(log_file, keywords)
    log_monitor.start()
if __name__ == "__main__":
    main()