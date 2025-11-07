# Unit Converter CLI Tool

## Overview

The Unit Converter CLI Tool is a simple yet powerful application designed to convert weights and mass between different units. It supports conversions between kilograms (kg), grams (g), pounds (lb), and ounces (oz). The tool is available in both Command Line Interface (CLI) and Graphical User Interface (GUI) versions, catering to different user preferences.

## Main Functions

- **Convert Weights/Mass:** Convert values between kilograms, grams, pounds, and ounces.
- **User-Friendly Interface:** Choose between a CLI for quick conversions or a GUI for a more interactive experience.
- **Error Handling:** Receive clear error messages for unsupported conversions or invalid inputs.

## Installation

### Prerequisites

- **Python:** Ensure you have Python 3.6 or higher installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps to Install

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ChatDev/unit-converter.git
   cd unit-converter
   ```

2. **Install Dependencies:**
   This project does not require any third-party dependencies. However, ensure you have Python installed as mentioned above.

## Usage

### Command Line Interface (CLI)

1. **Run the CLI:**
   ```bash
   python main.py <value> <source_unit> <target_unit>
   ```
   Replace `<value>` with the numerical value you wish to convert, `<source_unit>` with the unit of the input value, and `<target_unit>` with the unit you want to convert to.

   **Example:**
   ```bash
   python main.py 10 kg lb
   ```
   This command converts 10 kilograms to pounds.

2. **Error Handling:**
   - If you provide an incorrect number of arguments, the tool will display a usage message.
   - If the value is not a number, the tool will prompt you to enter a valid number.
   - If the conversion is not supported, the tool will display an error message.

### Graphical User Interface (GUI)

1. **Run the GUI:**
   If you run the tool without any command line arguments, it will automatically launch the GUI version.
   ```bash
   python main.py
   ```

2. **Using the GUI:**
   - Enter the value you wish to convert in the "Value" field.
   - Select the source unit from the "Source Unit" field.
   - Select the target unit from the "Target Unit" field.
   - Click the "Convert" button to see the result.

3. **Error Handling:**
   - If you enter an invalid value, a message box will appear prompting you to enter a valid number.
   - If the conversion is not supported, a message box will appear with an error message.

## Supported Units

- **Kilograms (kg)**
- **Grams (g)**
- **Pounds (lb)**
- **Ounces (oz)**

## Troubleshooting

- **tkinter Not Available:**
  If you encounter an error stating that `tkinter` is not available, you can run the CLI version as described above.
  ```bash
  python main.py <value> <source_unit> <target_unit>
  ```

- **Python Version:**
  Ensure you are using Python 3.6 or higher. You can check your Python version by running:
  ```bash
  python --version
  ```

## Conclusion

The Unit Converter CLI Tool is a versatile and user-friendly application designed to simplify weight and mass conversions. Whether you prefer the simplicity of the command line or the interactivity of the GUI, this tool has you covered. If you encounter any issues or have suggestions for improvement, feel free to reach out to our support team.

---

This manual should provide a comprehensive guide for users to understand and utilize the Unit Converter CLI Tool effectively.