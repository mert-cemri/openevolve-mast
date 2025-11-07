# Duplicate File Finder

A command-line interface (CLI) and graphical user interface (GUI) application to find duplicate files within a specified directory based on their content using hash algorithms like MD5 or SHA256.

## Main Functions

The Duplicate File Finder application provides two main functionalities:

1. **CLI Application**: Allows users to find duplicate files in a specified directory using a command-line interface.
2. **GUI Application**: Provides a graphical user interface for users who prefer a visual interaction to find duplicate files.

### CLI Application

- **Find Duplicate Files**: The CLI application scans a specified directory and lists paths of duplicate files based on their content hash.

### GUI Application

- **Browse and Select Directory**: Users can browse and select a directory to scan for duplicate files.
- **Display Results**: The GUI displays the list of duplicate files found in the selected directory.

## Installation

### Environment Setup

This project does not require any third-party packages, but it does require Python to be installed on your system. Additionally, ensure that `tkinter` is available in your Python installation for the GUI application.

### Quick Install

1. **Clone the Repository**: Clone the project repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Ensure Python is Installed**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

3. **Check for Tkinter**: Ensure that `tkinter` is available in your Python installation. It is usually included by default, but you can verify by running:
   ```bash
   python -m tkinter
   ```

## Usage

### CLI Application

1. **Navigate to the Project Directory**: Open your terminal and navigate to the directory where the project is located.

2. **Run the CLI Application**: Use the following command to run the CLI application:
   ```bash
   python main.py <directory-path>
   ```
   Replace `<directory-path>` with the path of the directory you want to scan for duplicate files.

3. **View Results**: The application will output the paths of duplicate files found in the specified directory.

### GUI Application

1. **Run the GUI Application**: Execute the following command to start the GUI application:
   ```bash
   python gui.py
   ```

2. **Select Directory**: Use the "Browse" button to select the directory you want to scan for duplicate files.

3. **View Results**: The application will display the paths of duplicate files in the text area of the GUI.

## Documentation

For further details on how the application works, you can refer to the source code files:

- `main.py`: Contains the main script to run the CLI application.
- `finder.py`: Implements the logic to find duplicate files using hash algorithms.
- `gui.py`: Implements the GUI for the application using Tkinter.

Feel free to explore and modify the code to suit your needs. If you encounter any issues or have questions, please reach out for support.