# CLI Data Plotter User Manual

Welcome to the CLI Data Plotter! This application allows you to generate basic text-based bar charts or line graphs directly in your terminal from a list of numbers. This manual will guide you through the installation, usage, and main features of the software.

## Quick Install

The CLI Data Plotter is a standalone application that does not require any external dependencies. However, it requires Python version 3.6 or higher. To ensure you have the correct version of Python, you can check your Python version by running:

```bash
python --version
```

If you need to install or update Python, you can download it from the [official Python website](https://www.python.org/downloads/).

## Main Functions

The CLI Data Plotter provides the following main functions:

- **Read Data from File**: Input a list of numbers from a specified file.
- **Read Data from Standard Input (stdin)**: Input a list of numbers directly from the terminal.
- **Plot Bar Chart**: Generate a text-based bar chart of the input data.
- **Plot Line Graph**: Generate a text-based line graph of the input data.

## How to Use

### Step 1: Prepare Your Data

You can input your data in two ways:

1. **From a File**: Create a text file containing a list of numbers separated by spaces or new lines.
2. **From Standard Input**: Enter numbers directly into the terminal when prompted.

### Step 2: Run the Application

To run the CLI Data Plotter, use the following command in your terminal:

```bash
python main.py <input_type> [<filename>]
```

- `<input_type>`: Specify 'file' to read from a file or 'stdin' to read from standard input.
- `<filename>`: If using 'file' as the input type, provide the path to the file containing your data.

### Step 3: Choose Plot Type

After running the application, you will be prompted to choose the type of plot you want to generate:

- Type 'bar' to generate a bar chart.
- Type 'line' to generate a line graph.

### Example Usage

1. **Reading from a File**:
   ```bash
   python main.py file data.txt
   ```
   (Assuming `data.txt` contains your list of numbers.)

2. **Reading from Standard Input**:
   ```bash
   python main.py stdin
   ```
   (You will then be prompted to enter your numbers directly.)

### Step 4: View Your Plot

Once you have chosen your plot type, the application will display the plot directly in your terminal.

## Additional Information

- **No External Dependencies**: This application does not require any additional Python packages beyond the standard library.
- **Python Version**: Ensure you are using Python 3.6 or higher for compatibility.

Thank you for using the CLI Data Plotter! We hope this tool helps you visualize your data quickly and effectively. If you have any questions or need further assistance, please feel free to reach out to our support team.