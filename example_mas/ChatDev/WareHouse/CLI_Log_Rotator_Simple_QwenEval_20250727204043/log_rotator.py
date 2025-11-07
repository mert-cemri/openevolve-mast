'''
Log Rotator module to handle the core functionality of renaming, compressing, and deleting log files.
'''
import os
import shutil
import gzip
import time
class LogRotator:
    def __init__(self, log_file, compress=False, delete_older_than=None):
        '''
        Initialize the LogRotator with the log file path, compression flag, and deletion threshold.
        '''
        self.log_file = log_file
        self.compress = compress
        self.delete_older_than = delete_older_than
    def rotate_logs(self):
        '''
        Perform the log rotation by renaming the current log file, creating a new empty log file,
        optionally compressing the old log file, and deleting old log files if specified.
        '''
        if not os.path.exists(self.log_file):
            raise FileNotFoundError(f"Log file {self.log_file} not found.")
        self.rename_log()
        self.create_new_log()
        if self.compress:
            self.compress_log(self.log_file + ".1")
        if self.delete_older_than is not None and self.delete_older_than > 0:
            self.delete_old_logs()
    def rename_log(self):
        '''
        Rename the current log file by appending '.1' to its name.
        If a file with the new name already exists, it will be deleted.
        '''
        new_log_file = self.log_file + ".1"
        if os.path.exists(new_log_file):
            os.remove(new_log_file)
        os.rename(self.log_file, new_log_file)
    def create_new_log(self):
        '''
        Create a new empty log file with the original name.
        '''
        with open(self.log_file, 'w') as f:
            pass
    def compress_log(self, old_log):
        '''
        Compress the specified old log file using gzip and remove the original file.
        '''
        try:
            with open(old_log, 'rb') as f_in:
                with gzip.open(old_log + '.gz', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            os.remove(old_log)
        except Exception as e:
            print(f"Error compressing log file {old_log}: {e}")
    def delete_old_logs(self):
        '''
        Delete log files that are older than the specified number of days.
        Consider both compressed log files (with '.gz' extension) and numbered backup files (e.g., '.1', '.2', etc.).
        '''
        now = time.time()
        base_name = os.path.splitext(self.log_file)[0]
        for filename in os.listdir('.'):
            if filename.startswith(base_name) and (filename.endswith('.gz') or filename.endswith('.1')):
                file_path = os.path.join('.', filename)
                if os.stat(file_path).st_mtime < now - self.delete_older_than * 86400:
                    os.remove(file_path)