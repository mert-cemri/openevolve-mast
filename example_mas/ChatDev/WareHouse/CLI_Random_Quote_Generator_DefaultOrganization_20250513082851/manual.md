# Quote Display CLI Tool

Welcome to the Quote Display CLI Tool! This application is designed to display a random quote from a predefined list of quotes stored in a text file. Each execution of the tool will show a different quote, providing inspiration or entertainment at the command line.

## Main Functions

- **Load Quotes**: The tool reads quotes from a specified text file, ensuring that each line in the file is treated as a separate quote.
- **Display Random Quote**: Once the quotes are loaded, the tool randomly selects and displays one quote each time it is executed.

## Installation

### Environment Setup

This project does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Quick Install

Clone the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

No additional installation steps are required since there are no external dependencies.

## Usage

### Running the Application

To use the Quote Display CLI Tool, follow these steps:

1. Prepare a text file containing your quotes. Each quote should be on a separate line.

2. Open your terminal or command prompt.

3. Navigate to the directory where the `main.py` file is located.

4. Run the application using the following command:

   ```bash
   python main.py <path_to_quotes_file>
   ```

   Replace `<path_to_quotes_file>` with the path to your text file containing quotes.

### Example

Assuming you have a file named `quotes.txt` in the same directory as `main.py`, you would run:

```bash
python main.py quotes.txt
```

This command will display a random quote from the `quotes.txt` file.

## Troubleshooting

- **File Not Found Error**: If you encounter an error stating that the file was not found, ensure that the file path you provided is correct and that the file exists.

- **No Quotes Available**: If the tool displays "No quotes available," check that your quotes file is not empty and that each quote is on a separate line.

## Conclusion

The Quote Display CLI Tool is a simple yet effective way to bring a bit of randomness and inspiration to your command line. Feel free to modify the quotes file to suit your preferences and enjoy the variety of quotes each time you run the tool.