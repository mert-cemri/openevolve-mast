# Random Quote CLI Tool User Manual

## Introduction

Welcome to the Random Quote CLI Tool! This tool is designed to display a random quote from a predefined list of quotes stored in a text file. Each execution of the tool will show a different quote, making it a fun and engaging way to start your day or break up your work.

## Main Functions

- **Load Quotes**: The tool reads quotes from a file named `quotes.txt` located in the same directory as the script.
- **Select Random Quote**: It selects a random quote from the loaded list and displays it to the user.
- **User-Friendly CLI**: The tool is designed to be simple and easy to use via the command line interface (CLI).

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps to Install

1. **Clone the Repository or Download the Code**: You can either clone the repository from GitHub or download the code as a ZIP file and extract it to your desired location.

2. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the directory where the project files are located.

3. **Install Dependencies**: This project has no external dependencies, but it's good practice to use a virtual environment. You can create and activate a virtual environment using the following commands:

   - **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

   - **macOS/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

4. **Install Required Packages**: Since there are no external dependencies, you can skip this step. However, if you have a `requirements.txt` file, you can install the packages using:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Tool

To run the Random Quote CLI Tool, follow these steps:

1. **Ensure the `quotes.txt` File is Present**: Make sure that the `quotes.txt` file is located in the same directory as the `main.py` file. This file contains the list of quotes from which a random quote will be selected.

2. **Execute the Script**: Run the following command in your terminal or command prompt:
   ```bash
   python main.py
   ```

   - **Note**: If you are using Python 3 and the above command does not work, try:
     ```bash
     python3 main.py
     ```

### Example

Here is an example of how the tool might look when executed:

```bash
$ python main.py
"The only way to do great work is to love what you do." - Steve Jobs
```

Each time you run the script, a different quote will be displayed.

## Customization

### Adding New Quotes

To add new quotes to the list, simply open the `quotes.txt` file in a text editor and add your new quotes, each on a new line. For example:

```txt
"Be yourself; everyone else is already taken." - Oscar Wilde
"The only way to do great work is to love what you do." - Steve Jobs
"Success is not final, failure is not fatal: It is the courage to continue that counts." - Winston Churchill
"Believe you can and you're halfway there." - Theodore Roosevelt
"Life is what happens when you're busy making other plans." - John Lennon
"Your time is limited, so don't waste it living someone else's life." - Steve Jobs
```

### Changing the Quotes File

If you want to use a different file for storing quotes, you can modify the `QuoteManager` class in `quote_manager.py` to specify a different filename. For example:

```python
quote_manager = QuoteManager(filename='custom_quotes.txt')
```

## Troubleshooting

### File Not Found Error

If you encounter a "File not found" error, ensure that the `quotes.txt` file (or the file you specified) is located in the same directory as the `main.py` file.

### Empty Quotes List

If the `quotes.txt` file is empty or contains no valid quotes, the tool will display a default quote: "Life is what happens when you're busy making other plans." - John Lennon.

## Conclusion

Thank you for using the Random Quote CLI Tool! We hope you find it useful and engaging. If you have any questions or suggestions, feel free to reach out to us.

---

This manual should provide a comprehensive guide for users to understand and use the Random Quote CLI Tool effectively.