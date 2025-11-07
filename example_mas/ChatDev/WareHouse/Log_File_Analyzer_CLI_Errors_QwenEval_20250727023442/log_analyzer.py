'''
LogAnalyzer class for reading log files, searching for patterns, and counting occurrences.
'''
class LogAnalyzer:
    def __init__(self, log_file, pattern):
        self.log_file = log_file
        self.pattern = pattern
    def count_pattern(self):
        count = 0
        try:
            with open(self.log_file, 'r') as file:
                for line in file:
                    if self.pattern in line:
                        count += 1
        except FileNotFoundError:
            print(f"Error: The file '{self.log_file}' was not found.")
        except PermissionError:
            print(f"Error: Permission denied when trying to read the file '{self.log_file}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return count