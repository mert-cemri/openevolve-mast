'''
Main application file for the CLI utility to change file permissions.
'''
import argparse
from permission_changer import change_file_permissions
def main():
    '''
    Main function to parse arguments and change file permissions.
    '''
    parser = argparse.ArgumentParser(description="Change file permissions using numeric (octal) notation.")
    parser.add_argument('mode', type=str, help='Permission mode (e.g., 755)')
    parser.add_argument('path', type=str, help='File/Directory path')
    args = parser.parse_args()
    mode = args.mode
    path = args.path
    if not mode.isdigit() or len(mode) != 3:
        print("Error: Invalid permission mode. Please enter a three-digit octal number.")
        return
    try:
        change_file_permissions(path, int(mode, 8))
        print(f"Success: Permissions for '{path}' changed to {mode}.")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()