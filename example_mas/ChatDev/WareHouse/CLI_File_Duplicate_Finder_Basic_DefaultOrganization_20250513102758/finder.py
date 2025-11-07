'''
Contains the DuplicateFileFinder class which implements the logic to find duplicate files.
'''
import os
import hashlib
class DuplicateFileFinder:
    def __init__(self, hash_algorithm='md5'):
        self.hash_algorithm = hash_algorithm
    def compute_hash(self, file_path):
        '''Computes the hash of a file using the specified hash algorithm.'''
        hash_func = hashlib.new(self.hash_algorithm)
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    def find_duplicates(self, directory):
        '''Finds and returns a list of duplicate files in the specified directory.'''
        hashes = {}
        duplicates = []
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = self.compute_hash(file_path)
                if file_hash in hashes:
                    duplicates.append((file_path, hashes[file_hash]))
                else:
                    hashes[file_hash] = file_path
        return duplicates