```markdown
# Directory Tree Generator

A versatile CLI and GUI utility for generating a visual tree structure of a given directory. This tool allows users to visualize their directory structure up to a specified depth, making it easier to understand and manage file systems.

## Main Functions

The Directory Tree Generator provides two main interfaces:

1. **Command-Line Interface (CLI):**
   - Generate a directory tree structure directly from the command line.
   - Specify the root directory and maximum depth for tree generation.

2. **Graphical User Interface (GUI):**
   - User-friendly interface using Tkinter for selecting directories and specifying maximum depth.
   - Visualize the directory tree in a text widget.

## Quick Install

### Prerequisites

- Ensure you have Python 3.6 or higher installed on your system.

### Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Install the required Python version (if not already installed).

```bash
# No external packages are required as the project uses standard libraries
```

## How to Use

### Using the Command-Line Interface (CLI)

1. Open your terminal or command prompt.
2. Navigate to the directory containing the `main.py` file.
3. Run the following command to generate a directory tree:

```bash
python main.py --cli <directory> --max-depth <depth>
```

- Replace `<directory>` with the path to the directory you want to visualize.
- Replace `<depth>` with the maximum depth you want to traverse (default is 3).

Example:

```bash
python main.py --cli /path/to/directory --max-depth 2
```

### Using the Graphical User Interface (GUI)

1. Run the `main.py` file without any arguments to start the GUI:

```bash
python main.py
```

2. In the GUI window:
   - Click "Browse" to select the directory you want to visualize.
   - Enter the maximum depth in the "Max Depth" field.
   - Click "Generate Tree" to display the directory structure.

3. The directory tree will be displayed in the text widget within the GUI.

## Troubleshooting

- **Permission Denied:** If you encounter a "Permission Denied" message, ensure you have the necessary permissions to access the directory.
- **Tkinter Errors:** If you face issues with the GUI, ensure your environment supports graphical display or switch to CLI mode.

## Documentation

For further details and updates, please refer to the project repository or contact support.

```
