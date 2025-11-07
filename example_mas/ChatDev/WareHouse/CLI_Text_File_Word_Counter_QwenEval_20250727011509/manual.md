# Word Count CLI Tool User Manual

## Overview

The Word Count CLI Tool is a simple yet powerful command-line utility designed to count the total number of words in a text file. It handles basic punctuation and counts sequences of alphanumeric characters as words. This tool is particularly useful for writers, researchers, and anyone who needs to quickly assess the word count of a document.

## Features

- **Command-Line Interface (CLI):** Easy to use from the terminal.
- **Punctuation Handling:** Automatically removes punctuation to accurately count words.
- **Alphanumeric Word Counting:** Counts sequences of alphanumeric characters as words.
- **Custom Encoding Support:** Supports specifying file encoding (default is UTF-8).

## Installation

### Prerequisites

- **Python 3.6+**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **pip**: Python's package installer, usually included with Python installations.

### Steps

1. **Clone the Repository (Optional):**

   If you prefer to clone the repository, you can do so using Git:

   ```bash
   git clone https://github.com/ChatDev/word-count-cli.git
   cd word-count-cli
   ```

2. **Install Dependencies:**

   The tool requires no external dependencies beyond Python's standard library. However, if you cloned the repository, you can install any additional dependencies (if any) using pip:

   ```bash
   pip install -r requirements.txt
   ```

   Note: As of now, there are no external dependencies required for this tool.

## Usage

### Basic Usage

To count the words in a text file, use the following command:

```bash
python main.py <file_path>
```

Replace `<file_path>` with the path to your text file.

### Example

```bash
python main.py example.txt
```

This command will output the total word count of `example.txt` to the console.

### Advanced Usage

You can also specify the file encoding if it differs from the default UTF-8:

```bash
python main.py <file_path> <encoding>
```

Replace `<encoding>` with the desired file encoding (e.g., `latin1`, `ascii`).

### Example

```bash
python main.py example.txt latin1
```

This command will count the words in `example.txt` using the `latin1` encoding.

## Troubleshooting

### Common Issues

- **File Not Found Error:**

  Ensure that the file path you provided is correct and that the file exists at the specified location.

- **Encoding Error:**

  If you encounter an encoding error, try specifying the correct encoding for your file.

### Contact Support

For any issues or questions, please contact our support team at [support@chatdev.com](mailto:support@chatdev.com).

## License

This software is released under the MIT License. For more information, see the [LICENSE](LICENSE) file.

## Contributing

We welcome contributions from the community! If you'd like to contribute to the Word Count CLI Tool, please see our [CONTRIBUTING](CONTRIBUTING.md) guide.

---

This manual provides a comprehensive guide to using the Word Count CLI Tool, covering installation, usage, and troubleshooting. If you have any further questions or need additional assistance, feel free to reach out to our support team.