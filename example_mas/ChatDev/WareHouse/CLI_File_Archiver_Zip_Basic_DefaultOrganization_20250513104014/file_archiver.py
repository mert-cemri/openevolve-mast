'''
Handles ZIP file operations such as creating and extracting archives.
'''
import zipfile
import os
class FileArchiver:
    def create_zip(self, zip_name, files):
        '''
        Creates a ZIP archive with the specified files.
        :param zip_name: Name of the ZIP file to create.
        :param files: List of file paths to include in the ZIP.
        '''
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            for file in files:
                if os.path.isdir(file):
                    for foldername, subfolders, filenames in os.walk(file):
                        for filename in filenames:
                            file_path = os.path.join(foldername, filename)
                            zipf.write(file_path, os.path.relpath(file_path, os.path.dirname(file)))
                else:
                    zipf.write(file, os.path.basename(file))
    def extract_zip(self, zip_name, extract_to):
        '''
        Extracts the contents of a ZIP archive to a specified directory.
        :param zip_name: Name of the ZIP file to extract.
        :param extract_to: Directory to extract files to.
        '''
        with zipfile.ZipFile(zip_name, 'r') as zipf:
            zipf.extractall(extract_to)