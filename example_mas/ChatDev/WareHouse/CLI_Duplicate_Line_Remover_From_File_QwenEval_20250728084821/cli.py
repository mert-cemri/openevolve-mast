'''
Handles the command-line interface logic for removing duplicate lines.
'''
from core import remove_duplicates
def remove_duplicates_cli(input_file, output_file):
    '''
    Removes duplicate lines from the input file and writes the result to the output file.
    If output_file is None, the result is printed to standard output.
    Handles exceptions and provides meaningful feedback to the user.
    '''
    try:
        remove_duplicates(input_file, output_file)
        if output_file:
            print(f'Duplicates removed and saved to {output_file}')
        else:
            print('Duplicates removed and printed to standard output')
    except FileNotFoundError:
        print(f'Error: The file {input_file} was not found.')
    except Exception as e:
        print(f'An error occurred: {str(e)}')