'''
Logic for splitting files into smaller parts.
'''
import os
def split_file(file_path, chunk_size, output_dir):
    '''
    Splits the specified file into smaller parts of the given chunk size.
    :param file_path: Path to the file to be split.
    :param chunk_size: Size of each chunk in bytes.
    :param output_dir: Directory to save the split files.
    '''
    base_name = os.path.basename(file_path)
    file_name, file_extension = os.path.splitext(base_name)
    file_size = os.path.getsize(file_path)
    # Handle multiple dots in the file name
    if '.' in file_name:
        file_name = base_name[:base_name.rfind('.')]
    with open(file_path, 'rb') as f:
        part_num = 0
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            part_num += 1
            part_file_name = os.path.join(output_dir, f"{file_name}.part{part_num}{file_extension}")
            with open(part_file_name, 'wb') as part_file:
                part_file.write(chunk)