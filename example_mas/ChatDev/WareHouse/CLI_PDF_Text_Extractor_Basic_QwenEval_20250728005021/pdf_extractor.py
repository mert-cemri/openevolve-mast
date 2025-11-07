'''
Handles the extraction of text from a PDF file.
'''
import pdftotext
class PDFExtractor:
    def extract_text(self, pdf_path):
        '''
        Extracts text from a PDF file and returns it as a string.
        '''
        try:
            with open(pdf_path, "rb") as f:
                pdf = pdftotext.PDF(f)
            return "\n\n".join(pdf)
        except Exception as e:
            raise Exception(f"Failed to extract text from PDF: {e}")
    def save_text_to_file(self, text, output_path):
        '''
        Saves the extracted text to a specified file.
        '''
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)
        except Exception as e:
            raise Exception(f"Failed to save text to file: {e}")