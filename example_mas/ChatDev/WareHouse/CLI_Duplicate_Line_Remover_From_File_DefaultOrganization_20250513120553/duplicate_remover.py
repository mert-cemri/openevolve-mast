'''
Module to remove duplicate lines from a text file.
'''
class DuplicateRemover:
    def remove_duplicates(self, file_path):
        seen = set()
        result = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    if line not in seen:
                        seen.add(line)
                        result.append(line)
            return ''.join(result)
        except FileNotFoundError:
            return f"Error: The file {file_path} does not exist."
        except IOError as e:
            return f"Error: An I/O error occurred. {str(e)}"