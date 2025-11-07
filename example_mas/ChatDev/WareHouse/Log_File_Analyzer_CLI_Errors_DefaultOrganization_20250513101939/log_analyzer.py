'''
Module to analyze log files and count lines containing a specific pattern.
'''
def analyze_log_file(file_path, pattern):
    '''
    Analyzes the log file and counts lines containing the specified pattern.
    :param file_path: Path to the log file.
    :param pattern: Pattern to search for in the log file.
    :return: Number of lines containing the pattern.
    '''
    count = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if pattern in line:
                    count += 1
    except FileNotFoundError:
        raise
    except Exception as e:
        raise RuntimeError(f"Failed to analyze the log file: {e}")
    return count