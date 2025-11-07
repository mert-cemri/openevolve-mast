```markdown
# QR Code Generator CLI Tool

A versatile command-line interface (CLI) tool for generating QR codes from text strings or URLs. This tool allows you to output the QR code as an ASCII art representation in the terminal or save it as an image file. Additionally, a graphical user interface (GUI) is available for users who prefer a visual interaction.

## Main Functions

- **Generate QR Code from Text or URL**: Convert any text string or URL into a QR code.
- **Output as ASCII Art**: Display the generated QR code as ASCII art directly in the terminal.
- **Save as Image**: Save the generated QR code as an image file (PNG format).
- **Graphical User Interface (GUI)**: A user-friendly GUI for generating and saving QR codes.

## Quick Install

To use the QR Code Generator CLI Tool, you need to install the required dependencies. Follow the steps below to set up your environment:

1. **Clone the Repository**: Clone the project repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Use `pip` to install the necessary Python packages.
   ```bash
   pip install -r requirements.txt
   ```

## How to Use

### Command-Line Interface (CLI)

1. **Generate QR Code and Display as ASCII Art**:
   ```bash
   python main.py "Your text or URL here" --ascii
   ```

2. **Generate QR Code and Save as Image**:
   ```bash
   python main.py "Your text or URL here" -o output.png
   ```

3. **Launch the Graphical User Interface (GUI)**:
   ```bash
   python main.py --gui
   ```

### Graphical User Interface (GUI)

1. **Open the GUI**: Run the command to launch the GUI.
   ```bash
   python main.py --gui
   ```

2. **Enter Text or URL**: Input the text or URL you wish to convert into a QR code.

3. **Choose Options**:
   - Check "Save as Image" to save the QR code as a PNG file.
   - Check "Display as ASCII" to view the QR code as ASCII art.

4. **Generate QR Code**: Click the "Generate QR Code" button to create the QR code based on your input and selected options.

## Additional Information

- **Dependencies**: This tool requires the `qrcode` and `Pillow` libraries, specified in the `requirements.txt` file.
- **Compatibility**: Ensure you have Python installed on your system to run the CLI tool.

For any questions or support, please contact our team at ChatDev. We are here to assist you in making the most out of our QR Code Generator CLI Tool.
```