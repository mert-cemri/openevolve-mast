### manual.md

```markdown
# Temperature Conversion Tool

## Introduction

The Temperature Conversion Tool is a command-line interface (CLI) application designed to convert temperatures between Celsius, Fahrenheit, and Kelvin. It allows users to input a temperature value along with the source and target units, and then outputs the converted temperature.

## Main Functions

- **Convert Temperatures:** Convert temperatures between Celsius (C), Fahrenheit (F), and Kelvin (K).
- **Command-Line Interface:** Easy-to-use CLI for quick conversions.
- **Error Handling:** Provides error messages for invalid inputs.

## Installation

### Prerequisites

- Python 3.6 or higher installed on your system.
- `pip` package manager installed.

### Steps to Install

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ChatDev/temperature-conversion-tool.git
   cd temperature-conversion-tool
   ```

2. **Install Dependencies:**

   The project requires no external dependencies beyond Python's standard library. However, if you have a `requirements.txt` file, you can install any additional dependencies using:

   ```bash
   pip install -r requirements.txt
   ```

   **Note:** The current `requirements.txt` file is empty as no external libraries are needed.

## Usage

### Running the Tool

To use the Temperature Conversion Tool, open your terminal or command prompt and navigate to the directory where the `main.py` file is located. Then, run the following command:

```bash
python main.py <value> <source_unit> <target_unit>
```

Replace `<value>` with the temperature value you want to convert, `<source_unit>` with the unit of the input temperature (C, F, or K), and `<target_unit>` with the unit you want to convert to (C, F, or K).

### Example Usage

1. **Convert 100 Celsius to Fahrenheit:**

   ```bash
   python main.py 100 C F
   ```

   **Output:**

   ```
   Result: 212.00 F
   ```

2. **Convert 32 Fahrenheit to Celsius:**

   ```bash
   python main.py 32 F C
   ```

   **Output:**

   ```
   Result: 0.00 C
   ```

3. **Convert 273.15 Kelvin to Celsius:**

   ```bash
   python main.py 273.15 K C
   ```

   **Output:**

   ```
   Result: 0.00 C
   ```

### Error Handling

- **Invalid Source or Target Unit:**

  If you provide an invalid source or target unit, the tool will raise a `ValueError` and display an error message.

  ```bash
  python main.py 100 C X
  ```

  **Output:**

  ```
  usage: main.py [-h] value source_unit target_unit
  main.py: error: argument target_unit: invalid choice: 'X' (choose from 'C', 'F', 'K')
  ```

- **Non-Numeric Value:**

  If you provide a non-numeric value for the temperature, the tool will raise a `ValueError` and display an error message.

  ```bash
  python main.py ABC C F
  ```

  **Output:**

  ```
  usage: main.py [-h] value source_unit target_unit
  main.py: error: argument value: invalid float value: 'ABC'
  ```

## Additional Features

### Graphical User Interface (GUI)

In addition to the CLI, the tool includes a graphical user interface (GUI) built using `tkinter`. To run the GUI, use the following command:

```bash
python temperature_gui.py
```

The GUI allows you to enter the temperature value, source unit, and target unit using text fields and a button to perform the conversion. The result is displayed in a label below the button.

## Conclusion

The Temperature Conversion Tool is a simple yet powerful utility for converting temperatures between Celsius, Fahrenheit, and Kelvin. Whether you prefer using the command line or the graphical interface, this tool provides a convenient way to perform temperature conversions quickly and accurately.

If you encounter any issues or have suggestions for improvement, please feel free to contact us or open an issue on our GitHub repository.
```

### requirements.txt

```plaintext
# No external dependencies are required for this project.
# All necessary functionality is provided by Python's standard library.
```

This manual provides a comprehensive guide for users to understand and use the Temperature Conversion Tool effectively. It covers installation, usage, error handling, and additional features, ensuring that users can make the most out of the tool.