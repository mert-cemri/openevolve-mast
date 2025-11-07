'''
Module containing the FileHasher class for hashing file contents.
'''
import os
import hashlib
class FileHasher:
    def __init__(self, hash_type='sha256'):
        self.hash_type = hash_type
    def hash_file(self, file_path):
        '''Compute the hash of a file.'''
        hasher = hashlib.new(self.hash_type)
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    def hash_directory(self, directory_path):
        '''Compute hashes for all files in a directory.'''
        file_hashes = {}
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = self.hash_file(file_path)
                if file_hash in file_hashes:
                    file_hashes[file_hash].append(file_path)
                else:
                    file_hashes[file_hash] = [file_path]
        return file_hashes