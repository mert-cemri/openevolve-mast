```markdown
# HTML Stripper CLI Tool

A command-line interface (CLI) tool designed to strip HTML tags from an HTML file or string input, leaving only the plain text content.

## Main Functions

The HTML Stripper CLI Tool provides the following main functionalities:

- **Strip HTML Tags from a String**: Input a string containing HTML content and receive plain text output.
- **Strip HTML Tags from a File**: Input a file path containing HTML content and receive plain text output.

## Installation

### Prerequisites

- Ensure you have Python 3.x installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Quick Install

1. Clone the repository or download the source code files.
2. Navigate to the directory containing the source code.
3. No external dependencies are required, but ensure your Python environment is set up correctly.

## Usage

### Command-Line Interface

The CLI tool can be used to strip HTML tags from either a string or a file. Below are the steps to use the CLI tool:

1. **Navigate to the directory** containing the `main.py` file.
2. **Run the CLI tool** using the following command:

   ```bash
   python main.py <input> [--file]
   ```

   - `<input>`: This is the HTML content or the file path containing HTML content.
   - `--file`: Use this flag if the input is a file path.

#### Examples

- **Strip HTML from a String**:

  ```bash
  python main.py "<html><body>Hello, World!</body></html>"
  ```

- **Strip HTML from a File**:

  ```bash
  python main.py path/to/your/file.html --file
  ```

### Graphical User Interface (Optional)

For users who prefer a graphical interface, a simple GUI is provided using Tkinter.

1. **Run the GUI** by executing the following command:

   ```bash
   python gui.py
   ```

2. **Use the GUI** to input HTML content and click the "Strip HTML" button to see the plain text output.

## Documentation

For further details on the implementation and code structure, please refer to the source code files:

- `main.py`: Entry point for the application.
- `html_stripper.py`: Contains the logic to strip HTML tags.
- `cli.py`: Handles command-line operations.
- `gui.py`: Provides a graphical user interface using Tkinter.

Feel free to explore and modify the code to suit your needs. If you encounter any issues or have questions, please reach out to our support team.

```
