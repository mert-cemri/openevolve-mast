'''
Handles file operations.
'''
class FileHandler:
    def read_file(self, file_path):
        '''
        Reads the contents of a file and returns the lines as a list.
        Parameters:
        file_path (str): The path to the file to be read.
        Returns:
        list of str: The lines of the file.
        '''
        with open(file_path, 'r') as file:
            return file.readlines()
    def write_file(self, file_path, lines):
        '''
        Writes a list of lines to a file.
        Parameters:
        file_path (str): The path to the file to be written.
        lines (list of str): The lines to be written to the file.
        '''
        with open(file_path, 'w') as file:
            file.writelines(lines)