'''
Logic for analyzing disk usage within a directory.
'''
import os
from humanize import naturalsize
class DiskAnalyzer:
    def __init__(self):
        self.items = []
    def analyze_directory(self, path):
        self.items = []
        for root, dirs, files in os.walk(path):
            for name in files:
                filepath = os.path.join(root, name)
                try:
                    size = os.path.getsize(filepath)
                    self.items.append({'path': filepath, 'size': size})
                except OSError as e:
                    print(f"Error accessing {filepath}: {e}")
            for name in dirs:
                dirpath = os.path.join(root, name)
                try:
                    size = self.get_directory_size(dirpath)
                    self.items.append({'path': dirpath, 'size': size})
                except OSError as e:
                    print(f"Error accessing {dirpath}: {e}")
    def get_directory_size(self, path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                try:
                    total_size += os.path.getsize(fp)
                except OSError as e:
                    print(f"Error accessing {fp}: {e}")
        return total_size
    def get_largest_items(self, n):
        sorted_items = sorted(self.items, key=lambda x: x['size'], reverse=True)
        return [{'path': item['path'], 'size': naturalsize(item['size'])} for item in sorted_items[:n]]