'''
Defines the FileWatcher class to monitor file system changes using watchdog.
'''
from watchdog.observers import Observer
from event_handler import EventHandler
import time
class FileWatcher:
    def __init__(self, path):
        self.path = path
        self.observer = Observer()
    def start(self):
        event_handler = EventHandler()
        self.observer.schedule(event_handler, self.path, recursive=True)
        self.observer.start()
        print(f"Started monitoring {self.path}")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()
    def stop(self):
        self.observer.stop()
        self.observer.join()
        print(f"Stopped monitoring {self.path}")