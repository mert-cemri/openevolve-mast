'''
DataLoader class to handle data loading from files or standard input.
'''
import sys
class DataLoader:
    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = [float(line.strip()) for line in file]
        return data
    def load_from_stdin(self):
        print("Enter numbers separated by newlines (end input with Ctrl+D):")
        data = [float(line.strip()) for line in sys.stdin]
        return data