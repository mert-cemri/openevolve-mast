'''
Main application file for the JSON viewer CLI application.
'''
import sys
import json
def format_json(file_path):
    '''
    Reads a JSON file, formats it, and prints it to the console.
    :param file_path: Path to the JSON file.
    '''
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        formatted_json = json.dumps(data, indent=4)
        print(formatted_json)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not a valid JSON file.")
    except Exception as e:
        print(f"Error reading or formatting JSON file: {e}")
def main():
    '''
    Entry point for the CLI application.
    '''
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        format_json(file_path)
    else:
        print("Usage: python main.py <path_to_json_file>")
if __name__ == "__main__":
    main()