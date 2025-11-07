'''
Main file for the CLI program that reads a CSV file and prints unique values from a specified column.
'''
import csv
import sys
class CSVReader:
    def __init__(self):
        self.data = []
    def read_csv(self, file_path):
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                self.data = list(reader)
            return True
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return False
        except Exception as e:
            print(f"Error: Failed to read CSV file: {e}")
            return False
    def get_unique_values(self, column_name):
        if not self.data:
            return []
        try:
            unique_values = set(row[column_name] for row in self.data if column_name in row)
            return list(unique_values)
        except KeyError:
            print(f"Error: Column '{column_name}' not found in the CSV file.")
            return []
def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <file_path> <column_name>")
        return
    file_path = sys.argv[1]
    column_name = sys.argv[2]
    csv_reader = CSVReader()
    if csv_reader.read_csv(file_path):
        unique_values = csv_reader.get_unique_values(column_name)
        if unique_values:
            print("Unique Values:")
            for value in unique_values:
                print(value)
        else:
            print("No unique values found or column not found.")
if __name__ == "__main__":
    main()