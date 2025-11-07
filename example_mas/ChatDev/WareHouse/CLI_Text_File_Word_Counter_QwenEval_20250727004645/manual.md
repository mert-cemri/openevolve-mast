# Word Count Tool User Manual

## Introduction

The Word Count Tool is a simple yet powerful Command Line Interface (CLI) application designed to count the total number of words in a given text file. It handles basic punctuation and counts sequences of alphanumeric characters as words. This manual will guide you through the installation process, usage instructions, and provide some additional tips.

## Quick Install

To use the Word Count Tool, you need to have Python installed on your system. The tool has been developed and tested with Python 3.6 and above. You can download Python from the [official website](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the source code from [ChatDev GitHub](https://github.com/ChatDev/word-count-tool).

### Cloning the Repository

```bash
git clone https://github.com/ChatDev/word-count-tool.git
cd word-count-tool
```

### Installing Dependencies

The Word Count Tool does not have any external dependencies beyond the Python Standard Library. However, if you encounter any issues, ensure that your Python environment is correctly set up.

## 🤔 What is this?

The Word Count Tool is a simple CLI application that reads a text file, processes its content to count words, and outputs the total count to the console. It is designed to be lightweight and efficient, making it suitable for quick word count tasks.

## 📖 Documentation

### Main Functions

- **CLI Interface**: The tool provides a command-line interface that allows users to specify the path to a text file and receive the word count as output.
- **Word Count Logic**: The core functionality involves reading the file, processing its content using regular expressions to identify words, and counting them.

### How to Use

1. **Open your terminal or command prompt**.
2. **Navigate to the directory where the Word Count Tool is located**.
3. **Run the tool with the path to your text file**:

```bash
python main.py /path/to/your/textfile.txt
```

**Example:**

```bash
python main.py example.txt
```

**Output:**

```
Total word count: 123
```

### Error Handling

- **File Not Found**: If the specified file does not exist, the tool will output an error message:

```
Error: The file /path/to/your/textfile.txt does not exist.
```

- **Other Exceptions**: Any other exceptions that occur during file processing will be caught and an error message will be displayed.

### Additional Tips

- **Ensure the file path is correct**: Double-check the file path to avoid errors.
- **Supported File Formats**: The tool is designed to work with plain text files (`.txt`). Other file formats may not be processed correctly.
- **Handling Punctuation**: The tool handles basic punctuation and counts sequences of alphanumeric characters as words.

## Conclusion

The Word Count Tool is a simple yet effective solution for counting words in text files. By following this manual, you should be able to install and use the tool without any issues. If you encounter any problems or have suggestions for improvement, please feel free to reach out to the development team.

---

This manual provides a comprehensive overview of the Word Count Tool, including installation, usage, and troubleshooting tips. It should help users get started quickly and efficiently.