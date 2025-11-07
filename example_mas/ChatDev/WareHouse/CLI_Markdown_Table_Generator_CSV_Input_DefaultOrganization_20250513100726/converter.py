'''
Module for converting CSV data to Markdown table format.
'''
import csv
class CSVToMarkdownConverter:
    def convert(self, csv_file_path):
        '''
        Reads the CSV file and converts it to a Markdown table string.
        :param csv_file_path: Path to the CSV file.
        :return: Markdown table as a string.
        '''
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            if not rows:
                raise ValueError("CSV file is empty")
            header = rows[0]
            table = [header]
            table.extend(rows[1:])
            # Calculate column widths
            col_widths = [max(len(str(item)) for item in col) for col in zip(*table)]
            # Create Markdown table
            markdown_table = self._create_markdown_table(table, col_widths)
            return markdown_table
    def _create_markdown_table(self, table, col_widths):
        '''
        Helper method to create a Markdown table from the table data and column widths.
        :param table: List of rows, where each row is a list of cell values.
        :param col_widths: List of column widths.
        :return: Markdown table as a string.
        '''
        def format_row(row):
            return "| " + " | ".join(f"{str(item).ljust(width)}" for item, width in zip(row, col_widths)) + " |"
        header_row = format_row(table[0])
        separator_row = "| " + " | ".join("-" * width for width in col_widths) + " |"
        data_rows = [format_row(row) for row in table[1:]]
        return "\n".join([header_row, separator_row] + data_rows)