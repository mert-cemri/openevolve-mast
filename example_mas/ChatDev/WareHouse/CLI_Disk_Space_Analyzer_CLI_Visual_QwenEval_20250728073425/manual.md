# CLI Disk Space Analyzer

## Quick Install

To install the CLI Disk Space Analyzer, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the source code. Then, navigate to the project directory and install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

Note: Since the provided code does not list any external dependencies, the `requirements.txt` file might be empty or non-existent. If there are any dependencies, they should be listed there.

## 🤔 What is this?

The CLI Disk Space Analyzer is a command-line tool that helps you analyze disk usage within a specified directory. It provides a detailed breakdown of disk usage, showing the largest files and folders. This tool is useful for identifying disk space hogs and managing storage efficiently.

## 📖 Documentation

### Main Functions

1. **Analyze Disk Usage:**
   - The tool recursively analyzes the specified directory and calculates the size of each file and folder.
   - It caches folder sizes to improve performance when analyzing large directories.

2. **Identify Largest Files and Folders:**
   - The tool can list the largest files and folders within the directory, sorted by size.
   - By default, it shows the top 10 largest files and folders, but you can specify a different limit.

3. **Human-Readable Output:**
   - Disk sizes are displayed in a human-readable format (e.g., KB, MB, GB).

### How to Use

1. **Run the Tool:**
   - Open a terminal or command prompt.
   - Navigate to the directory where the `main.py` script is located.
   - Run the script with the path to the directory you want to analyze as an argument:

     ```bash
     python main.py /path/to/directory
     ```

2. **Example:**
   - To analyze the disk usage of the `/home/user/Documents` directory, you would run:

     ```bash
     python main.py /home/user/Documents
     ```

3. **Output:**
   - The tool will print the total size of the directory.
   - It will then list the largest files and folders, showing their paths and sizes in a human-readable format.

### Error Handling

- **Invalid Directory Path:**
  - If the specified directory does not exist, the tool will print an error message and exit.
  
- **Permission Denied:**
  - If the tool does not have permission to access the specified directory, it will print an error message and exit.

## 🛠️ Development

If you want to contribute to the project or modify the source code, you can clone the repository from GitHub:

```bash
git clone https://github.com/your-username/cli-disk-space-analyzer.git
```

Navigate to the project directory and install the dependencies as described in the "Quick Install" section.

## 🙋‍♂️ Support

If you encounter any issues or have suggestions for improvements, please feel free to open an issue on the [GitHub repository](https://github.com/your-username/cli-disk-space-analyzer/issues).

---

This manual provides a comprehensive overview of the CLI Disk Space Analyzer, including installation instructions, main functions, usage examples, and error handling. It should help users get started with the tool and make the most of its features.