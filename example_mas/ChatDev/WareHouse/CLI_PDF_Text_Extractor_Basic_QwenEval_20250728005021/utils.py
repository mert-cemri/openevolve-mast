'''
Utility functions for the PDF text extractor tool.
'''
import os
def validate_pdf_path(pdf_path):
    '''
    Validates that the provided path is a valid PDF file.
    '''
    return os.path.isfile(pdf_path) and pdf_path.lower().endswith(".pdf")
def validate_output_path(output_path):
    '''
    Validates that the provided path is a valid directory or file path.
    '''
    directory = os.path.dirname(output_path)
    return os.path.exists(directory) or not directory