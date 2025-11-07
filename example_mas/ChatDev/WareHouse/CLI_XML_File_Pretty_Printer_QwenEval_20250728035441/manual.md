# XML File Pretty Printer User Manual

## Overview

The XML File Pretty Printer is a command-line interface (CLI) tool designed to take an XML file as input and output a well-formatted, indented version of the XML. It can either print the formatted XML to the console or save it to a new file. Additionally, a graphical user interface (GUI) is provided for users who prefer a more visual approach.

## Features

- **CLI Interface:** Allows users to specify input and output files directly from the command line.
- **GUI Interface:** Provides a user-friendly graphical interface for selecting files and performing operations.
- **XML Validation:** Ensures that the input file is a valid XML document before processing.
- **Error Handling:** Provides informative error messages for invalid XML files or missing input files.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system.
- Git (optional, for cloning the repository).

### Installation Steps

1. **Clone the Repository (Optional):**

   If you prefer to clone the repository, you can do so using Git:

   ```bash
   git clone https://github.com/ChatDev/xml-pretty-printer.git
   cd xml-pretty-printer
   ```

2. **Install Dependencies:**

   The project does not require any third-party libraries beyond Python's standard library. However, if you wish to install any dependencies listed in `requirements.txt` (which is currently empty), you can do so using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**

   You can run the application using the `main.py` script. For CLI usage, simply execute:

   ```bash
   python main.py <input_file> [-o <output_file>]
   ```

   For GUI usage, execute:

   ```bash
   python main.py --gui
   ```

## Usage

### Command-Line Interface (CLI)

The CLI interface allows you to specify the input XML file and optionally the output file directly from the command line.

#### Basic Usage

To pretty-print an XML file and print the result to the console:

```bash
python main.py input.xml
```

To pretty-print an XML file and save the result to a new file:

```bash
python main.py input.xml -o output.xml
```

#### Options

- `<input_file>`: The path to the input XML file.
- `-o <output_file>`: (Optional) The path to the output file where the pretty-printed XML will be saved.

### Graphical User Interface (GUI)

The GUI interface provides a more visual approach to selecting input and output files and performing the pretty-printing operation.

#### Launching the GUI

To launch the GUI, execute:

```bash
python main.py --gui
```

#### Using the GUI

1. **Select Input File:** Click the "Browse" button next to the "Input XML File" field to select the XML file you want to pretty-print.
2. **Select Output File (Optional):** Click the "Browse" button next to the "Output File" field to specify where you want to save the pretty-printed XML. If you leave this field blank, the result will be printed to the console.
3. **Pretty Print:** Click the "Pretty Print" button to perform the operation. If an output file is specified, a success message will be displayed. If not, the pretty-printed XML will be shown in a message box.

## Troubleshooting

### Common Issues

- **Invalid XML File:** If the input file is not a valid XML document, an error message will be displayed.
- **Missing Input File:** If the specified input file does not exist, an error message will be displayed.

### Solutions

- **Check XML Validity:** Ensure that the input file is a well-formed XML document.
- **Verify File Path:** Double-check the file path to ensure that the input file exists.

## Conclusion

The XML File Pretty Printer is a versatile tool for formatting XML files. Whether you prefer using the command line or a graphical interface, this tool provides a simple and effective way to achieve your formatting needs. If you encounter any issues or have suggestions for improvement, please feel free to reach out to our support team.

---

This manual should provide a comprehensive guide for users to understand and use the XML File Pretty Printer effectively.