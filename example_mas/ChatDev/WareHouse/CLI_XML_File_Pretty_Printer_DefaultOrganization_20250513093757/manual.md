# XML Pretty Printer CLI

A command-line interface (CLI) application for formatting XML files into a well-structured, indented format. This tool allows users to output the formatted XML either to the console or save it to a new file.

## Main Functions

- **Pretty Print to Console**: Reads an XML file and outputs a well-formatted version to the console.
- **Pretty Print to File**: Reads an XML file and writes the formatted version to a specified output file.

## Installation

### Environment Dependencies

To run the XML Pretty Printer CLI, you need to have Python installed on your system. Additionally, the application requires the `lxml` library for XML parsing and formatting.

#### Quick Install

You can install the required dependencies using `pip`:

```bash
pip install lxml
```

Alternatively, you can use the `requirements.txt` file to install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

The XML Pretty Printer CLI can be executed from the command line. Below are the instructions on how to use the application:

1. **Pretty Print to Console**

   To format an XML file and print it to the console, use the following command:

   ```bash
   python main.py path/to/input.xml
   ```

   Replace `path/to/input.xml` with the path to your XML file.

2. **Pretty Print to File**

   To format an XML file and save the output to a new file, use the following command:

   ```bash
   python main.py path/to/input.xml -o path/to/output.xml
   ```

   Replace `path/to/input.xml` with the path to your XML file and `path/to/output.xml` with the desired output file path.

### Error Handling

- If the XML file contains syntax errors, the application will output an "XML Syntax Error" message.
- If the specified input file is not found, an error message will indicate that the file was not found.
- Any other exceptions will be caught and displayed as a general error message.

## Conclusion

The XML Pretty Printer CLI is a simple yet powerful tool for developers and users who need to format XML files efficiently. By following the installation and usage instructions, you can easily integrate this tool into your workflow for better XML file management.