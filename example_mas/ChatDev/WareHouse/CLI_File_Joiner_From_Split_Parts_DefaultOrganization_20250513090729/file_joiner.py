'''
File joining logic for the File Joiner program.
'''
import os
def join_file_parts(first_part_path):
    '''
    Joins multiple file parts into a single file.
    Parameters:
    first_part_path (str): The path to the first part of the file.
    Returns:
    None
    '''
    base_dir = os.path.dirname(first_part_path)
    base_name = os.path.basename(first_part_path)
    prefix = base_name.rsplit('.', 1)[0]
    # List all files in the directory
    files = os.listdir(base_dir)
    # Filter files that match the prefix and are parts
    part_files = sorted([f for f in files if f.startswith(prefix) and f.endswith(tuple(f".part{i}" for i in range(1, len(files)+1)))])
    output_file_path = os.path.join(base_dir, "joined_file")
    with open(output_file_path, 'wb') as output_file:
        for part_file_name in part_files:
            part_file_path = os.path.join(base_dir, part_file_name)
            with open(part_file_path, 'rb') as part_file:
                output_file.write(part_file.read())
    print("Files joined successfully!")