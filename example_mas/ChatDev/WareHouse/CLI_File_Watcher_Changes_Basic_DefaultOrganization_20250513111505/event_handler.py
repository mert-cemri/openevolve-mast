'''
Defines the EventHandler class to handle file system events.
'''
from watchdog.events import FileSystemEventHandler
class EventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"File created: {event.src_path}")
    def on_modified(self, event):
        print(f"File modified: {event.src_path}")
    def on_deleted(self, event):
        print(f"File deleted: {event.src_path}")