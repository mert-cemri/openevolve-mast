```markdown
# Directory Size Calculator CLI

A command-line utility to calculate and display the total size of a directory and its subdirectories in a human-readable format (e.g., KB, MB, GB).

## Overview

The Directory Size Calculator CLI is a simple yet powerful tool designed to help users quickly determine the total size of a directory and all its subdirectories. This utility is particularly useful for managing disk space and understanding the storage footprint of various directories on your system.

## Main Functions

- **Calculate Directory Size**: Recursively calculates the total size of a specified directory and its subdirectories.
- **Human-Readable Output**: Converts the size from bytes to a more understandable format such as KB, MB, or GB.

## Quick Install

Since this project does not require any external Python packages, you can simply clone the repository and run the script using Python.

### Prerequisites

- Python 3.x installed on your system.

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Script**:
   You can execute the script directly using Python. No additional installation steps are required.

## How to Use

1. **Navigate to the Project Directory**:
   Ensure you are in the directory where the `main.py` file is located.

2. **Run the CLI Utility**:
   Use the following command to calculate the size of a directory:
   ```bash
   python main.py <directory-path>
   ```
   Replace `<directory-path>` with the path to the directory you want to analyze.

3. **View the Output**:
   The utility will display the total size of the directory and its subdirectories in a human-readable format.

### Example

To calculate the size of a directory located at `/home/user/documents`, run:
```bash
python main.py /home/user/documents
```

The output will be similar to:
```
Total Size: 1.23 GB
```

## Troubleshooting

- **Error Handling**: If an error occurs during execution, the utility will print an error message. Ensure that the directory path is correct and accessible.
- **Permissions**: Make sure you have the necessary permissions to read the directory and its contents.

## Additional Information

For further assistance or to report issues, please contact our support team or visit our [GitHub repository](<repository-url>) for more information.

```
```