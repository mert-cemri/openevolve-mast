```markdown
# CLI Utility for Adding Line Numbers to Text Files

This utility is a command-line interface (CLI) application designed to add line numbers to each line of a text file. The output can be directed to a new file or printed to standard output.

## Main Functions

- **Add Line Numbers**: The utility reads a text file, adds line numbers to each line, and either writes the result to a specified output file or prints it to the console.
- **Flexible Output**: Users can choose to save the numbered lines to a new file or simply view them in the terminal.

## Installation

### Prerequisites

- **Python Version**: Ensure you have Python 3.6 or higher installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository containing the utility code.
   
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Although this utility does not have external dependencies beyond Python itself, it is good practice to ensure your environment is set up correctly.

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command-Line Interface

The utility is executed from the command line. Below is the syntax for running the utility:

```bash
python main.py <input_file> [-o <output_file>]
```

- `<input_file>`: The path to the text file you want to process.
- `-o <output_file>`: (Optional) The path to the output file where the numbered lines will be saved. If this option is not provided, the output will be printed to the standard output (console).

### Examples

1. **Output to Console**: To add line numbers and print the result to the console:

   ```bash
   python main.py example.txt
   ```

2. **Output to File**: To add line numbers and save the result to a new file:

   ```bash
   python main.py example.txt -o numbered_example.txt
   ```

## Documentation

For further details on the implementation and potential extensions, please refer to the code comments within `main.py`. The script is designed to be straightforward and easily modifiable for additional features or customization.

## Support

For any issues or questions, please contact our support team or refer to our community forums for assistance.

```
```