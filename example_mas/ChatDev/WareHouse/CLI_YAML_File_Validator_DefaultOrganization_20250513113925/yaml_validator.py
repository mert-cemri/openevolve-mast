'''
Utility functions for validating YAML files.
'''
import yaml
def validate_yaml_file(file_path):
    '''
    Validate the syntax of a YAML file and return success or error messages with line numbers.
    '''
    try:
        with open(file_path, 'r') as file:
            yaml.safe_load(file)
        return "YAML syntax is valid."
    except yaml.YAMLError as exc:
        if hasattr(exc, 'problem_mark'):
            mark = exc.problem_mark
            return f"Error in YAML file at line {mark.line + 1}, column {mark.column + 1}: {exc.problem}"
        else:
            return f"YAML syntax error: {exc}"