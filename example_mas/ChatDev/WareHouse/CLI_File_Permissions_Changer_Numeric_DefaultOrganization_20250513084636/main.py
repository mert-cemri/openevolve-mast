'''
This module contains the main application class for the file permission changer utility.
It provides a CLI for users to input file paths and permission modes to change file permissions.
'''
import os
import argparse
def set_file_permissions(path, mode):
    '''
    Set the file permissions for the given path.
    :param path: The file or directory path.
    :param mode: The permission mode in octal.
    '''
    os.chmod(path, mode)
def main():
    '''
    Main function to parse command-line arguments and change file permissions.
    '''
    parser = argparse.ArgumentParser(description='Change file permissions using numeric (octal) notation.')
    parser.add_argument('path', type=str, help='The file or directory path.')
    parser.add_argument('mode', type=str, help='The permission mode (e.g., 755).')
    args = parser.parse_args()
    try:
        # Convert mode from string to octal
        mode = int(args.mode, 8)
        # Validate the mode is within the valid range
        if not (0 <= mode <= 0o777):
            raise ValueError("Permission mode must be between 000 and 777.")
        set_file_permissions(args.path, mode)
        print(f"Permissions for '{args.path}' changed to {args.mode}.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except FileNotFoundError:
        print(f"Error: File or directory '{args.path}' not found.")
    except PermissionError:
        print("Error: Permission denied. Please check your access rights.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()