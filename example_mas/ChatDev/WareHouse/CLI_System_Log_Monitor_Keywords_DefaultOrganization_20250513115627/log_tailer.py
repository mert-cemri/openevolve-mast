'''
Handles the tailing of log files.
'''
import threading
import time
class LogTailer:
    def __init__(self, filepath, callback):
        self.filepath = filepath
        self.callback = callback
        self.running = False
        self.thread = None
    def tail(self):
        self.running = True
        self.thread = threading.Thread(target=self._run)
        self.thread.start()
    def _run(self):
        with open(self.filepath, 'r') as file:
            file.seek(0, 2)  # Move to the end of the file
            while self.running:
                line = file.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                self.callback(line)
    def stop(self):
        self.running = False
        if self.thread is not None:
            self.thread.join()