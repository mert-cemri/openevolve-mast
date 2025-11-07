'''
ColumnExtractor class for extracting columns from data.
'''
class ColumnExtractor:
    @staticmethod
    def extract_by_number(data, column_numbers):
        return [[row[i] for i in column_numbers] for row in data]
    @staticmethod
    def extract_by_header(data, column_headers):
        header = data[0]
        try:
            indices = [header.index(col) for col in column_headers]
        except ValueError as e:
            missing_headers = [col for col in column_headers if col not in header]
            raise ValueError(f"Error: The following headers are missing from the file: {', '.join(missing_headers)}") from e
        return [[row[i] for i in indices] for row in data]