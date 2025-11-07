'''
Main application file for the Markdown Table Generator CLI.
'''
import argparse
from converter import convert_csv_to_markdown
def main():
    '''
    Main function to handle command-line arguments and convert CSV to Markdown.
    '''
    parser = argparse.ArgumentParser(description='Convert a CSV file to a Markdown table.')
    parser.add_argument('csv_file', type=str, help='Path to the CSV file')
    args = parser.parse_args()
    try:
        with open(args.csv_file, 'r', newline='') as file:
            csv_content = file.read()
        markdown_table = convert_csv_to_markdown(csv_content)
        print(markdown_table)
    except Exception as e:
        print(f"Error: Failed to read file: {e}")
if __name__ == "__main__":
    main()