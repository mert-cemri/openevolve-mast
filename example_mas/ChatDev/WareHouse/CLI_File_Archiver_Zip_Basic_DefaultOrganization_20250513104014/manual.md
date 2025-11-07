# CLI File Archiver

A simple command-line interface (CLI) application for creating and extracting ZIP archives. This tool allows users to easily compress files and directories into ZIP files and extract contents from existing ZIP archives.

## Quick Install

To get started with the CLI File Archiver, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository and install the necessary dependencies.

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/cli-file-archiver.git
cd cli-file-archiver
```

### Step 2: Install Dependencies

This application requires the `tkinter` library for the optional GUI component, which is included with standard Python installations. However, if you encounter any issues, you can install it using:

```bash
sudo apt-get install python3-tk
```

For other dependencies, you can use:

```bash
pip install -r requirements.txt
```

## 🤔 What is this?

The CLI File Archiver is a straightforward tool designed to manage ZIP archives through a command-line interface. It supports:

- Creating ZIP archives from files and directories.
- Extracting contents from existing ZIP archives.

This tool is ideal for users who prefer using the command line for file management tasks.

## 📖 How to Use

### Running the Application

To start the application, navigate to the directory where the files are located and run:

```bash
python main.py
```

### Main Functions

1. **Create ZIP Archive**

   - Enter the command `create` when prompted.
   - Input the name of the ZIP file you wish to create.
   - Provide a comma-separated list of files and directories to include in the ZIP archive.
   - The application will create the ZIP file with the specified contents.

2. **Extract ZIP Archive**

   - Enter the command `extract` when prompted.
   - Input the name of the ZIP file you wish to extract.
   - Specify the directory where you want the contents to be extracted.
   - The application will extract the contents of the ZIP file to the specified directory.

3. **Exit the Application**

   - Enter the command `exit` to close the application.

### Optional GUI

For users who prefer a graphical interface, a simple GUI is available using `tkinter`. To run the GUI:

```bash
python gui.py
```

- Use the "Create ZIP" button to select files and create a ZIP archive.
- Use the "Extract ZIP" button to select a ZIP file and extract its contents.

## 📖 Documentation

For more detailed documentation and examples, please refer to the [official documentation](https://github.com/yourusername/cli-file-archiver/wiki).

## Support

If you encounter any issues or have questions, please open an issue on the [GitHub repository](https://github.com/yourusername/cli-file-archiver/issues).

---

This user manual provides a comprehensive guide to installing and using the CLI File Archiver. Whether you prefer command-line operations or a graphical interface, this tool offers a simple and effective solution for managing ZIP archives.