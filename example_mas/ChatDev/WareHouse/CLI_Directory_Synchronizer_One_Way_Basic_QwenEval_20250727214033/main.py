'''
Main application file for the Directory Synchronizer.
This file handles the synchronization process via command line.
'''
import os
import shutil
from datetime import datetime
import logging
# Setting up logging
logging.basicConfig(filename='sync.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def sync_files(source, target):
    for root, dirs, files in os.walk(source):
        for file in files:
            source_file = os.path.join(root, file)
            relative_path = os.path.relpath(source_file, source)
            target_file = os.path.join(target, relative_path)
            target_dir = os.path.dirname(target_file)
            try:
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                if not os.path.exists(target_file) or os.path.getmtime(source_file) > os.path.getmtime(target_file):
                    shutil.copy2(source_file, target_file)
                    logging.info(f"Copied/Updated: {source_file} to {target_file}")
            except PermissionError:
                logging.error(f"Permission denied: {source_file}")
            except FileNotFoundError:
                logging.error(f"File not found: {source_file}")
            except Exception as e:
                logging.error(f"An error occurred while processing {source_file}: {e}")
def main():
    source_directory = input("Enter the source directory: ")
    target_directory = input("Enter the target directory: ")
    if not source_directory or not target_directory:
        print("Please provide both source and target directories.")
        return
    try:
        sync_files(source_directory, target_directory)
        print("Synchronization completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()