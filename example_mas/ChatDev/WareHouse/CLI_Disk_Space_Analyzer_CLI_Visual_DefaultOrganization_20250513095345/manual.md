```markdown
# Disk Space Analyzer

A command-line interface (CLI) application that provides a detailed breakdown of disk usage within a directory, showing the largest files and folders.

## Introduction

The Disk Space Analyzer is designed to help users understand the disk usage of directories on their system. By analyzing the size of files and folders, it provides a detailed, text-based breakdown of disk usage, highlighting the largest files and directories. This tool is particularly useful for identifying space hogs and managing disk space efficiently.

## Main Functions

- **Analyze Directory**: Scans a specified directory and calculates the size of each file and folder within it.
- **Display Largest Items**: Lists the largest files and directories, allowing users to quickly identify which items are consuming the most space.
- **Error Handling**: Gracefully handles errors encountered during file access, ensuring the application continues to run smoothly.

## Installation

Before using the Disk Space Analyzer, ensure that you have Python installed on your system. You will also need to install the required dependencies.

### Quick Install

1. **Clone the Repository**: Download the source code to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Use pip to install the necessary Python packages.
   ```bash
   pip install -r requirements.txt
   ```

   This will install the `humanize` package, which is used for formatting file sizes in a human-readable format.

## Usage

To use the Disk Space Analyzer, run the following command in your terminal:

```bash
python main.py <directory> [-n NUMBER]
```

- `<directory>`: The directory you want to analyze.
- `-n NUMBER`: (Optional) The number of largest items to display. Default is 10.

### Example

To analyze the `/home/user/documents` directory and display the 5 largest items, use:

```bash
python main.py /home/user/documents -n 5
```

## Documentation

For more detailed information about the Disk Space Analyzer, please refer to the `readme.md` file included in the repository. It contains additional details on the application's functionality and usage.

## Support

If you encounter any issues or have questions about using the Disk Space Analyzer, please feel free to reach out to our support team or open an issue on our GitHub repository.

```