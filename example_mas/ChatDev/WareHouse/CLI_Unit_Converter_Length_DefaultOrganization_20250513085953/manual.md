# CLI Unit Converter for Lengths

This user manual provides detailed instructions on how to use the CLI Unit Converter for lengths. This application allows users to convert length measurements between different units, such as meters, centimeters, inches, and feet.

## Main Functions

The CLI Unit Converter is designed to perform the following main functions:

- **Convert Lengths**: Convert a numerical value from one unit of length to another. Supported units include meters (m), centimeters (cm), inches (in), and feet (ft).

## Installation

### Environment Setup

This application is built using Python and does not require any external dependencies. To run the application, ensure you have Python installed on your system. You can download and install Python from the official [Python website](https://www.python.org/downloads/).

### Quick Install

Since there are no external dependencies, you do not need to install any additional packages. Simply ensure Python is installed and proceed to run the application.

## How to Use

1. **Run the Application**: Open your terminal or command prompt and navigate to the directory where `main.py` is located. Run the application using the following command:

   ```bash
   python main.py
   ```

2. **Input Values**: The application will prompt you to enter the following:

   - **Value to Convert**: Enter the numerical value you wish to convert.
   - **Source Unit**: Enter the unit of the value you are converting from. Supported units are `m` (meters), `cm` (centimeters), `in` (inches), and `ft` (feet).
   - **Target Unit**: Enter the unit you wish to convert the value to. Supported units are `m`, `cm`, `in`, and `ft`.

3. **View Results**: After entering the required inputs, the application will display the converted value in the target unit.

### Example Usage

- **Convert 100 centimeters to inches**:

  ```
  Enter the value to convert: 100
  Enter the source unit (m, cm, in, ft): cm
  Enter the target unit (m, cm, in, ft): in
  Result: 39.3701 in
  ```

- **Convert 5 feet to meters**:

  ```
  Enter the value to convert: 5
  Enter the source unit (m, cm, in, ft): ft
  Enter the target unit (m, cm, in, ft): m
  Result: 1.5240 m
  ```

## Error Handling

- **Invalid Input**: If you enter a non-numeric value for the conversion, the application will prompt you with "Invalid input. Please enter a numeric value."
- **Invalid Unit**: If you enter an unsupported unit, the application will raise an error message: "Invalid unit. Please enter a valid unit (m, cm, in, ft)."

## Conclusion

The CLI Unit Converter is a simple yet powerful tool for converting lengths between different units. With its straightforward interface and error handling, it provides a seamless user experience for quick and accurate conversions.