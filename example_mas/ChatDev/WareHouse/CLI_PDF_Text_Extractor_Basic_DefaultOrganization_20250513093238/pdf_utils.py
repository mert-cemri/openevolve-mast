'''
Utility functions for extracting text from PDF and saving text to a file.
'''
import PyPDF2
def extract_text_from_pdf(pdf_path):
    '''
    Extracts text from a PDF file.
    :param pdf_path: Path to the PDF file.
    :return: Extracted text as a string.
    '''
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text
def save_text_to_file(text, file_path):
    '''
    Saves text to a specified file.
    :param text: Text to save.
    :param file_path: Path to the file where text will be saved.
    '''
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)