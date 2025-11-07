'''
Contains the DirectorySizeCalculator class for calculating directory sizes.
'''
import os
import shutil
class DirectorySizeCalculator:
    def __init__(self, directory):
        '''
        Initialize the DirectorySizeCalculator with the directory path.
        '''
        self.directory = directory
    def calculate_size(self):
        '''
        Calculate the total size of the directory and its subdirectories.
        '''
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(self.directory):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # Skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
        return total_size
    def format_size(self, size):
        '''
        Convert the size in bytes to a human-readable format.
        '''
        return shutil.format_size(size)