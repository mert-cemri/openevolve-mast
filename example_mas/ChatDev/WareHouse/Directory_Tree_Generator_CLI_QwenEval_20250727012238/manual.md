# Directory Tree Generator CLI Utility

## Overview

The Directory Tree Generator CLI Utility is a Python-based tool designed to generate a visual tree structure of a given directory. It supports specifying a maximum depth for the tree, allowing users to control the level of detail in the output. This utility is particularly useful for developers, system administrators, and anyone who needs to visualize the structure of directories and files.

## Quick Install

To install the Directory Tree Generator CLI Utility, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the source code. Navigate to the directory containing the source code and run the following command to install the utility:

```bash
pip install -r requirements.txt
```

Since there are no third-party dependencies, this command will simply confirm that all requirements are met.

## 🤔 What is this?

The Directory Tree Generator CLI Utility is a command-line interface (CLI) tool that allows users to generate a visual representation of a directory's structure. This tool is particularly useful for:

- **Visualizing Project Structure:** Easily see the organization of files and directories in a project.
- **System Administration:** Quickly inspect the structure of directories on a server or local machine.
- **Learning and Education:** Help students and new developers understand directory structures.

## 📖 Documentation

### Main Functions

The main function of the Directory Tree Generator CLI Utility is to generate a visual tree structure of a given directory. It supports the following features:

- **Specify Directory Path:** Users can specify the path to the directory they want to visualize.
- **Maximum Depth:** Users can specify the maximum depth of the tree, allowing them to control the level of detail in the output.

### How to Use

1. **Open a Terminal or Command Prompt:**
   - Navigate to the directory containing the `main.py` file.

2. **Run the Utility:**
   - Use the following command to generate a directory tree:

     ```bash
     python main.py <directory_path> [--max-depth <depth>]
     ```

   - Replace `<directory_path>` with the path to the directory you want to visualize.
   - Replace `<depth>` with the maximum depth of the tree (optional).

3. **Examples:**

   - Generate a directory tree for the current directory:

     ```bash
     python main.py .
     ```

   - Generate a directory tree for a specific directory with a maximum depth of 2:

     ```bash
     python main.py /path/to/directory --max-depth 2
     ```

### Error Handling

- **Invalid Path:** If the specified path does not exist or is not a directory, the utility will raise a `ValueError` and print an error message.
- **Invalid Depth:** If the specified depth is not a valid integer, the utility will raise an `ArgumentTypeError` and print an error message.

## 🛠️ Development

If you are interested in contributing to the Directory Tree Generator CLI Utility, you can find the source code on [GitHub](https://github.com/your-repo/directory-tree-generator).

### Contributing

- **Fork the Repository:** Create a fork of the repository on GitHub.
- **Create a Branch:** Create a new branch for your feature or bug fix.
- **Make Changes:** Implement your changes and commit them.
- **Create a Pull Request:** Submit a pull request to the main repository.

## 🙏 Acknowledgments

- **Python:** The Directory Tree Generator CLI Utility is built using Python, a powerful and versatile programming language.
- **Open Source Community:** Thank you to the open source community for providing the tools and resources that make this utility possible.

## 📝 License

The Directory Tree Generator CLI Utility is released under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

Feel free to reach out if you have any questions or need further assistance!