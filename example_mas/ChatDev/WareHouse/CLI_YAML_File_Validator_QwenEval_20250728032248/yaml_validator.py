'''
Handles the validation of YAML files.
'''
import yaml
from utils import read_file, format_error_message
class YAMLValidator:
    def __init__(self):
        self.errors = []
    def validate_file(self, file_path):
        self.errors = []
        try:
            content = read_file(file_path)
            yaml.safe_load(content)
            return {'success': True, 'errors': self.errors}
        except yaml.YAMLError as e:
            self.errors.append(format_error_message(e))
            return {'success': False, 'errors': self.errors}
    def get_error_details(self):
        return self.errors