'''
This file contains the main application code for a CLI tool to encode and decode strings using Base64.
'''
import base64
import argparse
class Base64Tool:
    @staticmethod
    def encode_string(input_string):
        '''
        Encodes the input string using Base64.
        '''
        try:
            encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
            return encoded_bytes.decode('utf-8')
        except Exception as e:
            return f"Error encoding string: {e}"
    @staticmethod
    def decode_string(input_string):
        '''
        Decodes the input string from Base64.
        '''
        try:
            decoded_bytes = base64.b64decode(input_string.encode('utf-8'))
            return decoded_bytes.decode('utf-8')
        except Exception as e:
            return f"Error decoding string: {e}"
def main():
    '''
    Main function to parse command-line arguments and perform Base64 encoding or decoding.
    '''
    parser = argparse.ArgumentParser(description='Base64 Encode/Decode CLI Tool')
    parser.add_argument('operation', choices=['encode', 'decode'], help='Operation to perform: encode or decode')
    parser.add_argument('input_string', help='The string to encode or decode')
    args = parser.parse_args()
    if args.operation == 'encode':
        result = Base64Tool.encode_string(args.input_string)
    elif args.operation == 'decode':
        result = Base64Tool.decode_string(args.input_string)
    print(f"Result: {result}")
if __name__ == "__main__":
    main()