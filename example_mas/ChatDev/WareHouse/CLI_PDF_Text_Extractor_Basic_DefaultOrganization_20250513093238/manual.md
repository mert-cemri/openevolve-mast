```markdown
# CLI PDF Text Extractor

A command-line interface (CLI) application for extracting text from PDF files. This tool allows users to extract text content from a PDF file and either print it to the standard output or save it to a specified text file.

## Main Functions

- **Extract Text from PDF**: The application reads a PDF file and extracts all text content.
- **Output Options**: Users can choose to print the extracted text to the console or save it to a text file.

## Quick Install

To use the CLI PDF Text Extractor, you need to have Python installed on your system. Follow the steps below to set up the environment and install necessary dependencies.

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
```

### Step 2: Navigate to the Project Directory

Change into the project directory:

```bash
cd <project-directory>
```

### Step 3: Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

This will install the `PyPDF2` library, which is used for reading PDF files.

## How to Use

The CLI PDF Text Extractor can be used directly from the command line. Below are the instructions on how to run the application:

### Basic Usage

To extract text from a PDF and print it to the standard output, use the following command:

```bash
python main.py <pdf-file-path>
```

Replace `<pdf-file-path>` with the path to your PDF file.

### Save Extracted Text to a File

If you want to save the extracted text to a file, use the `-o` or `--output` option followed by the desired output file path:

```bash
python main.py <pdf-file-path> -o <output-file-path>
```

Replace `<output-file-path>` with the path where you want to save the extracted text.

### Example

Extract text from `example.pdf` and print it to the console:

```bash
python main.py example.pdf
```

Extract text from `example.pdf` and save it to `output.txt`:

```bash
python main.py example.pdf -o output.txt
```

## Documentation

For more detailed documentation and examples, please refer to the source code comments and function docstrings in `main.py` and `pdf_utils.py`.

## Support

If you encounter any issues or have questions, please contact our support team or open an issue in the repository.

```
```