'''
This module provides a CLI tool for encoding and decoding strings using Base64.
The user can input a string and choose whether to encode or decode it via command-line arguments.
'''
import base64
import argparse
def encode_string(input_string):
    '''Encodes the input string using Base64.'''
    encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
    return encoded_bytes.decode('utf-8')
def decode_string(input_string):
    '''Decodes the input string using Base64.'''
    try:
        decoded_bytes = base64.b64decode(input_string.encode('utf-8'))
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        return f"Error: {str(e)}"
def main():
    '''Entry point of the CLI application.'''
    parser = argparse.ArgumentParser(description='Base64 Encode/Decode CLI Tool')
    parser.add_argument('operation', choices=['encode', 'decode'], help='Operation to perform: encode or decode')
    parser.add_argument('input_string', help='The string to encode or decode')
    args = parser.parse_args()
    if args.operation == 'encode':
        output_string = encode_string(args.input_string)
    else:
        output_string = decode_string(args.input_string)
    print(output_string)
if __name__ == "__main__":
    main()