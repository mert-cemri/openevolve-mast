# QR Code Generator CLI Tool

## Overview

The QR Code Generator CLI Tool is a Python-based application that allows users to generate QR codes from text strings or URLs. The tool can output the QR code as an ASCII art representation in the terminal or save it as an image file. This tool is designed to be simple, efficient, and user-friendly, making it suitable for a wide range of users, from developers to casual users.

## Main Functions

### Generate QR Code

The primary function of the tool is to generate a QR code from a given text string or URL. The QR code can be displayed as ASCII art in the terminal or saved as an image file.

### Save QR Code

Users can choose to save the generated QR code as an image file. The tool supports saving QR codes in PNG format.

### Display QR Code as ASCII Art

For users who prefer a terminal-based output, the tool can display the QR code as ASCII art in the terminal.

## Installation

To use the QR Code Generator CLI Tool, you need to have Python installed on your system. The tool requires Python 3.6 or later.

### Install Dependencies

The tool has the following dependencies:

- `qrcode[pil]`: This ensures that the `qrcode` library is installed with the `pil` extra, which includes the Pillow library as a dependency.
- `Pillow>=9.0.1`: This specifies that the Pillow library should be installed, with a minimum version of 9.0.1.

To install these dependencies, you can use the `requirements.txt` file provided with the tool. Run the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

To generate a QR code from a text string or URL, run the following command in your terminal:

```bash
python main.py "Your text string or URL"
```

### Save QR Code as an Image File

To save the generated QR code as an image file, use the `--output` option followed by the desired filename. For example:

```bash
python main.py "Your text string or URL" --output qr_code.png
```

### Display QR Code as ASCII Art

If you do not specify the `--output` option, the tool will display the QR code as ASCII art in the terminal:

```bash
python main.py "Your text string or URL"
```

## Examples

### Example 1: Generate QR Code and Display as ASCII Art

```bash
python main.py "https://www.example.com"
```

### Example 2: Generate QR Code and Save as Image File

```bash
python main.py "https://www.example.com" --output example_qr.png
```

## Troubleshooting

### Issue: Dependencies Not Installed

If you encounter an error indicating that dependencies are not installed, make sure to run the following command:

```bash
pip install -r requirements.txt
```

### Issue: Python Version Not Supported

Ensure that you are using Python 3.6 or later. You can check your Python version by running:

```bash
python --version
```

If you need to install a newer version of Python, you can download it from the [official Python website](https://www.python.org/downloads/).

## Conclusion

The QR Code Generator CLI Tool is a simple and efficient way to generate QR codes from text strings or URLs. Whether you need to display QR codes as ASCII art in the terminal or save them as image files, this tool has you covered. If you encounter any issues or have suggestions for improvement, please feel free to reach out to the development team.

---

This manual should provide users with a comprehensive understanding of how to use the QR Code Generator CLI Tool, including installation, usage, and troubleshooting steps.