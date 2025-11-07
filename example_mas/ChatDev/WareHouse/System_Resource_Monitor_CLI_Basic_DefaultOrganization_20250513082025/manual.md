```markdown
# System Resource Monitor CLI Tool

A simple command-line interface (CLI) tool to monitor basic system resource usage, including CPU percentage, memory usage (total, used, free), and disk space (total, used, free for a specified partition or root). The tool updates the display every few seconds or on command.

## Main Functions

- **CPU Usage Monitoring**: Displays the current CPU usage percentage.
- **Memory Usage Monitoring**: Shows total, used, and free memory.
- **Disk Space Monitoring**: Provides total, used, and free disk space for a specified partition or root.
- **Automatic and Manual Updates**: Automatically updates every few seconds or updates on user command.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- `pip` package manager for Python.

### Quick Install

1. **Clone the Repository**: Clone the project repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Install the required Python packages using `pip`.

   ```bash
   pip install -r requirements.txt
   ```

   This will install the `psutil` library, which is necessary for monitoring system resources.

## How to Use

### Running the CLI Tool

1. **Navigate to the Project Directory**: Ensure you are in the directory where the project files are located.

2. **Execute the CLI Tool**: Run the main Python script to start the system resource monitor.

   ```bash
   python main.py
   ```

3. **Interact with the Tool**:
   - The tool will display the current CPU, memory, and disk usage.
   - Press `Enter` to manually update the display.
   - Type `exit` and press `Enter` to quit the application.

### Using the GUI (Optional)

For users who prefer a graphical interface, a simple GUI is available.

1. **Run the GUI Application**:

   ```bash
   python app_gui.py
   ```

2. **Interact with the GUI**:
   - The GUI will display the current CPU, memory, and disk usage.
   - Click "Update Now" to manually refresh the display.
   - Use the "Start Auto Update" button to toggle automatic updates every 5 seconds.

## Documentation

For further information and detailed documentation, please refer to the source code comments and function docstrings within the project files.

Feel free to reach out for support or to contribute to the project by submitting issues or pull requests on the project's GitHub repository.
```
