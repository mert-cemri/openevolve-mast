'''
This module contains the main logic to handle CLI interactions for joining file parts.
It uses the `argparse` module for CLI arguments.
'''
import argparse
import glob
import os
def join_file_parts(first_part):
    '''
    This function joins multiple file parts into a single file.
    It takes the first part filename as input and reconstructs the original file.
    '''
    # Extract the base filename (without the .partXX suffix)
    base_filename = os.path.splitext(os.path.splitext(first_part)[0])[0]
    # Create a pattern to match all parts
    pattern = f"{base_filename}.part*"
    # Find all parts
    parts = sorted(glob.glob(pattern))
    if not parts:
        print(f"No parts found for the pattern: {pattern}")
        return
    # Create the output file
    output_filename = f"{base_filename}"
    with open(output_filename, 'wb') as outfile:
        for part in parts:
            with open(part, 'rb') as infile:
                outfile.write(infile.read())
    print(f"Reconstructed file saved as: {output_filename}")
def main():
    '''
    This function handles the main logic for the CLI program.
    It checks if the first part filename is provided via CLI arguments.
    '''
    parser = argparse.ArgumentParser(description="Join multiple file parts into a single file.")
    parser.add_argument("first_part", help="The name of the first part file (e.g., filename.part01)")
    args = parser.parse_args()
    try:
        join_file_parts(args.first_part)
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()