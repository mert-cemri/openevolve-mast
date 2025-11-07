'''
Command-line interface for changing file permissions.
'''
import argparse
from permission_changer import change_permissions
def main():
    parser = argparse.ArgumentParser(description='Change file permissions using numeric (octal) notation.')
    parser.add_argument('mode', type=str, help='Permission mode (e.g., 755)')
    parser.add_argument('file_path', type=str, help='File or directory path')
    args = parser.parse_args()
    try:
        change_permissions(args.file_path, args.mode)
        print(f"Permissions for {args.file_path} changed to {args.mode}.")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except FileNotFoundError as fnfe:
        print(f"File Not Found Error: {fnfe}")
    except PermissionError as pe:
        print(f"Permission Error: {pe}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    main()