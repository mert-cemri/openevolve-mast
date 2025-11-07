'''
Log monitoring and processing logic.
'''
import threading
import time
class LogMonitor:
    def __init__(self, file_path, keywords, update_callback):
        self.file_path = file_path
        self.keywords = keywords
        self.update_callback = update_callback
        self.running = False
        self.thread = None
    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.tail_log)
        self.thread.start()
    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
    def tail_log(self):
        with open(self.file_path, 'r') as file:
            file.seek(0, 2)  # Move to the end of the file
            while self.running:
                line = file.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                if any(keyword in line for keyword in self.keywords):
                    self.update_callback(line.strip())