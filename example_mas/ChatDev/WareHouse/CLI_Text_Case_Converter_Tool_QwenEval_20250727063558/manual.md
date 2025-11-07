# Text Converter Utility User Manual

## Overview

The Text Converter Utility is a command-line interface (CLI) tool designed to convert text to various cases: uppercase, lowercase, title case, and sentence case. The tool can take text input directly from the command line or read from a specified file.

## Features

- Convert text to uppercase.
- Convert text to lowercase.
- Convert text to title case.
- Convert text to sentence case.
- Read text from a file.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system.
- `pip` (Python package installer) must be installed.

### Installing the Tool

1. **Clone the Repository (if applicable):**

   If you have the source code in a Git repository, clone it to your local machine:

   ```bash
   git clone https://github.com/your-repo/text-converter.git
   cd text-converter
   ```

2. **Install Dependencies:**

   The tool requires the `nltk` library for sentence tokenization. Install the dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the `nltk` library and any other dependencies listed in the `requirements.txt` file.

## Usage

### Basic Commands

The tool can be used in two modes: by providing text directly via the command line or by reading from a file.

#### Convert Text Directly

To convert text directly, use the following command:

```bash
python main.py "Your text here" --uppercase
```

Replace `"Your text here"` with the text you want to convert and `--uppercase` with the desired conversion option (`--lowercase`, `--titlecase`, or `--sentencecase`).

#### Convert Text from a File

To convert text from a file, use the following command:

```bash
python main.py -f path/to/your/file.txt --uppercase
```

Replace `path/to/your/file.txt` with the path to your file and `--uppercase` with the desired conversion option.

### Conversion Options

- `--uppercase`: Convert the text to uppercase.
- `--lowercase`: Convert the text to lowercase.
- `--titlecase`: Convert the text to title case.
- `--sentencecase`: Convert the text to sentence case.

### Examples

1. **Convert to Uppercase:**

   ```bash
   python main.py "hello world" --uppercase
   ```

   Output: `HELLO WORLD`

2. **Convert to Lowercase:**

   ```bash
   python main.py "HELLO WORLD" --lowercase
   ```

   Output: `hello world`

3. **Convert to Title Case:**

   ```bash
   python main.py "hello world" --titlecase
   ```

   Output: `Hello World`

4. **Convert to Sentence Case:**

   ```bash
   python main.py "this is a sentence. this is another sentence." --sentencecase
   ```

   Output: `This is a sentence. This is another sentence.`

5. **Read from a File and Convert to Sentence Case:**

   ```bash
   python main.py -f example.txt --sentencecase
   ```

   If `example.txt` contains:

   ```
   this is a sentence. this is another sentence.
   ```

   The output will be:

   ```
   This is a sentence. This is another sentence.
   ```

## Troubleshooting

- **No Text Provided:**

  If you run the tool without providing text or a file, you will see the following message:

  ```
  No text provided. Please provide text or a file.
  ```

- **Multiple Conversion Options:**

  If you specify more than one conversion option, you will see the following message:

  ```
  Please specify only one conversion option.
  ```

- **File Reading Error:**

  If the tool fails to read a file, you will see an error message indicating the issue.

## Conclusion

The Text Converter Utility is a simple yet powerful tool for converting text to various cases. By following the installation and usage instructions provided in this manual, you can easily integrate the tool into your workflow and perform text conversions efficiently.

If you encounter any issues or have suggestions for improvement, please feel free to reach out to our support team.

---

This manual provides a comprehensive guide for users to understand and utilize the Text Converter Utility effectively.