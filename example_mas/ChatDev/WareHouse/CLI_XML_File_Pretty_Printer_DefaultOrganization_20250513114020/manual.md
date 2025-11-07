```markdown
# XML Pretty Printer CLI

A command-line interface (CLI) application for pretty printing XML files, developed in Python. This tool takes an XML file and outputs a well-formatted, indented version to the console or a specified output file.

## Main Functions

- **Pretty Print XML**: The application reads an XML file and formats it with proper indentation for better readability.
- **Output Options**: Users can choose to display the formatted XML directly in the console or save it to a new file.

## Quick Install

To use the XML Pretty Printer CLI, you need to have Python installed on your system. The application is compatible with Python version 3.6 and above.

### Step 1: Install Python

Ensure you have Python 3.6 or later installed. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Dependencies

The application does not require any external libraries beyond the Python standard library. However, it's good practice to set up a virtual environment:

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### Step 3: Clone the Repository

Clone the repository containing the XML Pretty Printer CLI code:

```bash
git clone <repository-url>
cd <repository-directory>
```

## How to Use

### Running the Application

The application is executed via the command line. Here’s how you can use it:

1. **Basic Usage**: To pretty print an XML file and display the output in the console, use:

   ```bash
   python main.py path/to/input.xml
   ```

2. **Output to a File**: To pretty print an XML file and save the output to a new file, use:

   ```bash
   python main.py path/to/input.xml -o path/to/output.xml
   ```

### Command-Line Arguments

- `input_file`: The path to the XML file you want to pretty print.
- `-o, --output`: (Optional) The path where you want to save the pretty-printed XML. If not specified, the output will be printed to the console.

## Example

Here’s an example command to pretty print an XML file named `example.xml` and save the output to `formatted_example.xml`:

```bash
python main.py example.xml -o formatted_example.xml
```

This command will read `example.xml`, format it with proper indentation, and save the result to `formatted_example.xml`.

## Support

For any issues or questions, please contact our support team at support@chatdev.com.

```
