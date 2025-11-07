'''
Main application file for the CLI YAML Validator.
'''
import argparse
from yaml_validator import validate_yaml_file
def main():
    '''
    Main function to parse arguments and validate YAML file.
    '''
    parser = argparse.ArgumentParser(description='Validate a YAML file.')
    parser.add_argument('file_path', type=str, help='Path to the YAML file to validate')
    args = parser.parse_args()
    result = validate_yaml_file(args.file_path)
    print(result)
if __name__ == "__main__":
    main()