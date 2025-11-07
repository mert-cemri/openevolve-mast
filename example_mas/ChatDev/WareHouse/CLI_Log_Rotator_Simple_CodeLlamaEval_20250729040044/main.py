# main.py
import os
import shutil
import datetime
import logging
from log_rotator import LogRotator
from log_file import LogFile
from log_compressor import LogCompressor
from log_deleter import LogDeleter
def main():
    log_file = 'app.log'
    compress = True
    delete = True
    log_rotator = LogRotator(log_file, compress, delete)
    log_rotator.rotate_log()
    log_file = LogFile(log_file)
    log_file.write('This is a test message')
    log_file.read()
    log_file.delete()
    log_compressor = LogCompressor(log_file)
    log_compressor.compress()
    log_deleter = LogDeleter(log_file)
    log_deleter.delete()
if __name__ == '__main__':
    main()