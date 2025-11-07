'''
CLI program to find unique values in a specified CSV column.
'''
import csv
import argparse
def read_csv(file_path):
    '''
    Read a CSV file and return the data as a list of dictionaries.
    '''
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]
def get_unique_column_values(data, column_name):
    '''
    Extract unique values from a specified column.
    '''
    return list(set(row[column_name] for row in data if column_name in row))
def main():
    '''
    Main function to parse arguments and find unique values in the specified column.
    '''
    parser = argparse.ArgumentParser(description='Find unique values in a specified CSV column.')
    parser.add_argument('file_path', help='Path to the CSV file')
    parser.add_argument('column_name', help='Name of the column to extract unique values from')
    args = parser.parse_args()
    try:
        data = read_csv(args.file_path)
        if not data:
            print("Error: The CSV file is empty or does not contain the specified column.")
            return
        unique_values = get_unique_column_values(data, args.column_name)
        if unique_values:
            print("\n".join(unique_values))
        else:
            print(f"No unique values found for the column '{args.column_name}'.")
    except FileNotFoundError:
        print(f"Error: The file '{args.file_path}' was not found.")
    except KeyError:
        print(f"Error: The column '{args.column_name}' does not exist in the CSV file.")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()