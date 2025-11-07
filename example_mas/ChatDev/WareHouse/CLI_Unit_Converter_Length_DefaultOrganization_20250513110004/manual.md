# CLI Unit Converter User Manual

Welcome to the CLI Unit Converter! This application allows you to convert lengths between different units such as meters, feet, inches, and centimeters. This manual will guide you through the installation, usage, and features of the software.

## Quick Install

The CLI Unit Converter is a simple Python application that does not require any external dependencies. To get started, ensure you have Python installed on your system.

### Installation Steps

1. **Clone the Repository**: First, clone the repository containing the CLI Unit Converter code to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change your directory to the location where the project files are stored.

   ```bash
   cd <project-directory>
   ```

3. **Run the Application**: Execute the main application file using Python.

   ```bash
   python main.py
   ```

## 🤔 What is this?

The CLI Unit Converter is a command-line interface application designed to facilitate the conversion of length measurements between different units. It supports the following units:

- Meters
- Feet
- Inches
- Centimeters

This tool is particularly useful for quick conversions without the need for a graphical interface or internet access.

## 📖 How to Use

1. **Start the Application**: Run the `main.py` file using Python as described in the installation steps.

2. **Input the Value**: When prompted, enter the numeric value you wish to convert.

   ```
   Enter the value to convert: 10
   ```

3. **Specify the Source Unit**: Enter the unit of the value you are converting from. The available options are `meters`, `feet`, `inches`, and `cm`.

   ```
   Enter the source unit (meters, feet, inches, cm): meters
   ```

4. **Specify the Target Unit**: Enter the unit you wish to convert the value to. The available options are the same as above.

   ```
   Enter the target unit (meters, feet, inches, cm): feet
   ```

5. **View the Result**: The application will display the converted value in the target unit.

   ```
   Result: 32.81 feet
   ```

## Troubleshooting

- **Invalid Input**: If you enter a non-numeric value, the application will prompt you to enter a valid numeric value.
  
  ```
  Invalid input. Please enter a numeric value.
  ```

- **Invalid Unit**: If you enter a unit that is not supported, the application will prompt you to enter a valid unit.

  ```
  Invalid unit. Please enter a valid unit (meters, feet, inches, cm).
  ```

## Conclusion

The CLI Unit Converter is a straightforward and efficient tool for converting length measurements. With its simple interface and no dependency requirements, it is easy to use and accessible for anyone needing quick conversions. Enjoy using the CLI Unit Converter for all your length conversion needs!