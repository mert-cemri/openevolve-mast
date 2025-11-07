# log_compressor.py
import shutil
class LogCompressor:
    def __init__(self, log_file):
        self.log_file = log_file
    def compress(self):
        # Compress the log file using the zip command
        os.system('zip -r {}.zip {}'.format(self.log_file, self.log_file))