```markdown
# QR Code Generator CLI Tool

A simple command-line interface (CLI) tool to generate QR codes from a given text string or URL. The tool can output the QR code as an ASCII art representation in the terminal or save it as an image file.

## Quick Install

To use the QR Code Generator CLI Tool, you need to have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## 🤔 What is this?

This CLI tool allows users to easily generate QR codes from any text or URL. The generated QR code can be displayed as ASCII art directly in the terminal or saved as an image file for later use. This tool is ideal for developers, marketers, or anyone who needs to quickly create QR codes for various applications.

## Main Functions

- **Generate QR Code**: Create a QR code from a given text string or URL.
- **Display ASCII Art**: Convert the QR code into ASCII art and display it in the terminal.
- **Save as Image**: Save the generated QR code as an image file in the specified format.

## How to Use

1. **Generate and Display QR Code as ASCII Art**

   To generate a QR code and display it as ASCII art in the terminal, use the following command:

   ```bash
   python main.py "Your text or URL here" --ascii
   ```

   Replace `"Your text or URL here"` with the text or URL you want to encode.

2. **Generate and Save QR Code as an Image**

   To generate a QR code and save it as an image file, use the following command:

   ```bash
   python main.py "Your text or URL here" --save filename.png
   ```

   Replace `"Your text or URL here"` with the text or URL you want to encode, and `filename.png` with your desired file name and format.

3. **Generate and Perform Both Actions**

   You can also generate a QR code, display it as ASCII art, and save it as an image simultaneously:

   ```bash
   python main.py "Your text or URL here" --ascii --save filename.png
   ```

## 📖 Documentation

For more detailed information on how the tool works, please refer to the source code files:

- `main.py`: The main application file that handles command-line arguments and orchestrates the QR code generation process.
- `qr_utils.py`: Contains utility functions for generating QR codes, converting them to ASCII art, and saving them as image files.

## Dependencies

The tool relies on the following Python packages:

- `qrcode`: For generating QR codes.
- `Pillow`: For handling image creation and manipulation.

Ensure these packages are installed by using the `requirements.txt` file provided.

```bash
pip install -r requirements.txt
```

## Support

For any issues or questions, please contact our support team or refer to the documentation provided in the source code files.
```