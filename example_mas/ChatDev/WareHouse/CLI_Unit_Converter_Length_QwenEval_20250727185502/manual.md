# Unit Converter CLI Application

## Quick Overview

The Unit Converter CLI Application is a simple yet powerful tool designed to convert length units from one system to another. It supports conversion between meters, feet, inches, and centimeters. The application can be run in either Command Line Interface (CLI) mode or Graphical User Interface (GUI) mode, providing flexibility based on user preference.

## 📦 Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system.
- `tkinter` library is required for the GUI mode. It is included with standard Python installations, but you may need to install it separately on some Linux distributions.

### Installation Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ChatDev/unit-converter.git
   cd unit-converter
   ```

2. **Install Dependencies:**

   The application does not require any external dependencies beyond Python's standard library. However, if you encounter any issues, ensure that your Python environment is correctly set up.

## 🚀 Usage

### CLI Mode

1. **Run the Application:**

   ```bash
   python main.py
   ```

2. **Choose Mode:**

   When prompted, type `CLI` and press Enter to start the Command Line Interface mode.

3. **Perform Conversion:**

   - Enter the value you wish to convert.
   - Enter the source unit (e.g., meters, feet, inches, cm).
   - Enter the target unit (e.g., meters, feet, inches, cm).
   - The application will display the converted value.

4. **Exit:**

   Type `exit` and press Enter to quit the CLI mode.

### GUI Mode

1. **Run the Application:**

   ```bash
   python main.py
   ```

2. **Choose Mode:**

   When prompted, type `GUI` and press Enter to start the Graphical User Interface mode.

3. **Perform Conversion:**

   - Enter the value you wish to convert in the "Value" field.
   - Enter the source unit in the "Source Unit" field.
   - Enter the target unit in the "Target Unit" field.
   - Click the "Convert" button to perform the conversion.
   - The result will be displayed below the button.

4. **Exit:**

   Close the GUI window to exit the application.

## 🛠️ Main Functions

### Conversion Factors

The application uses predefined conversion factors for the following units:

- **Meters (m)**
- **Feet (ft)**
- **Inches (in)**
- **Centimeters (cm)**

### Error Handling

- **Invalid Input:** If the user enters a non-numeric value for the conversion, the application will display an error message.
- **Invalid Units:** If the user enters an unsupported unit, the application will display an error message listing the available units.

## 📖 Documentation

For more detailed information, including additional features and troubleshooting tips, please refer to the [full documentation](https://github.com/ChatDev/unit-converter/wiki).

## 🙋‍♂️ Support

If you encounter any issues or have suggestions for improvement, please feel free to open an issue on the [GitHub repository](https://github.com/ChatDev/unit-converter/issues).

---

This manual should provide users with a comprehensive understanding of how to install, use, and troubleshoot the Unit Converter CLI Application. If you have any specific requirements or additional features to include, please let me know!