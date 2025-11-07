'''
This module contains the logic to join file parts into a single file.
It uses the `glob` module to find all parts and concatenate them.
'''
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