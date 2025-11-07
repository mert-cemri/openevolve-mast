'''
Module to calculate MD5 and SHA256 checksums of a file.
'''
import hashlib
class ChecksumCalculator:
    def calculate_md5(self, file_path):
        '''
        Calculate the MD5 checksum of the given file.
        :param file_path: Path to the file.
        :return: MD5 checksum as a hexadecimal string.
        '''
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    def calculate_sha256(self, file_path):
        '''
        Calculate the SHA256 checksum of the given file.
        :param file_path: Path to the file.
        :return: SHA256 checksum as a hexadecimal string.
        '''
        hash_sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()