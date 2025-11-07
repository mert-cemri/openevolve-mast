# log_rotator.py
import os
import shutil
import datetime
class LogRotator:
    def __init__(self, log_file, compress, delete):
        self.log_file = log_file
        self.compress = compress
        self.delete = delete
    def rotate_log(self):
        # Rename the log file
        new_log_file = self.log_file + '.1'
        os.rename(self.log_file, new_log_file)
        # Create a new empty log file
        with open(self.log_file, 'w') as f:
            pass
        # Compress the old log file
        if self.compress:
            shutil.make_archive(new_log_file, 'zip', new_log_file)
            # Create a directory for the compressed log file
            os.mkdir(new_log_file)
            # Move the compressed log file to the directory
            shutil.move(new_log_file + '.zip', new_log_file)
        # Delete old log files
        if self.delete:
            for file in os.listdir(os.path.dirname(self.log_file)):
                if file.startswith(os.path.basename(self.log_file)) and file != self.log_file:
                    os.remove(file)