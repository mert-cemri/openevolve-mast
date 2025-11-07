'''
EventHandler class to handle file system events.
'''
from watchdog.events import FileSystemEventHandler
class EventHandler(FileSystemEventHandler):
    def on_created(self, event):
        '''
        Handles file creation events.
        :param event: The event object containing event information.
        '''
        print(f"File created: {event.src_path}")
    def on_modified(self, event):
        '''
        Handles file modification events.
        :param event: The event object containing event information.
        '''
        print(f"File modified: {event.src_path}")
    def on_deleted(self, event):
        '''
        Handles file deletion events.
        :param event: The event object containing event information.
        '''
        print(f"File deleted: {event.src_path}")