'''
File splitting logic for dividing a large file into smaller chunks.
'''
import os
def split_file(file_path, chunk_size_mb, output_dir):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    chunk_size = chunk_size_mb * 1024 * 1024  # Convert MB to bytes
    file_size = os.path.getsize(file_path)
    file_name = os.path.basename(file_path)
    # Calculate the number of chunks to determine zero-padding width
    total_chunks = (file_size + chunk_size - 1) // chunk_size
    padding_width = len(str(total_chunks))
    with open(file_path, 'rb') as f:
        chunk_number = 0
        while True:
            chunk_data = f.read(chunk_size)
            if not chunk_data:
                break
            chunk_file_name = f"{file_name}_part{chunk_number:0{padding_width}}"
            chunk_file_path = os.path.join(output_dir, chunk_file_name)
            with open(chunk_file_path, 'wb') as chunk_file:
                chunk_file.write(chunk_data)
            chunk_number += 1