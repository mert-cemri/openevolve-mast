'''
Handles the logic of splitting a file into smaller parts.
Provides a method to split a file into chunks of a specified size.
'''
import os
class FileSplitter:
    def __init__(self):
        pass
    def split_file(self, file_path, chunk_size):
        """
        Splits the file into chunks of the specified size.
        :param file_path: Path to the file to be split.
        :param chunk_size: Size of each chunk in bytes.
        """
        if not os.path.isfile(file_path):
            print(f"Error: The file '{file_path}' does not exist.")
            return
        try:
            with open(file_path, 'rb') as file:
                chunk_number = 1
                while True:
                    chunk = file.read(chunk_size)
                    if not chunk:
                        break
                    with open(f"{file_path}.part{chunk_number}", 'wb') as chunk_file:
                        chunk_file.write(chunk)
                    chunk_number += 1
            print("File has been split successfully.")
        except Exception as e:
            print(f"An error occurred while splitting the file: {e}")