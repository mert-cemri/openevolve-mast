# ChatDev PDF Text Extractor

## Quick Install

To install the required dependencies for the ChatDev PDF Text Extractor, you can use pip. First, ensure you have Python installed on your system. Then, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

This command will install the `PyMuPDF` library, which is used for extracting text from PDF files.

## 🤔 What is this?

The ChatDev PDF Text Extractor is a command-line interface (CLI) tool designed to extract text from PDF files. It can print the extracted text to the standard output or save it to a text file. The tool is built using Python and leverages the `PyMuPDF` library for text extraction.

## 📖 Documentation

### Main Functions

1. **Extract Text from PDF:**
   - The primary function of the tool is to extract text from a specified PDF file.
   - You can specify the PDF file path as a command-line argument.
   - The extracted text can be printed to the standard output or saved to a text file.

2. **Command-Line Interface (CLI):**
   - The tool provides a simple and intuitive CLI for users to interact with.
   - Users can specify the PDF file path and the output file path (if desired) using command-line arguments.

### How to Use

#### Basic Usage

To extract text from a PDF file and print it to the standard output, use the following command:

```bash
python main.py path/to/your/file.pdf
```

#### Saving to a Text File

To extract text from a PDF file and save it to a text file, use the following command:

```bash
python main.py path/to/your/file.pdf -o path/to/output/file.txt
```

### Example

Suppose you have a PDF file named `example.pdf` located in the current directory. To extract text from this file and print it to the standard output, you can use the following command:

```bash
python main.py example.pdf
```

If you want to save the extracted text to a file named `output.txt`, you can use the following command:

```bash
python main.py example.pdf -o output.txt
```

### Error Handling

The tool includes basic error handling to ensure that the specified PDF file path and output file path are valid. If an invalid path is provided, the tool will print an error message and exit.

### Dependencies

The tool requires the `PyMuPDF` library, which can be installed using pip as described in the "Quick Install" section.

## 🛠️ Development

If you want to contribute to the development of the ChatDev PDF Text Extractor, you can clone the repository from GitHub and set up the development environment using the following commands:

```bash
git clone https://github.com/ChatDev/pdf-text-extractor.git
cd pdf-text-extractor
pip install -r requirements.txt
```

Once the development environment is set up, you can make changes to the code and test them using the provided CLI commands.

## 🙋‍♂️ Support

If you encounter any issues or have questions about the tool, please feel free to reach out to the ChatDev support team. You can also check the GitHub repository for additional resources and documentation.

---

This manual provides a comprehensive overview of the ChatDev PDF Text Extractor, including its main functions, how to install dependencies, and how to use the tool. If you have any further questions or need additional assistance, please don't hesitate to ask.