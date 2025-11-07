'''
Handles the command-line interface for the YAML file validator.
'''
import argparse
from yaml_validator import YAMLValidator
class CLIInterface:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Validate a YAML file.')
        self.parser.add_argument('file_path', type=str, help='Path to the YAML file')
    def run(self):
        args = self.parser.parse_args()
        validator = YAMLValidator()
        result = validator.validate_file(args.file_path)
        if result['success']:
            print("Success: The YAML file is valid.")
        else:
            print("Error: The YAML file is invalid.")
            for error in result['errors']:
                print(error)