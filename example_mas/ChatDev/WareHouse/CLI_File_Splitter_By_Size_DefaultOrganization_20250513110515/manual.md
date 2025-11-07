```markdown
# File Splitter CLI Utility

A command-line interface (CLI) utility to split large files into smaller parts of a specified size. This tool is designed to help users manage large files by breaking them down into more manageable chunks, which can be useful for storage, transfer, or processing.

## Main Functions

- **File Splitting:** The utility splits a specified file into smaller parts based on the user-defined chunk size.
- **Sequential Naming:** The output parts are named sequentially to ensure easy identification and reassembly.
- **Custom Output Directory:** Users can specify a directory where the split files will be saved.

## Quick Install

To use the File Splitter CLI utility, you need to have Python installed on your system. The utility requires Python version 3.6 or higher.

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
```

### Step 2: Install Environment Dependencies

Navigate to the project directory and install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

This will ensure that your environment is set up with the necessary Python version.

## How to Use

Once the environment is set up, you can use the File Splitter CLI utility by following these steps:

### Step 1: Navigate to the Project Directory

Open your terminal and navigate to the directory where the project is located.

### Step 2: Run the Utility

Use the following command to run the utility:

```bash
python main.py <file_path> <chunk_size> [--output_dir <output_directory>]
```

- `<file_path>`: The path to the file you want to split.
- `<chunk_size>`: The size of each chunk in megabytes (MB).
- `--output_dir <output_directory>`: (Optional) The directory where the split files will be saved. If not specified, the current directory is used by default.

### Example

To split a file named `largefile.txt` into 10MB chunks and save the parts in the current directory, use:

```bash
python main.py largefile.txt 10
```

To specify an output directory, use:

```bash
python main.py largefile.txt 10 --output_dir /path/to/output
```

## Error Handling

- **Invalid File Path:** If the specified file path does not exist, an error message will be displayed.
- **Invalid Output Directory:** If the specified output directory does not exist, an error message will be displayed.

## Documentation

For more detailed information on the utility's functionality and code structure, please refer to the source code files `main.py` and `file_splitter_logic.py`.

This utility is designed to be simple yet effective, providing a straightforward solution for splitting large files into smaller, manageable parts. Enjoy using the File Splitter CLI Utility!
```