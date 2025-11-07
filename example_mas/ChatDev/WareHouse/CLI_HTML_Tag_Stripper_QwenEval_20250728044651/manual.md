# HTML Stripper CLI Tool

## Overview

The HTML Stripper CLI Tool is a utility designed to remove all HTML tags from an HTML file or string input, leaving only the plain text content. This tool can be used via a command-line interface (CLI) or through a graphical user interface (GUI).

## Main Functions

1. **CLI Mode**: Accepts either an HTML file path or a string input directly from the command line, processes the input to remove HTML tags, and outputs the plain text.
2. **GUI Mode**: Provides a graphical interface where users can either enter HTML content directly into a text area or select an HTML file to process. The tool will then display the plain text result.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installing Dependencies

1. Clone the repository or download the source code.
2. Navigate to the root directory of the project.
3. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should contain:

```
beautifulsoup4
tk
```

## Usage

### CLI Mode

1. **Open a terminal or command prompt.**
2. **Navigate to the directory containing the `main.py` file.**
3. **Run the tool with the appropriate arguments:**

#### Example 1: Strip HTML from a file

```bash
python main.py -f path/to/your/file.html
```

#### Example 2: Strip HTML from a string

```bash
python main.py -s "<html><body><h1>Hello, World!</h1></body></html>"
```

### GUI Mode

1. **Open a terminal or command prompt.**
2. **Navigate to the directory containing the `gui.py` file.**
3. **Run the GUI application:**

```bash
python gui.py
```

4. **Use the GUI to either enter HTML content directly or select an HTML file to process.**
5. **Click the "Strip HTML" button to see the plain text result.**

## Troubleshooting

- **FileNotFoundError**: Ensure that the file path provided is correct and that the file exists.
- **Encoding Issues**: The tool reads files with UTF-8 encoding by default. If you encounter encoding issues, you may need to modify the file reading section in `main.py` to use a different encoding.
- **HTML Parsing Errors**: If the HTML content is malformed, BeautifulSoup may not be able to parse it correctly. Ensure that the HTML is well-formed or consider using a more robust HTML parser if necessary.

## Contributing

Contributions to this project are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the GitHub repository.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

This manual should provide a comprehensive guide for users to understand and use the HTML Stripper CLI Tool effectively.