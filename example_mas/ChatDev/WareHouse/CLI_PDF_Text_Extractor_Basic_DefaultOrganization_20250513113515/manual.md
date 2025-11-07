```markdown
# CLI PDF Text Extractor

A command-line interface (CLI) tool for extracting text from PDF files. This tool allows users to extract text content from a specified PDF file and either print it to the standard output or save it to a text file.

## Main Functions

- **Extract Text from PDF**: The tool reads a PDF file and extracts all text content.
- **Output Options**: Users can choose to print the extracted text directly to the console or save it to a specified text file.

## Installation

### Prerequisites

Ensure you have Python installed on your system. This tool requires Python 3.6 or later.

### Quick Install

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the necessary library, PyPDF2, which is used for PDF text extraction.

## Usage

### Command-Line Interface

To use the CLI PDF Text Extractor, open your terminal or command prompt and navigate to the directory containing the `main.py` file. Use the following command structure:

```bash
python main.py <pdf_path> [--output <output_path>]
```

- `<pdf_path>`: The path to the PDF file you want to extract text from.
- `--output <output_path>`: (Optional) The path where you want to save the extracted text. If not provided, the text will be printed to the console.

### Examples

1. **Extract and Print to Console**

   To extract text from a PDF and print it to the console, use:

   ```bash
   python main.py example.pdf
   ```

2. **Extract and Save to File**

   To extract text from a PDF and save it to a text file, use:

   ```bash
   python main.py example.pdf --output output.txt
   ```

   This will save the extracted text to `output.txt`.

## Error Handling

- If the PDF contains non-extractable content, a warning message will be included in the output indicating which page contains such content.
- If an error occurs during the extraction process, an error message will be displayed.

## Support

For any issues or questions, please contact our support team or visit our documentation page for more detailed guidance.

```