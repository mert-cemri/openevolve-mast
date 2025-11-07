'''
CLI program to analyze a log file for a specific pattern.
'''
import argparse
def count_pattern_in_file(file_path, pattern):
    '''
    Count the number of lines containing the pattern in the specified file.
    :param file_path: Path to the log file.
    :param pattern: Pattern to search for in the file.
    :return: Tuple of (count, lines) where count is the number of matching lines and lines is a list of those lines.
    '''
    count = 0
    matching_lines = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if pattern in line:
                    count += 1
                    matching_lines.append(line.strip())
    except Exception as e:
        raise IOError(f"Error reading file: {e}")
    return count, matching_lines
def main():
    '''
    Main function to parse arguments and perform log analysis.
    '''
    parser = argparse.ArgumentParser(description='Analyze a log file for a specific pattern.')
    parser.add_argument('file_path', type=str, help='Path to the log file')
    parser.add_argument('pattern', type=str, help='Pattern to search for in the log file')
    args = parser.parse_args()
    try:
        count, lines = count_pattern_in_file(args.file_path, args.pattern)
        print(f"Total lines containing pattern '{args.pattern}': {count}")
        for line in lines:
            print(line)
    except IOError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()