# Backup Script Creator

A user-friendly application to generate shell scripts for backing up directories using `rsync` or `tar`.

## Introduction

The Backup Script Creator is a graphical user interface (GUI) application designed to help users easily create shell scripts for backing up specified source directories to a target backup location. The application supports two popular backup methods: `rsync` and `tar`.

### Main Functions

- **Add Source Directories**: Select multiple directories that you want to back up.
- **Select Target Directory**: Choose the destination directory where backups will be stored.
- **Generate Rsync Script**: Create a shell script using `rsync` to perform the backup.
- **Generate Tar Script**: Create a shell script using `tar` to perform the backup.

## Installation

### Environment Setup

This application does not require any external dependencies beyond the standard Python library. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download the source code to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main application file.
   ```bash
   python main.py
   ```

## How to Use

1. **Launch the Application**: Run `main.py` to open the Backup Script Creator GUI.

2. **Add Source Directories**:
   - Click on "Add Source Directory".
   - Select the directories you wish to back up. You can add multiple directories.

3. **Select Target Directory**:
   - Click on "Select Target Directory".
   - Choose the directory where you want the backups to be stored.

4. **Generate Backup Script**:
   - To create a script using `rsync`, click "Generate Rsync Script".
   - To create a script using `tar`, click "Generate Tar Script".

5. **Save the Script**:
   - After generating the script, you will be prompted to save it. Choose a location and filename for your script.

6. **Execute the Script**:
   - The saved script can be executed in a terminal to perform the backup operation.

## Notes

- Ensure you have the necessary permissions to read from the source directories and write to the target directory.
- The application requires a graphical display environment to run. If you encounter issues related to display, ensure you have access to a graphical interface or use a virtual display.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided in the source code.

---

This manual provides a comprehensive guide to using the Backup Script Creator, ensuring users can effectively generate and utilize backup scripts with ease.