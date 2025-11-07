'''
Main entry point for the file encryption and decryption application using CLI.
'''
import argparse
from file_encryptor import FileEncryptor
def main():
    parser = argparse.ArgumentParser(description='Encrypt or decrypt files using AES encryption.')
    parser.add_argument('mode', choices=['encrypt', 'decrypt'], help='Mode of operation: encrypt or decrypt')
    parser.add_argument('input_file', help='Path to the input file')
    parser.add_argument('output_file', help='Path to the output file')
    parser.add_argument('password', help='Password for encryption/decryption')
    args = parser.parse_args()
    try:
        validate_password(args.password)
    except ValueError as e:
        print(f"Error: {e}")
        return
    encryptor = FileEncryptor()
    if args.mode == 'encrypt':
        encryptor.encrypt_file(args.input_file, args.output_file, args.password)
        print("File encrypted successfully!")
    elif args.mode == 'decrypt':
        encryptor.decrypt_file(args.input_file, args.output_file, args.password)
        print("File decrypted successfully!")
def validate_password(password):
    # Enforce strong password requirements
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit.")
    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least one uppercase letter.")
    if not any(char.islower() for char in password):
        raise ValueError("Password must contain at least one lowercase letter.")
    if not any(char in "!@#$%^&*()-_+=" for char in password):
        raise ValueError("Password must contain at least one special character.")
    return True
if __name__ == "__main__":
    main()