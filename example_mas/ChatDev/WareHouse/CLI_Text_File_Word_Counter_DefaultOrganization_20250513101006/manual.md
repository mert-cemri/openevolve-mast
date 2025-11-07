```markdown
# Word Count CLI Tool

A simple command-line interface (CLI) tool for counting words in a text file. This tool reads a text file, counts the number of words by identifying sequences of alphanumeric characters, and outputs the total word count to the console.

## Main Functions

- **Word Counting**: The tool reads a text file specified by the user, processes the text to identify words, and counts them. Words are defined as sequences of alphanumeric characters, and basic punctuation is handled appropriately.

## Quick Install

### Prerequisites

- Ensure you have Python 3.6 or higher installed on your system.

### Installation Steps

1. **Clone the Repository**: Clone the repository containing the CLI tool to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up the Environment**: It is recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**: Install the required dependencies using the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

## How to Use

1. **Run the Tool**: Use the command line to run the tool. You need to provide the path to the text file you want to analyze.

   ```bash
   python main.py <file_path>
   ```

   Replace `<file_path>` with the actual path to your text file.

2. **Output**: The tool will output the total word count to the console. If the file is not found, an error message will be displayed.

   Example:

   ```bash
   python main.py sample.txt
   ```

   Output:

   ```
   Total Words: 123
   ```

## Error Handling

- **File Not Found**: If the specified file path does not exist, the tool will output an error message indicating that the file was not found.

- **General Errors**: Any other exceptions will be caught and displayed with a generic error message.

## Documentation

For more detailed information on the tool's implementation and usage, please refer to the source code and comments within the `main.py` and `utils.py` files.

```