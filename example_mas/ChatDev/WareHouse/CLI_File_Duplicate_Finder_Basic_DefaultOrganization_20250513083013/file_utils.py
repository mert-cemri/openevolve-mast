'''
Utility functions for file operations, including calculating MD5 hashes and finding duplicate files.
'''
import os
import hashlib
def calculate_md5(file_path):
    '''
    Calculate the MD5 hash of a file.
    :param file_path: Path to the file.
    :return: MD5 hash of the file.
    '''
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
def find_duplicate_files(directory):
    '''
    Find duplicate files in a directory based on their MD5 hash.
    :param directory: Directory to search for duplicate files.
    :return: List of lists containing paths of duplicate files.
    '''
    files_by_hash = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_md5(file_path)
            if file_hash in files_by_hash:
                files_by_hash[file_hash].append(file_path)
            else:
                files_by_hash[file_hash] = [file_path]
    duplicates = [files for files in files_by_hash.values() if len(files) > 1]
    return duplicates