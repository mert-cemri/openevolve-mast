'''
Main entry point for the CSV Unique Values Finder CLI application.
Handles the initialization and running of the application.
'''
import sys
from csv_processor import CSVProcessor
def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <csv_file_path> <column_name>")
        sys.exit(1)
    file_path = sys.argv[1]
    column_name = sys.argv[2]
    try:
        processor = CSVProcessor(file_path)
        unique_values = processor.get_unique_values(column_name)
        print(f"Unique values in column '{column_name}':")
        for value in unique_values:
            print(value)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except KeyError:
        print(f"Error: Column '{column_name}' not found in the CSV file.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
if __name__ == "__main__":
    main()