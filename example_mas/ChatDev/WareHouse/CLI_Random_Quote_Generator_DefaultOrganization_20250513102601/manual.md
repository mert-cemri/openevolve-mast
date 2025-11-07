# Random Quote CLI Tool

This is a simple CLI (Command Line Interface) tool that displays a random quote from a predefined list of quotes stored in a text file. Each execution of the tool will show a different quote, providing inspiration and motivation whenever you need it.

## Main Functions

- **Load Quotes**: The tool reads quotes from a text file (`quotes.txt`) and stores them in a list.
- **Display Random Quote**: Each time the tool is executed, it selects and displays a random quote from the list.

## Installation

### Prerequisites

- **Python 3.x**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: First, clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory**: Change your directory to the project folder:
   ```bash
   cd <project-directory>
   ```
   Replace `<project-directory>` with the actual directory name.

3. **Install Dependencies**: This project does not have any external dependencies beyond Python itself, so no additional installations are required.

## How to Use

1. **Prepare the Quotes File**: Ensure that the `quotes.txt` file is in the same directory as `main.py`. This file should contain the quotes you want to display, each on a new line.

2. **Run the CLI Tool**: Execute the following command in your terminal to run the tool:
   ```bash
   python main.py
   ```

3. **View the Random Quote**: After running the command, a random quote will be displayed in your terminal.

## Example

Here's an example of what you might see when you run the tool:

```bash
$ python main.py
Here's a random quote for you:
The best way to predict the future is to invent it. - Alan Kay
```

## Customization

- **Adding Quotes**: To add more quotes, simply edit the `quotes.txt` file and add each new quote on a new line.
- **Changing Quotes File**: If you want to use a different file for quotes, modify the `file_path` parameter in the `QuoteManager` initialization within `main.py`.

## Support

For any issues or questions, please contact our support team or visit our [GitHub repository](<repository-url>) for more information and updates.