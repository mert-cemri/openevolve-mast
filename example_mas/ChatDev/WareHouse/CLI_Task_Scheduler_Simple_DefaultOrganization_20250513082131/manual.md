# Task Scheduler CLI and GUI Application

Welcome to the Task Scheduler CLI and GUI application! This software allows users to schedule tasks to be executed at a specific time and date. The tasks are stored in a simple text file for persistence. This manual will guide you through the main functions of the software, how to install it, and how to use it effectively.

## Main Functions

The Task Scheduler application provides the following main functions:

1. **Add Task**: Users can add tasks specifying the date, time, and command to be executed.
2. **Execute Command**: The application will automatically execute the specified command at the scheduled time.
3. **Persistent Storage**: Tasks are stored in a text file (`tasks.txt`) to ensure they are not lost between sessions.
4. **CLI Interface**: A command-line interface for users who prefer terminal-based interaction.
5. **GUI Interface**: A graphical user interface built with Tkinter for users who prefer a visual interaction.

## Installation

### Prerequisites

- Python 3.x must be installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: First, clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change your directory to the project folder:
   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**: There are no external dependencies required for this project, as specified in the `requirements.txt` file. However, ensure that Python's standard libraries are available.

## Usage

### CLI Interface

1. **Run the Application**: Execute the following command in your terminal to start the CLI application:
   ```bash
   python main.py
   ```

2. **Add a Task**: Follow the on-screen instructions to add a task. You will be prompted to enter the date (YYYY-MM-DD), time (HH:MM), and the command to be executed.

3. **Exit the Application**: Choose the option to exit when you are done adding tasks.

### GUI Interface

1. **Run the GUI Application**: Execute the following command in your terminal to start the GUI application:
   ```bash
   python gui.py
   ```

2. **Add a Task**: Enter the date, time, and command in the respective fields and click the "Add Task" button. A message box will confirm the successful addition of the task.

3. **Close the Application**: Simply close the window when you are finished.

## Additional Information

- **Task Execution**: The application uses Python's `sched` module to schedule tasks and `subprocess` to execute commands.
- **Task Storage**: Tasks are stored in a `tasks.txt` file in the format `date,time,command`.
- **Threading**: The scheduler runs in a separate thread to allow continuous interaction with the user interface.

We hope this manual helps you effectively use the Task Scheduler application. If you encounter any issues or have further questions, please feel free to reach out for support.