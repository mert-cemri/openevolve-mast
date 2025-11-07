# log_deleter.py
import os
class LogDeleter:
    def __init__(self, log_file):
        self.log_file = log_file
    def delete(self):
        os.remove(self.log_file)