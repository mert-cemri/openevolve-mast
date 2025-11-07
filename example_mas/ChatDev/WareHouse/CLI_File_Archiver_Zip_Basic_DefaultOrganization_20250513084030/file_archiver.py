'''
FileArchiver class for handling ZIP archive creation and extraction.
'''
import zipfile
import os
class FileArchiver:
    def create_zip(self, archive_name, files):
        '''
        Create a ZIP archive with the specified files/directories.
        :param archive_name: Name of the archive to create.
        :param files: List of file paths to include in the archive.
        '''
        with zipfile.ZipFile(archive_name, 'w') as zipf:
            for file in files:
                if os.path.isdir(file):
                    for foldername, subfolders, filenames in os.walk(file):
                        for filename in filenames:
                            file_path = os.path.join(foldername, filename)
                            zipf.write(file_path, os.path.relpath(file_path, os.path.dirname(file)))
                else:
                    zipf.write(file, os.path.basename(file))
    def extract_zip(self, archive_name, extract_to):
        '''
        Extract contents of a ZIP archive to a specified directory.
        :param archive_name: Name of the archive to extract.
        :param extract_to: Directory to extract files to.
        '''
        with zipfile.ZipFile(archive_name, 'r') as zipf:
            zipf.extractall(extract_to)