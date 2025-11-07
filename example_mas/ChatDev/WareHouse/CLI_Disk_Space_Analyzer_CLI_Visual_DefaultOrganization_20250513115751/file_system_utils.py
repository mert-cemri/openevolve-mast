'''
Utility functions for file system operations.
'''
import os
class FileSystemUtils:
    @staticmethod
    def get_directory_size(directory):
        if not os.path.exists(directory):
            raise ValueError(f"The directory {directory} does not exist.")
        usage_data = {}
        error_count = 0
        for dirpath, dirnames, filenames in os.walk(directory):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                try:
                    size = os.path.getsize(fp)
                    usage_data[fp] = size
                except OSError as e:
                    error_count += 1
                    print(f"Error accessing {fp}: {e}")
        if error_count > 0:
            print(f"Encountered errors accessing {error_count} files.")
        return usage_data