'''
DiskAnalyzer class to handle the disk space analysis.
'''
import os
from file import File
from folder import Folder
from utils import human_readable_size
class DiskAnalyzer:
    def __init__(self, directory):
        self.directory = directory
        self.files = []
        self.folders = []
        self.total_size = 0
        self.size_cache = {}
    def analyze(self):
        self._analyze_directory(self.directory)
    def _analyze_directory(self, path):
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isfile(full_path):
                file = File(full_path)
                self.files.append(file)
                self.total_size += file.size()
            elif os.path.isdir(full_path):
                folder = Folder(full_path, self)
                self.folders.append(folder)
                folder_size = self._get_folder_size(full_path)
                self.total_size += folder_size
    def _get_folder_size(self, path):
        if path in self.size_cache:
            return self.size_cache[path]
        total_size = 0
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isfile(full_path):
                total_size += os.path.getsize(full_path)
            elif os.path.isdir(full_path):
                total_size += self._get_folder_size(full_path)
        self.size_cache[path] = total_size
        return total_size
    def get_largest_files(self, limit=10):
        return sorted(self.files, key=lambda x: x.size(), reverse=True)[:limit]
    def get_largest_folders(self, limit=10):
        return sorted(self.folders, key=lambda x: x.size(), reverse=True)[:limit]
    def print_report(self):
        print(f"Total size: {human_readable_size(self.total_size)}")
        print("\nLargest Files:")
        for file in self.get_largest_files():
            print(f"{file.path}: {human_readable_size(file.size())}")
        print("\nLargest Folders:")
        for folder in self.get_largest_folders():
            print(f"{folder.path}: {human_readable_size(folder.size())}")