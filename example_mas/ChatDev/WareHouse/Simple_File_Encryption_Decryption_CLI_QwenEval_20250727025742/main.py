'''
Main entry point for the file encryption and decryption utility.
Handles command-line arguments and performs encryption/decryption.
'''
import argparse
import sys
try:
    from file_encryptor import encrypt_file, decrypt_file
except ModuleNotFoundError:
    print("Error: The 'pycryptodome' package is not installed. Please install it using 'pip install pycryptodome'.")
    sys.exit(1)
def parse_arguments():
    '''
    Parses command-line arguments for the utility.
    Required arguments are mode (encrypt/decrypt), input file path, output file path, and password.
    '''
    parser = argparse.ArgumentParser(description='File Encryption and Decryption Utility')
    parser.add_argument('--mode', choices=['encrypt', 'decrypt'], required=True, help='Mode of operation (encrypt/decrypt)')
    parser.add_argument('--input', required=True, help='Input file path')
    parser.add_argument('--output', required=True, help='Output file path')
    parser.add_argument('--password', required=True, help='Password for encryption/decryption')
    return parser.parse_args()
def main():
    '''
    Main function to execute the encryption or decryption based on user input.
    Handles exceptions and provides feedback to the user.
    '''
    args = parse_arguments()
    try:
        if args.mode == 'encrypt':
            encrypt_file(args.input, args.output, args.password)
            print(f"File '{args.input}' encrypted successfully to '{args.output}'.")
        elif args.mode == 'decrypt':
            decrypt_file(args.input, args.output, args.password)
            print(f"File '{args.input}' decrypted successfully to '{args.output}'.")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
if __name__ == '__main__':
    main()