'''
Implements the command-line interface for changing file permissions.
'''
import argparse
from file_permissions import change_permissions
def main():
    parser = argparse.ArgumentParser(description="Change file permissions using numeric (octal) notation.")
    parser.add_argument('mode', type=str, help='Permission mode (e.g., 755, 644)')
    parser.add_argument('path', type=str, help='File or directory path')
    args = parser.parse_args()
    try:
        change_permissions(args.path, args.mode)
        print(f"Permissions changed for {args.path} to {args.mode}")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == '__main__':
    main()