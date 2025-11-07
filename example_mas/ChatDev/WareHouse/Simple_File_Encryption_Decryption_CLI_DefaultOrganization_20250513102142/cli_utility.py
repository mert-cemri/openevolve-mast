'''
Provides a command-line interface for the file encryption and decryption utility.
'''
# cli_utility.py
import argparse
from file_encryptor import FileEncryptor
class CLIUtility:
    def __init__(self):
        self.encryptor = FileEncryptor()
    def run(self):
        parser = argparse.ArgumentParser(description='File Encryption/Decryption Utility')
        parser.add_argument('mode', choices=['encrypt', 'decrypt'], help='Mode of operation')
        parser.add_argument('input_file', help='Input file path')
        parser.add_argument('output_file', help='Output file path')
        parser.add_argument('password', help='Password for encryption/decryption')
        args = parser.parse_args()
        try:
            if args.mode == 'encrypt':
                self.encryptor.encrypt_file(args.input_file, args.output_file, args.password)
            elif args.mode == 'decrypt':
                self.encryptor.decrypt_file(args.input_file, args.output_file, args.password)
            print(f"File {args.mode}ed successfully!")
        except ValueError as e:
            print(f"Error: {e}")