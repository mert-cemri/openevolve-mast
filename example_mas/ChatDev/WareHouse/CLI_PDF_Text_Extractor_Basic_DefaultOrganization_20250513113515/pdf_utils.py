'''
Utility functions for extracting text from PDF files.
'''
import PyPDF2
def extract_text_from_pdf(pdf_path):
    '''
    Extract text from a PDF file.
    Parameters:
    pdf_path (str): Path to the PDF file.
    Returns:
    str: Extracted text from the PDF.
    '''
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_number, page in enumerate(reader.pages):
                page_text = page.extract_text()
                if page_text:
                    text += page_text
                else:
                    text += f"\n[Warning: Page {page_number + 1} contains non-extractable content]\n"
    except Exception as e:
        text = f"An error occurred: {e}"
    return text