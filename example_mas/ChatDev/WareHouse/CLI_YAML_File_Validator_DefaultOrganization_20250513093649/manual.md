```markdown
# YAML Validator CLI Application

A command-line interface (CLI) application for validating the syntax of YAML files. This tool helps ensure that your YAML files are correctly formatted and provides detailed error messages with line numbers if any syntax issues are detected.

## Main Functions

- **Validate YAML Syntax**: The primary function of this application is to validate the syntax of a YAML file. It reads the file, checks for any syntax errors, and provides feedback on the validity of the file.

- **Error Reporting**: If the YAML file contains syntax errors, the application will report the error along with the specific line and column number where the error occurred.

## Installation

To use the YAML Validator CLI application, you need to have Python installed on your system. Additionally, you need to install the required dependencies listed in the `requirements.txt` file.

### Step-by-Step Installation

1. **Clone the Repository**: First, clone the repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

3. **Install Dependencies**: Use pip to install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Once the environment is set up, you can use the YAML Validator CLI application to validate YAML files.

### Running the CLI Application

1. **Navigate to the Application Directory**: Ensure you are in the directory where the application files are located.

2. **Run the Application**: Use the following command to run the application and validate a YAML file.
   ```bash
   python main.py <path-to-yaml-file>
   ```

   Replace `<path-to-yaml-file>` with the actual path to the YAML file you want to validate.

3. **Interpreting Results**: The application will print a message indicating whether the YAML syntax is valid. If there are errors, it will provide details about the error, including the line and column number.

### Example

To validate a file located at `config/example.yaml`, you would run:
```bash
python main.py config/example.yaml
```

### GUI Version

For users who prefer a graphical interface, a GUI version of the YAML Validator is also available. To use the GUI:

1. **Run the GUI Application**: Execute the following command:
   ```bash
   python yaml_validator_gui.py
   ```

2. **Use the Interface**: Use the "Browse" button to select a YAML file and click "Validate" to check its syntax.

## Documentation

For more detailed documentation and examples, please refer to the source code and comments within the files. The code is designed to be straightforward and easy to understand, with comments explaining each function's purpose and usage.

## Support

For any issues or questions, please contact our support team or open an issue on the repository's issue tracker.

```