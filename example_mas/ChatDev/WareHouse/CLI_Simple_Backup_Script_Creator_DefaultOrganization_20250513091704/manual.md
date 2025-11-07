# Backup Script Creator

A simple CLI tool to generate backup scripts using `rsync` or `tar`. This tool allows users to specify source directories and a target backup location, and it generates a shell script for backing up the specified directories.

## Quick Install

No external dependencies are required for this project. Ensure you have Python installed on your system.

## 🤔 What is this?

The Backup Script Creator is a command-line interface (CLI) tool designed to simplify the process of creating backup scripts. By specifying the source directories and a target backup location, users can generate a shell script that uses either `rsync` or `tar` for backing up files. This tool is ideal for users who need to automate their backup processes without manually writing scripts.

### Main Functions

- **Generate Backup Script with `rsync`:** Creates a shell script that uses `rsync` to copy files from the source directories to the target backup location.
- **Generate Backup Script with `tar`:** Creates a shell script that uses `tar` to archive files from the source directories into the target backup location.

## 📖 Documentation

### Getting Started

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Ensure Python is Installed:**

   Make sure you have Python installed on your system. You can verify this by running:

   ```bash
   python --version
   ```

3. **Run the Application:**

   You can run the application directly using the command:

   ```bash
   python main.py -s <source_directories> -t <target_directory> -m <method> -o <output_file>
   ```

   Replace `<source_directories>`, `<target_directory>`, `<method>`, and `<output_file>` with your desired values.

### How to Use

- **Specify Source Directories:**

  Use the `-s` or `--sources` option to list the directories you want to back up. You can specify multiple directories separated by space.

- **Specify Target Directory:**

  Use the `-t` or `--target` option to specify the directory where the backups will be stored.

- **Choose Backup Method:**

  Use the `-m` or `--method` option to choose between `rsync` and `tar` for the backup method.

- **Specify Output File:**

  Use the `-o` or `--output` option to specify the file where the generated script will be saved.

### Example Usage

To create a backup script using `rsync`:

```bash
python main.py -s /path/to/source1 /path/to/source2 -t /path/to/backup -m rsync -o backup_script.sh
```

To create a backup script using `tar`:

```bash
python main.py -s /path/to/source1 /path/to/source2 -t /path/to/backup -m tar -o backup_script.sh
```

### Resources

For more information on `rsync` and `tar`, you can refer to their respective documentation:

- [rsync Documentation](https://rsync.samba.org/documentation.html)
- [tar Documentation](https://www.gnu.org/software/tar/manual/tar.html)

This tool is designed to be simple and efficient, providing users with a quick way to automate their backup processes.