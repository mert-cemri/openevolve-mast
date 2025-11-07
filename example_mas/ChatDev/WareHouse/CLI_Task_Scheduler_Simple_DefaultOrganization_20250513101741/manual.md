```markdown
# CLI Task Scheduler

A simple command-line interface (CLI) task scheduler that allows users to add tasks with a specific execution time. The tool executes a specified command when the time is reached and stores tasks in a simple text file.

## Main Functions

- **Add Tasks**: Users can add tasks specifying a command to execute at a particular date and time.
- **View Tasks**: Users can view all scheduled tasks.
- **Execute Commands**: The scheduler automatically executes the specified command at the scheduled time.
- **Graphical User Interface (GUI)**: Provides a GUI for users who prefer a visual interface to add and manage tasks.

## Installation

### Environment Setup

1. **Python Installation**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the project repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Dependencies**: There are no external dependencies required for this project, as specified in the `requirements.txt` file.

## How to Use

### Running the Application

1. **Navigate to the Project Directory**: Open your terminal or command prompt and navigate to the project directory.

   ```bash
   cd <repository-directory>
   ```

2. **Start the Application**: Run the main Python script to start the CLI Task Scheduler.

   ```bash
   python main.py
   ```

### Using the CLI

- **Add a New Task**: Select option 1 to add a new task. You will be prompted to enter the command, date (YYYY-MM-DD), and time (HH:MM).

- **View All Tasks**: Select option 2 to view all scheduled tasks. The tasks will be displayed with their scheduled execution time.

- **Open GUI**: Select option 3 to open the graphical user interface for managing tasks.

- **Exit**: Select option 4 to exit the application.

### Using the GUI

1. **Open GUI**: From the CLI, select option 3 to open the GUI.

2. **Add Task**: Enter the command, date, and time in the respective fields and click "Add Task" to schedule it.

3. **View Tasks**: The list of scheduled tasks will be displayed in the task list section of the GUI.

## Additional Information

- **Task Storage**: Tasks are stored in a simple text file named `tasks.txt` in the project directory. This file is used to load tasks when the application starts.

- **Execution**: The application uses threading to handle task execution, ensuring that commands are executed at the specified time without blocking the main application.

- **Error Handling**: If a task is scheduled for a time in the past, the application will notify the user and not schedule the task.

For any further assistance or inquiries, please contact our support team.

```