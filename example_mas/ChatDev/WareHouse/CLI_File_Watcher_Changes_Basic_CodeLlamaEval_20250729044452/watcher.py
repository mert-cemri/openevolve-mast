import os
import time
class FileWatcher:
    def __init__(self, path):
        self.path = path
        self.last_modified = None
    def start(self):
        self.last_modified = os.path.getmtime(self.path)
        self.thread = Thread(target=self.watch)
        self.thread.start()
    def watch(self):
        while True:
            try:
                current_modified = os.path.getmtime(self.path)
            except OSError:
                # File or directory does not exist
                return
            if current_modified != self.last_modified:
                self.last_modified = current_modified
                self.event_queue.put(Event(self.path, 'modified'))
                print(f'{self.path} modified')
            time.sleep(1)
    def stop(self):
        self.thread.join()
    def get_event(self):
        try:
            return self.event_queue.get(block=False)
        except Empty:
            return None