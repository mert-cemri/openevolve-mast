'''
Handles the creation and extraction of ZIP archives.
'''
import os
import zipfile
from pathlib import Path
class Archiver:
    def add_to_zip(self, zip_path, files):
        try:
            with zipfile.ZipFile(zip_path, 'a') as zipf:
                for file in files:
                    if os.path.isfile(file):
                        zipf.write(file, os.path.basename(file))
                    elif os.path.isdir(file):
                        for root, _, filenames in os.walk(file):
                            for filename in filenames:
                                file_path = os.path.join(root, filename)
                                arcname = os.path.relpath(file_path, start=os.path.dirname(file))
                                zipf.write(file_path, arcname)
        except Exception as e:
            raise Exception(f"Error adding files to ZIP archive: {e}")
    def extract_zip(self, zip_path, extract_to):
        try:
            if not os.path.exists(extract_to):
                os.makedirs(extract_to)
            elif not os.path.isdir(extract_to):
                raise ValueError(f"The specified extract path '{extract_to}' is not a directory.")
            elif not os.access(extract_to, os.W_OK):
                raise PermissionError(f"The specified extract path '{extract_to}' is not writable.")
            with zipfile.ZipFile(zip_path, 'r') as zipf:
                zipf.extractall(extract_to)
        except Exception as e:
            raise Exception(f"Error extracting ZIP archive: {e}")