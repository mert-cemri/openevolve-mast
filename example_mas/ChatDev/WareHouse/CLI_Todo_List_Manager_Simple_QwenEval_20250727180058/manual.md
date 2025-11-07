# ChatDev To-Do List Manager

## Quick Overview

The ChatDev To-Do List Manager is a simple Command Line Interface (CLI) application designed to help you manage your daily tasks efficiently. You can add, view, mark as complete, and remove tasks. All tasks are stored in a text file, ensuring your data is preserved between sessions.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps to Install

1. **Clone the Repository** (if you haven't already):

   ```bash
   git clone https://github.com/your-repo/chatdev-todo-manager.git
   cd chatdev-todo-manager
   ```

2. **Install Dependencies**:

   This project does not require any external dependencies. However, you can ensure all dependencies are installed by running:

   ```bash
   pip install -r requirements.txt
   ```

   Since the `requirements.txt` file is empty, this command will not install any additional packages.

## How to Use

### Running the Application

To start the To-Do List Manager, run the following command in your terminal:

```bash
python main.py
```

### Main Functions

1. **Add Task**:
   - Enter `1` when prompted.
   - Provide a description for the task.
   - The task will be added to your list and saved to `tasks.txt`.

2. **View Tasks**:
   - Enter `2` when prompted.
   - The application will display all tasks, indicating whether each task is pending or done.

3. **Mark Task as Complete**:
   - Enter `3` when prompted.
   - Provide the task ID (number) of the task you want to mark as complete.
   - The task's status will be updated to "Done" and saved to `tasks.txt`.

4. **Remove Task**:
   - Enter `4` when prompted.
   - Provide the task ID (number) of the task you want to remove.
   - The task will be deleted from your list and `tasks.txt` will be updated accordingly.

5. **Exit**:
   - Enter `5` when prompted.
   - The application will terminate, and any changes will be saved to `tasks.txt`.

### Example Workflow

1. **Add a Task**:
   ```
   To-Do List Manager
   1. Add Task
   2. View Tasks
   3. Mark Task as Complete
   4. Remove Task
   5. Exit
   Enter your choice: 1
   Enter task description: Buy groceries
   Task added successfully.
   ```

2. **View Tasks**:
   ```
   To-Do List Manager
   1. Add Task
   2. View Tasks
   3. Mark Task as Complete
   4. Remove Task
   5. Exit
   Enter your choice: 2
   1. [Pending] Buy groceries
   ```

3. **Mark Task as Complete**:
   ```
   To-Do List Manager
   1. Add Task
   2. View Tasks
   3. Mark Task as Complete
   4. Remove Task
   5. Exit
   Enter your choice: 3
   Enter task ID to mark as complete: 1
   Task marked as complete.
   ```

4. **Remove Task**:
   ```
   To-Do List Manager
   1. Add Task
   2. View Tasks
   3. Mark Task as Complete
   4. Remove Task
   5. Exit
   Enter your choice: 4
   Enter task ID to remove: 1
   Task 'Buy groceries' removed successfully.
   ```

5. **Exit**:
   ```
   To-Do List Manager
   1. Add Task
   2. View Tasks
   3. Mark Task as Complete
   4. Remove Task
   5. Exit
   Enter your choice: 5
   Exiting...
   ```

## File Structure

- `main.py`: The main entry point of the application. Handles user input and interacts with the `TaskManager`.
- `task_manager.py`: Manages all operations related to tasks, including adding, viewing, marking as complete, and removing tasks.
- `file_handler.py`: Handles reading from and writing to the `tasks.txt` file.
- `tasks.txt`: Stores all tasks in JSON format.

## Troubleshooting

- **Invalid Task ID**: If you enter an invalid task ID when marking a task as complete or removing a task, the application will prompt you to enter a valid task number.
- **File Errors**: If there are issues reading from or writing to `tasks.txt`, the application will display an error message.

## Conclusion

The ChatDev To-Do List Manager is a simple yet powerful tool to help you manage your tasks efficiently. With its intuitive CLI interface, you can easily add, view, mark, and remove tasks, all while keeping your data stored in a text file for easy access and preservation.

If you have any questions or need further assistance, feel free to reach out to our support team.

---

This manual should provide a comprehensive guide for users to understand and use the ChatDev To-Do List Manager effectively.