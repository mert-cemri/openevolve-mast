'''
This module contains the CLIInterface class which handles the command-line interface logic.
'''
from base64_tool import Base64Tool
class CLIInterface:
    def __init__(self):
        self.tool = Base64Tool()
    def run(self, args):
        '''Runs the CLI interface with the provided arguments.'''
        action = args[0]
        input_string = args[1]
        if action == "encode":
            result = self.tool.encode(input_string)
            print(f"Encoded: {result}")
        elif action == "decode":
            result = self.tool.decode(input_string)
            print(f"Decoded: {result}")
        else:
            print("Invalid action. Use 'encode' or 'decode'.")