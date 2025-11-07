'''
FileWatcher class to monitor file system changes using watchdog.
'''
from watchdog.observers import Observer
from event_handler import EventHandler
import time
class FileWatcher:
    def __init__(self, path):
        '''
        Initializes the FileWatcher with the specified path.
        :param path: Path to the directory or file to monitor.
        '''
        self.path = path
        self.observer = Observer()
        self.event_handler = EventHandler()
    def start(self):
        '''
        Starts the file monitoring process.
        '''
        self.observer.schedule(self.event_handler, self.path, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()
    def stop(self):
        '''
        Stops the file monitoring process.
        '''
        self.observer.stop()
        self.observer.join()