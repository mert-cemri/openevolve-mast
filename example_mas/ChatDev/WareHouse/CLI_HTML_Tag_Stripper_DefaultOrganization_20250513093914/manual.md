# HTML Stripper CLI Tool

Welcome to the HTML Stripper CLI Tool! This application is designed to strip all HTML tags from an HTML file or string input, leaving only the plain text content. The tool can be used in both command-line interface (CLI) and graphical user interface (GUI) modes.

## Main Functions

- **Strip HTML Tags from a File**: Provide the path to an HTML file, and the tool will output the plain text content.
- **Strip HTML Tags from a String**: Input an HTML string directly, and the tool will output the plain text content.
- **Dual Interface**: Use the tool via the command line or through a simple GUI.

## Installation

### Environment Setup

This project does not require any external dependencies beyond Python's standard library. However, ensure that `tkinter` is available in your Python environment if you wish to use the GUI mode.

### Quick Install

1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Ensure Python is Installed**: 
   Make sure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

3. **Verify tkinter Availability**: 
   `tkinter` is included with standard Python installations. To verify, run:
   ```bash
   python -m tkinter
   ```
   If a simple window appears, `tkinter` is installed correctly.

## How to Use

### Command-Line Interface (CLI)

1. **Run the Application**:
   ```bash
   python main.py -f <path-to-html-file>
   ```
   or
   ```bash
   python main.py -s "<html-string>"
   ```

2. **Options**:
   - `-f`, `--file`: Specify the path to an HTML file.
   - `-s`, `--string`: Provide an HTML string directly.

3. **Example**:
   ```bash
   python main.py -f example.html
   ```
   or
   ```bash
   python main.py -s "<p>Hello, <b>world</b>!</p>"
   ```

### Graphical User Interface (GUI)

1. **Run the Application**:
   Simply execute the script without any arguments:
   ```bash
   python main.py
   ```

2. **Using the GUI**:
   - Enter HTML content in the input text area.
   - Click the "Strip HTML" button.
   - View the plain text output in the output text area.

## Troubleshooting

- **File Not Found**: Ensure the file path is correct when using the `-f` option.
- **No Display Environment**: If running on a server or a system without a display, use the CLI mode instead of the GUI.

## Support

For any issues or questions, please contact our support team or visit our [GitHub repository](<repository-url>) for more information and updates.

Thank you for using the HTML Stripper CLI Tool! We hope it simplifies your workflow and enhances your productivity.