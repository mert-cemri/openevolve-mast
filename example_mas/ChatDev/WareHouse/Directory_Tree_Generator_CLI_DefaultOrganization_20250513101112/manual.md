# Directory Tree CLI Utility

This CLI utility is designed to generate a visual tree structure of a given directory. It represents directories and files, indenting subdirectories and their contents. Users can specify a maximum depth for the tree, allowing for customizable views of directory structures.

## Main Functions

- **Generate Tree Structure**: The utility scans a specified directory and outputs a visual tree structure, showing all files and subdirectories.
- **Depth Limitation**: Users can specify a maximum depth to limit how deep the tree structure should go, providing flexibility in viewing nested directories.

## Quick Install

This project does not require any external dependencies, making it straightforward to set up and run.

### Prerequisites

- Python 3.x

### Installation

1. **Clone the Repository**: Clone the project repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up Environment**: Ensure Python is installed on your system. No additional packages are required as per the `requirements.txt`.

## How to Use

### Running the Utility

1. **Navigate to the Project Directory**: Open your terminal and navigate to the directory where the project is located.

2. **Execute the CLI Utility**: Run the following command to generate a tree structure of a directory.
   ```bash
   python main.py <directory-path> [--max-depth <depth>]
   ```

   - `<directory-path>`: The path to the directory you want to visualize.
   - `--max-depth <depth>`: (Optional) Specify the maximum depth of the tree. If not provided, the tree will display all levels.

### Example Usage

- To generate a tree structure for the directory `/home/user/documents` with no depth limit:
  ```bash
  python main.py /home/user/documents
  ```

- To generate a tree structure for the directory `/home/user/documents` with a maximum depth of 2:
  ```bash
  python main.py /home/user/documents --max-depth 2
  ```

### Output

The output will display the directory structure in a tree format, with each level of depth indented for clarity. Directories and files will be listed, and subdirectories will be further indented according to their depth.

## Troubleshooting

- **Permission Denied**: If you encounter a "Permission Denied" message, it indicates that the utility does not have permission to access certain directories. Ensure you have the necessary permissions to access the directory you are trying to visualize.

- **Invalid Path**: Ensure the directory path provided is correct and exists on your system.

## Conclusion

This CLI utility provides a simple yet powerful way to visualize directory structures, making it easier to understand and navigate complex file systems. With the ability to limit the depth of the tree, users can tailor the output to their specific needs.