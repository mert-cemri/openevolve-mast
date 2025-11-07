# CLI Text Search Tool

A command-line interface (CLI) program that searches for a given string or pattern within all text files in a specified directory and its subdirectories, similar to the functionality of `grep -r`. This tool displays the matching lines along with their filenames.

## Main Functions

- **Recursive Search**: Searches through all text files in the specified directory and its subdirectories.
- **Pattern Matching**: Finds and displays lines containing the specified string or pattern.
- **Output**: Displays the filename and the matching line for each occurrence of the pattern.

## Installation

### Prerequisites

- Ensure you have Python 3.6 or higher installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: Clone the project repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Install the required dependencies using `pip`.

   ```bash
   pip install -r requirements.txt
   ```

   This will ensure that your environment is set up with the necessary Python version.

## Usage

To use the CLI Text Search Tool, navigate to the directory containing the `main.py` file and execute the following command:

```bash
python main.py <directory> <pattern>
```

- `<directory>`: The path to the directory where you want to perform the search.
- `<pattern>`: The string or pattern you want to search for within the text files.

### Example

To search for the pattern "example" in the directory `/path/to/directory`, use the following command:

```bash
python main.py /path/to/directory example
```

### Output

The program will output the filenames and lines where the pattern is found. If no matches are found, it will display "No matches found."

## Documentation

For further information and detailed documentation, please refer to the source code comments and function docstrings within the `main.py` and `search.py` files. These provide insights into the implementation details and logic used in the program.

## Support

For any issues or questions, please contact our support team or open an issue in the project repository. We are committed to providing assistance and improving the tool based on user feedback.