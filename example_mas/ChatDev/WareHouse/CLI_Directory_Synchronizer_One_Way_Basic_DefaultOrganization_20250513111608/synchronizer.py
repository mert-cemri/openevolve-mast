'''
Contains the DirectorySynchronizer class for synchronizing directories.
'''
import os
import shutil
class DirectorySynchronizer:
    def synchronize(self, source, target):
        try:
            if not os.path.exists(target):
                os.makedirs(target)
            for root, dirs, files in os.walk(source):
                relative_path = os.path.relpath(root, source)
                target_path = os.path.join(target, relative_path)
                if not os.path.exists(target_path):
                    os.makedirs(target_path)
                for file in files:
                    source_file = os.path.join(root, file)
                    target_file = os.path.join(target_path, file)
                    if not os.path.exists(target_file) or os.path.getmtime(source_file) > os.path.getmtime(target_file):
                        shutil.copy2(source_file, target_file)
        except OSError as e:
            raise RuntimeError(f"OS error occurred during synchronization: {e}")
        except shutil.Error as e:
            raise RuntimeError(f"Shutil error occurred during synchronization: {e}")