'''
Module to convert CSV content to Markdown table format.
'''
import csv
from io import StringIO
def convert_csv_to_markdown(csv_content):
    '''
    Convert CSV content to a Markdown table format.
    Parameters:
    csv_content (str): The content of the CSV file.
    Returns:
    str: A string representing the Markdown table.
    '''
    csv_reader = csv.reader(StringIO(csv_content), quoting=csv.QUOTE_MINIMAL)
    rows = list(csv_reader)
    if not rows:
        return "No data available."
    header = rows[0]
    markdown_table = "| " + " | ".join(header) + " |\n"
    markdown_table += "| " + " | ".join(['---'] * len(header)) + " |\n"
    for row in rows[1:]:
        markdown_table += "| " + " | ".join(row) + " |\n"
    return markdown_table