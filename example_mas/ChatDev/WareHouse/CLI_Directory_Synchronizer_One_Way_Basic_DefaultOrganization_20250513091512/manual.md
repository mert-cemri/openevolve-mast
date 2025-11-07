```markdown
# Directory Synchronizer

A simple application to synchronize files from a source directory to a target directory. This application ensures that new or modified files in the source directory are copied to the target directory without deleting any files from the target.

## Main Functions

- **One-Way Synchronization**: Copies new or modified files from the source directory to the target directory. It does not delete files from the target directory if they are removed from the source.
- **Graphical User Interface (GUI)**: Provides an easy-to-use interface for selecting source and target directories and initiating the synchronization process.

## Installation

### Prerequisites

- **Python 3.6 or higher**: Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Environment Setup

1. **Clone the Repository**: Clone the project repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Install the required dependencies using pip.

   ```bash
   pip install -r requirements.txt
   ```

   Ensure that your Python version is 3.6 or higher as specified in the `requirements.txt`.

## How to Use

1. **Run the Application**: Execute the main script to start the application.

   ```bash
   python main.py
   ```

2. **Select Directories**:
   - Click on "Select Source Directory" to choose the directory from which files will be synchronized.
   - Click on "Select Target Directory" to choose the directory where files will be copied.

3. **Synchronize**:
   - After selecting both directories, click on the "Synchronize" button to start the synchronization process.
   - A message box will confirm the completion of the synchronization.

## Troubleshooting

- **Tkinter Errors**: If you encounter errors related to Tkinter, ensure that you have a display environment set up. For remote servers, consider using X11 forwarding.
- **Permission Issues**: Ensure that you have the necessary permissions to read from the source directory and write to the target directory.

## Additional Information

For further assistance or to report issues, please contact our support team or visit our [GitHub repository](<repository-url>) for more information.

```