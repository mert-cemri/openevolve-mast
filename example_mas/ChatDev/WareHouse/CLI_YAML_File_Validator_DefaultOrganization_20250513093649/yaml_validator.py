'''
YAML Validator class to validate YAML files and return results.
'''
import yaml
class YAMLValidator:
    '''
    Handles the validation of YAML files.
    '''
    @staticmethod
    def validate_yaml(file_path):
        '''
        Validates the YAML file at the given path.
        :param file_path: Path to the YAML file.
        :return: Success or error message with line numbers.
        '''
        try:
            with open(file_path, 'r') as file:
                yaml.safe_load(file)
            return "YAML syntax is valid."
        except yaml.YAMLError as exc:
            if hasattr(exc, 'problem_mark'):
                mark = exc.problem_mark
                return f"YAML syntax error at line {mark.line + 1}, column {mark.column + 1}: {exc.problem}"
            else:
                return f"YAML syntax error: {exc}"
        except Exception as e:
            return f"Error reading file: {e}"