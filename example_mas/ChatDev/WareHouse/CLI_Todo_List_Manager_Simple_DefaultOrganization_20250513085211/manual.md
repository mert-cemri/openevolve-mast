```markdown
# To-Do List Manager

A simple command-line interface (CLI) application to manage your tasks efficiently.

## Introduction

The To-Do List Manager is a straightforward CLI application that allows users to manage their tasks through a command-line interface. Users can add tasks, view all tasks, mark tasks as complete, and remove tasks. All tasks are stored in a text file, ensuring persistence across sessions.

## Main Functions

1. **View Tasks**: Display all tasks with their status (Completed or Pending).
2. **Add Task**: Add a new task to your to-do list.
3. **Remove Task**: Remove a task from your list by specifying its number.
4. **Mark Task as Complete**: Mark a specific task as completed.
5. **Exit**: Exit the application.

## Installation

### Prerequisites

- Python 3.x installed on your machine.

### Environment Setup

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change your directory to the project folder.
   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**: There are no external packages required for this application. Ensure you have Python installed.

## How to Use

1. **Run the Application**: Execute the `main.py` file to start the application.
   ```bash
   python main.py
   ```

2. **Interact with the CLI**: Follow the on-screen menu to interact with your to-do list.
   - **View Tasks**: Press `1` to view all tasks.
   - **Add Task**: Press `2` and enter the task description when prompted.
   - **Remove Task**: Press `3` and enter the task number you wish to remove.
   - **Mark Task as Complete**: Press `4` and enter the task number you wish to mark as complete.
   - **Exit**: Press `5` to exit the application.

3. **Task Persistence**: All tasks are saved in `tasks.txt` in JSON format, allowing you to resume where you left off in subsequent sessions.

## Troubleshooting

- **Invalid Input**: If you enter an invalid choice or task number, the application will prompt you to try again.
- **File Not Found**: If `tasks.txt` does not exist, it will be created automatically.

## Conclusion

The To-Do List Manager is a simple yet effective tool for managing tasks directly from your command line. It is designed to be intuitive and easy to use, making task management a breeze.

```