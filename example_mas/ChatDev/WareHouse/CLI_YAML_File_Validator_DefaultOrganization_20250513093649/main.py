'''
Main entry point for the YAML Validator CLI application.
'''
import argparse
from yaml_validator import YAMLValidator
def main():
    '''
    Initializes and runs the YAML Validator CLI application.
    '''
    parser = argparse.ArgumentParser(description='Validate YAML file syntax.')
    parser.add_argument('file_path', type=str, help='Path to the YAML file to validate.')
    args = parser.parse_args()
    result = YAMLValidator.validate_yaml(args.file_path)
    print(result)
if __name__ == "__main__":
    main()