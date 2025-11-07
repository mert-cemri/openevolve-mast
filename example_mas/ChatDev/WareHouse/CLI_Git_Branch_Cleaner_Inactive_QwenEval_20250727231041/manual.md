# Git Branch Cleanup Tool User Manual

## Overview

The Git Branch Cleanup Tool is a command-line interface (CLI) application designed to help you manage your local Git branches by identifying branches that have been merged into the main/master branch and are inactive (based on the last commit date). It provides an option to delete these branches to keep your repository clean and organized.

## Main Functions

1. **List Merged Branches**: Identifies branches that have been merged into the main/master branch.
2. **List Inactive Branches**: Identifies branches that have not been committed to for a specified number of days (default is 30 days).
3. **Delete Branches**: Allows you to delete selected branches from your local repository.

## Installation

### Prerequisites

- Python 3.6 or higher
- Git installed and configured on your system

### Installing the Tool

1. **Clone the Repository**: First, clone the Git Branch Cleanup Tool repository from GitHub to your local machine.
   ```bash
   git clone https://github.com/ChatDev/git-branch-cleanup-tool.git
   cd git-branch-cleanup-tool
   ```

2. **Install Dependencies**: The tool requires the `subprocess` module, which is part of Python's standard library, so no additional dependencies need to be installed.

## Usage

### Running the Tool

To run the Git Branch Cleanup Tool, navigate to the directory where you cloned the repository and execute the following command:

```bash
python main.py --cli
```

### Command-Line Interface (CLI)

1. **List Branches**: When you run the tool, it will list all branches that can be deleted (merged and inactive branches).
   ```
   Branches that can be deleted:
    - feature-branch-1
    - feature-branch-2
    - old-feature-branch
   ```

2. **Delete Branches**: You can specify which branches to delete by entering their names separated by commas. If you do not want to delete any branches, simply press Enter.
   ```
   Enter branch names to delete (comma-separated, or press Enter to skip): feature-branch-1, old-feature-branch
   ```

3. **Validation**: The tool will validate the entered branch names and confirm if they are valid branches that can be deleted. If any invalid branch names are entered, the tool will display an error message and exit.

4. **Branch Deletion**: If all entered branch names are valid, the tool will delete them and confirm the deletion.

### Graphical User Interface (GUI)

The tool also includes a graphical user interface (GUI) for users who prefer a visual interface. To run the GUI, execute the following command:

```bash
python main.py
```

1. **Branch List**: The GUI will display a list of branches that can be deleted.
2. **Delete Branches**: You can select one or more branches from the list and click the "Delete Selected Branch" button to delete them.
3. **Confirmation**: The GUI will prompt you to confirm the deletion of each selected branch.

## Troubleshooting

- **Branch Not Found**: If you try to delete a branch that does not exist, the tool will display an error message.
- **Git Command Errors**: If there are issues with the Git commands executed by the tool, the tool will display an error message with details.

## Support

For any issues or questions, please contact the ChatDev support team at support@chatdev.com.

---

This manual provides a comprehensive guide on how to use the Git Branch Cleanup Tool, including installation, main functions, and usage instructions for both the CLI and GUI interfaces.