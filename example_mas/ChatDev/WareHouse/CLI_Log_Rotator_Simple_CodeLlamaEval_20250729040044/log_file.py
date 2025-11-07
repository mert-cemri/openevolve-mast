# log_file.py
import os
import logging
class LogFile:
    def __init__(self, log_file):
        self.log_file = log_file
    def write(self, message):
        with open(self.log_file, 'a') as f:
            f.write(message + '\n')
    def read(self):
        with open(self.log_file, 'r') as f:
            return f.read()
    def delete(self):
        os.remove(self.log_file)