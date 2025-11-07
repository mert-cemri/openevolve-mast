import os
import re
def search(directory, pattern):
    """
    Searches for a given string/pattern within all text files in a specified directory and its subdirectories.
    :param directory: The directory to search in.
    :param pattern: The pattern to search for.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), "r") as f:
                    for line in f:
                        match = re.search(pattern, line)
                        if match is not None:
                            print(f"{file}: {line}")