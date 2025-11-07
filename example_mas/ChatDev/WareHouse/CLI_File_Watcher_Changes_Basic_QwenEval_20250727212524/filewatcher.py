'''
FileWatcher class to monitor file or directory changes.
Uses the watchdog library to handle file system events.
'''
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
class FileWatcher(FileSystemEventHandler):
    def __init__(self, path, callback):
        self.path = path
        self.callback = callback
        self.observer = Observer()
    def start(self):
        self.observer.schedule(self, self.path, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()
    def stop(self):
        self.observer.stop()
        self.observer.join()
    def on_modified(self, event):
        self.callback(f"File {event.src_path} has been modified")
    def on_created(self, event):
        self.callback(f"File {event.src_path} has been created")
    def on_deleted(self, event):
        self.callback(f"File {event.src_path} has been deleted")