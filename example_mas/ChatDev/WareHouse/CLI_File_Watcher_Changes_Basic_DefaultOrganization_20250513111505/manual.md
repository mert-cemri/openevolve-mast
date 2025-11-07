```markdown
# CLI File Watcher

A simple command-line interface (CLI) application to monitor file system changes in a specified directory. The application detects file creation, modification, and deletion events and prints notifications to the console.

## Main Functions

- **Monitor Directory**: Watch a specified directory for any file system changes.
- **Event Notifications**: Receive real-time notifications for file creation, modification, and deletion.
- **GUI Option**: A graphical user interface (GUI) is available for users who prefer a visual interface over the command line.

## Quick Install

To get started with the CLI File Watcher, you need to install the required dependencies. The application is built using Python, and the primary dependency is the `watchdog` library.

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Install Dependencies

Ensure you have Python installed on your system. Then, install the necessary Python packages using `pip`:

```bash
pip install -r requirements.txt
```

This command will install the `watchdog` library, which is essential for monitoring file system events.

## How to Use

### CLI Usage

1. **Run the Application**: Use the following command to start the file watcher from the command line:

   ```bash
   python main.py <directory_to_watch>
   ```

   Replace `<directory_to_watch>` with the path of the directory you want to monitor.

2. **Stop the Application**: To stop monitoring, simply interrupt the process using `Ctrl+C`.

### GUI Usage

For users who prefer a graphical interface, a simple GUI is available using `tkinter`.

1. **Run the GUI**: Execute the following command to start the GUI:

   ```bash
   python gui.py
   ```

2. **Select Directory**: Use the "Browse" button to select the directory you wish to monitor.

3. **Start/Stop Monitoring**: Click "Start Watching" to begin monitoring and "Stop Watching" to end the session.

## Documentation

For more detailed documentation and examples, please refer to the source code comments and the `README.md` file in the repository.

## Support

For any issues or questions, please contact our support team or open an issue in the repository.

```
