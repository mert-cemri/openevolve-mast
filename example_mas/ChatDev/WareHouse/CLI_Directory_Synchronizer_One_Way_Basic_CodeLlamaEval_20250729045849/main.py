import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
class FileSyncHandler(FileSystemEventHandler):
    def __init__(self, source_dir, target_dir):
        self.source_dir = source_dir
        self.target_dir = target_dir
    def on_created(self, event):
        if event.is_directory:
            return None
        # Ignore hidden files and directories
        if event.src_path.startswith('.'):
            return None
        self._copy_file(event.src_path, self.target_dir)
    def on_modified(self, event):
        if event.is_directory:
            return None
        # Ignore hidden files and directories
        if event.src_path.startswith('.'):
            return None
        self._copy_file(event.src_path, self.target_dir)
    def on_deleted(self, event):
        if event.is_directory:
            return None
        # Ignore hidden files and directories
        if event.src_path.startswith('.'):
            return None
        self._delete_file(event.src_path, self.target_dir)
    def _copy_file(self, src_path, dst_path):
        dst_path = os.path.join(dst_path, os.path.basename(src_path))
        shutil.copyfile(src_path, dst_path)
    def _delete_file(self, src_path, dst_path):
        dst_path = os.path.join(dst_path, os.path.basename(src_path))
        os.remove(dst_path)
if __name__ == '__main__':
    source_dir = '/path/to/source/directory'
    target_dir = '/path/to/target/directory'
    event_handler = FileSyncHandler(source_dir, target_dir)
    observer = Observer()
    observer.schedule(event_handler, source_dir, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()