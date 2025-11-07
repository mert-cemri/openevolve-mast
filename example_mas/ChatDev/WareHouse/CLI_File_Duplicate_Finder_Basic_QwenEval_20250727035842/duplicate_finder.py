'''
Module containing the DuplicateFinder class for finding duplicate files.
'''
class DuplicateFinder:
    def __init__(self, file_hashes):
        self.file_hashes = file_hashes
    def find_duplicates(self):
        '''Find and group duplicate files.'''
        duplicates = {hash_value: paths for hash_value, paths in self.file_hashes.items() if len(paths) > 1}
        return duplicates