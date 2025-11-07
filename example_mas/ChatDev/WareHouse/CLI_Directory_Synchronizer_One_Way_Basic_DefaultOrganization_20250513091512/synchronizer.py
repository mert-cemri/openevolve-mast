'''
Contains the logic for one-way directory synchronization.
'''
import os
import shutil
class DirectorySynchronizer:
    def __init__(self):
        '''
        Initializes the DirectorySynchronizer class.
        '''
        pass
    def synchronize(self, source, target):
        '''
        Synchronizes files from the source directory to the target directory.
        Only copies new or modified files. Does not delete files from the target.
        '''
        for root, _, files in os.walk(source):
            for file in files:
                source_file = os.path.join(root, file)
                relative_path = os.path.relpath(source_file, source)
                target_file = os.path.join(target, relative_path)
                # Create target directory if it doesn't exist
                os.makedirs(os.path.dirname(target_file), exist_ok=True)
                # Copy file if it doesn't exist in target or is modified
                if not os.path.exists(target_file) or os.path.getmtime(source_file) > os.path.getmtime(target_file):
                    shutil.copy2(source_file, target_file)