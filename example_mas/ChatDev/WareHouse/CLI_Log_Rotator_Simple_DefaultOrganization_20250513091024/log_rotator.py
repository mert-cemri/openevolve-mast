'''
Module for log rotation functionality.
'''
import os
import shutil
import gzip
import time
from datetime import datetime, timedelta
class LogRotator:
    def __init__(self, log_file, compress=False, delete_days=None):
        self.log_file = log_file
        self.compress = compress
        self.delete_days = delete_days
    def rotate_log(self):
        if os.path.exists(self.log_file):
            # Rename the existing log file
            new_log_file = f"{self.log_file}.1"
            os.rename(self.log_file, new_log_file)
            # Create a new empty log file
            open(self.log_file, 'w').close()
            print(f"Rotated log: {self.log_file} to {new_log_file}")
    def compress_logs(self):
        if self.compress:
            for file in os.listdir('.'):
                # Ensure only rotated log files are compressed
                if file.startswith(f"{self.log_file}.") and file[len(self.log_file)+1:].isdigit() and not file.endswith('.gz'):
                    with open(file, 'rb') as f_in:
                        with gzip.open(f"{file}.gz", 'wb') as f_out:
                            shutil.copyfileobj(f_in, f_out)
                    os.remove(file)
                    print(f"Compressed log: {file}")
    def delete_old_logs(self):
        if self.delete_days is not None:
            cutoff_date = datetime.now() - timedelta(days=self.delete_days)
            for file in os.listdir('.'):
                if file.startswith(self.log_file) and file.endswith('.gz'):
                    file_time = datetime.fromtimestamp(os.path.getmtime(file))
                    if file_time < cutoff_date:
                        os.remove(file)
                        print(f"Deleted old log: {file}")
    def execute(self):
        self.rotate_log()
        self.compress_logs()
        self.delete_old_logs()