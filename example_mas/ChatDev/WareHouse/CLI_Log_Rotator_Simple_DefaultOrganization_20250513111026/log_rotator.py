'''
LogRotator class handles log file rotation, compression, and deletion.
'''
import os
import shutil
import gzip
from datetime import datetime, timedelta
class LogRotator:
    def __init__(self, log_file):
        self.log_file = log_file
    def rotate_log(self):
        if os.path.exists(self.log_file):
            new_log_file = f"{self.log_file}.1"
            os.rename(self.log_file, new_log_file)
            print(f"Rotated log file: {self.log_file} to {new_log_file}")
        # Ensure a new empty log file is created
        open(self.log_file, 'w').close()
        print(f"Created new empty log file: {self.log_file}")
    def compress_logs(self):
        log_files = [f for f in os.listdir('.') if f.startswith(self.log_file) and f != self.log_file and not f.endswith('.gz')]
        for log in log_files:
            with open(log, 'rb') as f_in:
                with gzip.open(f"{log}.gz", 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            os.remove(log)
            print(f"Compressed log file: {log}")
    def delete_old_logs(self, days):
        cutoff_date = datetime.now() - timedelta(days=days)
        log_files = [f for f in os.listdir('.') if f.startswith(self.log_file) and (f.endswith('.gz') or f.endswith('.1'))]
        for log in log_files:
            file_time = datetime.fromtimestamp(os.path.getmtime(log))
            if file_time < cutoff_date:
                os.remove(log)
                print(f"Deleted old log file: {log}")