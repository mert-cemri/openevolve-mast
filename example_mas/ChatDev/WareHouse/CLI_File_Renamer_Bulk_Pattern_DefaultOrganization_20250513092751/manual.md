# CLI File Renamer

A command-line interface (CLI) application for renaming multiple files in a directory based on a specified pattern. This application allows users to add prefixes, replace substrings, and add sequential numbers to file names.

## Main Functions

The CLI File Renamer provides the following functionalities:

- **Add Prefix**: Add a specified prefix to the beginning of each file name in the directory.
- **Replace Substring**: Replace a specified substring within the file names with a new substring.
- **Add Sequential Numbers**: Append sequential numbers to file names, starting from a specified number.

## Installation

### Prerequisites

- **Python 3.x**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Setup

1. **Clone the Repository**: Clone the project repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Install the required dependencies. The primary dependency is `tkinter`, which is used for the GUI version of the application. Note that `tkinter` is included with standard Python installations on Windows and macOS. On some Linux distributions, you may need to install it separately.
   ```bash
   # For Ubuntu or Debian-based systems
   sudo apt-get install python3-tk
   ```

## Usage

### CLI Usage

1. **Navigate to the Project Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

2. **Run the Application**: Use the following command to run the application with desired options.
   ```bash
   python main.py <directory> [--prefix PREFIX] [--replace OLD NEW] [--start-number START_NUMBER]
   ```

   - `<directory>`: The directory containing files to rename.
   - `--prefix PREFIX`: (Optional) The prefix to add to file names.
   - `--replace OLD NEW`: (Optional) The old substring to replace and the new substring to replace it with.
   - `--start-number START_NUMBER`: (Optional) The starting number for sequential numbering.

   **Example**:
   ```bash
   python main.py /path/to/directory --prefix "new_" --replace "old" "new" --start-number 1
   ```

### GUI Usage

1. **Run the GUI Application**: Execute the `file_renamer_gui.py` script to launch the GUI version.
   ```bash
   python file_renamer_gui.py
   ```

2. **Use the GUI**:
   - **Select Directory**: Click "Select Directory" to choose the directory containing files to rename.
   - **Enter Details**: Fill in the fields for prefix, old substring, new substring, and start number as needed.
   - **Rename Files**: Click "Rename Files" to apply the changes. A success message will be displayed upon completion.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided with the application.

---

This manual provides a comprehensive guide to installing and using the CLI File Renamer application. Follow the instructions carefully to ensure a smooth experience.