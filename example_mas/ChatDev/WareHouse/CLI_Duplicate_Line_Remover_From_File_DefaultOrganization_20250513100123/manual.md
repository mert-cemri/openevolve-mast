```markdown
# Duplicate Line Remover CLI Tool

A command-line interface (CLI) tool designed to remove duplicate lines from a text file, preserving the order of the first occurrence. The tool can output the results to a new file or print them to the standard output.

## Quick Install

This tool is implemented in Python and does not require any external dependencies. Ensure you have Python 3.6 or higher installed on your system.

### Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Verify Python Installation:**
   Ensure that Python 3.6 or higher is installed on your system. You can verify this by running:
   ```bash
   python --version
   ```

3. **Install Dependencies:**
   There are no external dependencies for this project. However, you can create a virtual environment to manage your Python packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

## 🤔 What is this?

The Duplicate Line Remover CLI Tool is designed to help users clean up text files by removing duplicate lines while maintaining the order of their first occurrence. This can be particularly useful for processing logs, configuration files, or any text data where duplicates may occur.

## 📖 How to Use

### Running the Tool

1. **Basic Usage:**
   To remove duplicate lines from a file and print the result to the standard output, use:
   ```bash
   python main.py <input_file>
   ```

2. **Output to a File:**
   To save the output to a new file, use the `-o` or `--output` option:
   ```bash
   python main.py <input_file> -o <output_file>
   ```

### Example

Suppose you have a text file `example.txt` with the following content:

```
apple
banana
apple
orange
banana
```

Running the tool with the command:
```bash
python main.py example.txt
```

Will output:
```
apple
banana
orange
```

To save this output to a file named `unique_example.txt`, use:
```bash
python main.py example.txt -o unique_example.txt
```

## Troubleshooting

- **File Not Found Error:** Ensure the input file path is correct.
- **Permission Error:** Check if you have the necessary permissions to read the input file or write to the output file.

## Support

For any issues or feature requests, please contact our support team or open an issue in the repository.

```
