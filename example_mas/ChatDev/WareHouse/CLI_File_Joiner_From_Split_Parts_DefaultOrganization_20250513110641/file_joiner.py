'''
Contains the FileJoiner class responsible for joining file parts into a single file.
'''
import os
class FileJoiner:
    def join_files(self, first_part_name: str, output_file_name: str):
        '''
        The join_files method assumes that the file parts are named sequentially
        with a '.part' suffix followed by a number (e.g., 'file.part1', 'file.part2', etc.).
        Ensure that the file splitter uses this naming convention.
        '''
        # Determine the base name and directory
        base_name = os.path.basename(first_part_name)
        dir_name = os.path.dirname(first_part_name)
        # Extract the prefix and check for extension
        if '.part' in base_name:
            prefix = base_name.split('.part')[0]
        else:
            prefix, _ = os.path.splitext(base_name)
        # Initialize the part number
        part_number = 1
        # Open the output file
        with open(output_file_name, 'wb') as output_file:
            while True:
                # Construct the part file name
                part_file_name = os.path.join(dir_name, f"{prefix}.part{part_number}")
                # Check if the part file exists
                if not os.path.exists(part_file_name):
                    break
                # Read the part file and write to the output file
                with open(part_file_name, 'rb') as part_file:
                    output_file.write(part_file.read())
                # Increment the part number
                part_number += 1