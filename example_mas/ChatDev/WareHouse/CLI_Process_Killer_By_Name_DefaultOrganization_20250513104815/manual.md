# Process Manager CLI Tool

This user manual provides detailed instructions on how to install, configure, and use the Process Manager CLI tool. This tool allows users to find and kill processes by their name through a command-line interface (CLI) or a graphical user interface (GUI).

## Main Functions

The Process Manager tool provides the following main functions:

1. **List Processes by Name**: Search for and list all processes that match a given name.
2. **Kill Processes**: Prompt for confirmation and kill the selected processes.

## Installation

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Quick Install

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**

   Install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the `psutil` library, which is necessary for managing system processes.

## Usage

### Command-Line Interface (CLI)

To use the CLI version of the Process Manager tool, follow these steps:

1. **Run the CLI Tool**

   Execute the following command in your terminal:

   ```bash
   python main.py --cli
   ```

2. **Search for Processes**

   Enter the name of the process you want to search for when prompted:

   ```
   Enter the process name to search: <process-name>
   ```

3. **List and Kill Processes**

   The tool will list all matching processes. You will be prompted to confirm if you want to kill each process:

   ```
   PID: <pid>, Name: <process-name>
   Do you want to kill process <pid>? (y/n): 
   ```

   Enter `y` to kill the process or `n` to skip.

### Graphical User Interface (GUI)

To use the GUI version of the Process Manager tool, follow these steps:

1. **Run the GUI Tool**

   Execute the following command in your terminal:

   ```bash
   python main.py
   ```

2. **Search for Processes**

   - Enter the process name in the provided text field.
   - Click the "Find Processes" button to list all matching processes.

3. **List and Kill Processes**

   - Select a process from the list.
   - Click the "Kill Selected Process" button to terminate the selected process.
   - Confirm the action in the pop-up dialog.

## Documentation

For further information and detailed documentation, please refer to the source code comments and function docstrings within the provided Python files. These comments provide additional context and technical details about the implementation and usage of each function.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided in the source code. We are committed to providing comprehensive support to ensure a smooth experience with the Process Manager tool.