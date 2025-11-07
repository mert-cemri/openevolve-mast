'''
FileHandler module to handle file operations.
'''
class FileHandler:
    @staticmethod
    def read_file(file_path):
        '''
        Reads the content of the given file and returns it as a string.
        :param file_path: Path to the text file.
        :return: Content of the file as a string.
        '''
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found. Please ensure the file exists in the correct directory.")
            return ""