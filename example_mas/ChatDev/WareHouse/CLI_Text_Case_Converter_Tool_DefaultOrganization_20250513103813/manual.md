```markdown
# Text Case Converter CLI Utility

A command-line interface (CLI) utility to convert text to various cases: uppercase, lowercase, title case, and sentence case. This tool can take a string as input directly or read from a file.

## Quick Install

To use the Text Case Converter CLI utility, ensure you have Python installed on your system. This utility requires Python version 3.6 or higher.

### Installation Steps

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**

   Change your directory to the project folder:

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the actual directory name.

3. **Install Dependencies:**

   Although no additional third-party packages are required, ensure your Python environment is set up correctly. You can create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Then, install any dependencies (if needed) using:

   ```bash
   pip install -r requirements.txt
   ```

## 🤔 What is this?

The Text Case Converter CLI utility is designed to facilitate the conversion of text into different cases. It supports:

- **Uppercase Conversion**: Converts all characters in the text to uppercase.
- **Lowercase Conversion**: Converts all characters in the text to lowercase.
- **Title Case Conversion**: Converts the first character of each word to uppercase.
- **Sentence Case Conversion**: Converts the first character of each sentence to uppercase.

## 📖 How to Use

### Command-Line Usage

Run the utility from the command line using the following syntax:

```bash
python main.py <input> [--uppercase | --lowercase | --titlecase | --sentencecase] [--file]
```

- `<input>`: The text string or file path you want to convert.
- `--uppercase`: Convert text to uppercase.
- `--lowercase`: Convert text to lowercase.
- `--titlecase`: Convert text to title case.
- `--sentencecase`: Convert text to sentence case.
- `--file`: Indicate that the input is a file path.

### Examples

1. **Convert a String to Uppercase:**

   ```bash
   python main.py "Hello World" --uppercase
   ```

2. **Convert a File's Content to Lowercase:**

   ```bash
   python main.py path/to/file.txt --lowercase --file
   ```

3. **Convert a String to Title Case:**

   ```bash
   python main.py "hello world" --titlecase
   ```

4. **Convert a File's Content to Sentence Case:**

   ```bash
   python main.py path/to/file.txt --sentencecase --file
   ```

## Support

For any issues or questions, please contact our support team or refer to the documentation provided in the repository.

```
