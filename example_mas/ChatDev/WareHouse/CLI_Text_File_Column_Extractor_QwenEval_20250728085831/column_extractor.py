'''
Extracts specified columns from the data based on the delimiter.
'''
def extract_columns(data, columns, delimiter):
    if delimiter == ',':
        headers = data[0]
        column_indices = []
        for col in columns.split(','):
            if col.isdigit():
                col_index = int(col) - 1
                if col_index < 0 or col_index >= len(headers):
                    raise ValueError(f"Column number {col} is out of range.")
                column_indices.append(col_index)
            else:
                if col not in headers:
                    raise ValueError(f"Header '{col}' not found in the file.")
                column_indices.append(headers.index(col))
        extracted_data = [[row[i] for i in column_indices] for row in data]
    else:
        column_indices = [int(col) - 1 for col in columns.split(',')]
        for col_index in column_indices:
            if col_index < 0 or col_index >= len(data[0]):
                raise ValueError(f"Column number {col_index + 1} is out of range.")
        extracted_data = [[row[i] for i in column_indices] for row in data]
    return extracted_data