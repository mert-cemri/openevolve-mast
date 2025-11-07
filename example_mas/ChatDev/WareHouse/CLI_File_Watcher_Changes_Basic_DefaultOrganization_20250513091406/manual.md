```markdown
# CLI File Watcher

A command-line interface (CLI) application to monitor specified files or directories for changes such as creation, modification, and deletion, and print notifications to the console.

## Main Functions

The CLI File Watcher provides the following main functionalities:

- **File and Directory Monitoring**: Continuously monitors a specified file or directory for any changes.
- **Event Notifications**: Prints notifications to the console whenever a file is created, modified, or deleted.
- **Graphical User Interface (GUI)**: A simple GUI is available for users who prefer a visual interface over the command line.

## Quick Install

To use the CLI File Watcher, you need to install the required dependencies. The application is built using Python, and the primary dependency is the `watchdog` library.

### Installation Steps

1. **Clone the Repository**: First, clone the repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**: Use the `requirements.txt` file to install necessary packages.
   ```bash
   pip install -r requirements.txt
   ```

## How to Use

### Command-Line Interface

1. **Run the CLI Application**: Use the following command to start monitoring a file or directory.
   ```bash
   python main.py <path_to_watch>
   ```
   Replace `<path_to_watch>` with the path of the file or directory you want to monitor.

2. **Stop Monitoring**: To stop the monitoring process, simply interrupt the program using `Ctrl+C`.

### Graphical User Interface

1. **Run the GUI Application**: If you prefer using a GUI, execute the following command:
   ```bash
   python gui.py
   ```

2. **Using the GUI**:
   - Enter the path of the file or directory you wish to monitor in the text entry field.
   - Click "Start Watching" to begin monitoring.
   - Click "Stop Watching" to stop the monitoring process.

## Documentation

For more detailed documentation and examples, please refer to the source code comments and docstrings within each module. The application is designed to be straightforward and user-friendly, with clear instructions provided at each step.

## Support

For any issues or questions, please contact our support team or refer to the project's issue tracker on the repository.

```