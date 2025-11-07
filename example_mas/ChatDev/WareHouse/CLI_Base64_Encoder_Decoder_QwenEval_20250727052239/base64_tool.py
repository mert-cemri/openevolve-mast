'''
This module contains the Base64Tool class which handles the encoding and decoding of strings.
'''
import base64
class Base64Tool:
    def encode(self, input_string):
        '''Encodes the input string using Base64.'''
        return base64.b64encode(input_string.encode()).decode()
    def decode(self, input_string):
        '''Decodes the input string using Base64.'''
        try:
            return base64.b64decode(input_string).decode()
        except Exception as e:
            return f"Error decoding: {str(e)}"