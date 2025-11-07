```markdown
# File Joiner CLI Application

A command-line interface (CLI) application to join multiple file parts back into a single original file. This application is designed for users who have split files into parts and need to reassemble them.

## Main Functions

- **Join File Parts**: The application takes the first part of a file as input and joins all subsequent parts to recreate the original file. The parts must follow a naming convention with a `.part` suffix followed by a number (e.g., `file.part1`, `file.part2`, etc.).

## Installation

### Prerequisites

- **Python 3.x**: Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory**:
   ```bash
   cd <project-directory>
   ```
   Replace `<project-directory>` with the name of the cloned repository.

3. **Install Dependencies**: Install any required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
   Ensure that a `requirements.txt` file is present in the project directory listing all necessary dependencies.

## How to Use

### Command-Line Interface (CLI)

1. **Run the Application**: Execute the main script with the required arguments:
   ```bash
   python main.py <first_part_name> <output_file_name>
   ```
   - `<first_part_name>`: The name of the first part of the file you want to join.
   - `<output_file_name>`: The desired name for the output file.

2. **Example**:
   ```bash
   python main.py file.part1 original_file.txt
   ```
   This command will join all parts starting from `file.part1` and create a file named `original_file.txt`.

### Graphical User Interface (GUI)

1. **Run the GUI**: Execute the GUI script to launch the application with a graphical interface:
   ```bash
   python gui.py
   ```

2. **Using the GUI**:
   - **Select the First Part**: Click on the "Browse" button to select the first part of the file.
   - **Enter Output File Name**: Type the desired name for the output file in the provided entry field.
   - **Join Files**: Click the "Join" button to start the joining process. A success message will appear once the files are joined successfully.

## Troubleshooting

- Ensure that all file parts are present and named correctly according to the `.part` suffix convention.
- Verify that Python and all dependencies are installed correctly.
- If an error occurs, check the console or message box for specific error messages and resolve any issues accordingly.

## Support

For further assistance, please contact our support team or refer to the documentation provided within the repository.

```