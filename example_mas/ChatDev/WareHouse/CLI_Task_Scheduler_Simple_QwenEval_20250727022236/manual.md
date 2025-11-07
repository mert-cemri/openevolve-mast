# CLI Task Scheduler User Manual

## Introduction

The CLI Task Scheduler is a command-line utility designed to help users schedule and execute tasks at specific times. It allows you to add tasks with a specific execution time (e.g., HH:MM on a given date) and execute a specified command when the time is reached. Tasks are stored in a simple text file for persistence.

## Main Features

- **Add Tasks:** Schedule tasks with a specific date and time.
- **Execute Due Tasks:** Automatically execute tasks when their scheduled time is reached.
- **Persistent Storage:** Tasks are stored in a simple text file, ensuring they persist across sessions.
- **Graceful Shutdown:** The scheduler can be stopped gracefully using signals (SIGINT, SIGTERM).

## Quick Install

To install the CLI Task Scheduler, you need to have Python installed on your system. The project does not have any third-party dependencies, so you can clone the repository and run the script directly.

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-repository/cli-task-scheduler.git
   cd cli-task-scheduler
   ```

2. **Run the Scheduler:**

   You can run the scheduler directly using Python. Make sure you are in the project directory.

   ```bash
   python main.py
   ```

## Usage

### Adding a Task

To add a task, use the `--add` option followed by the date, time, and command. The date should be in the format `YYYY-MM-DD`, and the time should be in the format `HH:MM`.

**Example:**

```bash
python main.py --add 2023-12-25 15:30 "echo 'Merry Christmas!'"
```

This command schedules a task to execute the command `echo 'Merry Christmas!'` on December 25, 2023, at 15:30.

### Executing Due Tasks

To execute all due tasks, use the `--execute` option. This will check for any tasks that are due to be executed and run them.

**Example:**

```bash
python main.py --execute
```

### Running the Scheduler Continuously

The scheduler can be run continuously to periodically check for and execute due tasks. By default, it checks every minute.

**Example:**

```bash
python main.py
```

This command starts the scheduler, which will continuously check for and execute due tasks every minute.

### Graceful Shutdown

The scheduler can be stopped gracefully using signals (SIGINT, SIGTERM). You can stop the scheduler by pressing `Ctrl+C` in the terminal.

## Task File

Tasks are stored in a simple text file named `tasks.txt`. Each line in the file represents a task in the format:

```
YYYY-MM-DD HH:MM - command
```

For example:

```
2023-12-25 15:30 - echo 'Merry Christmas!'
2024-01-01 00:00 - echo 'Happy New Year!'
```

## Logging

The scheduler logs all actions to a file named `scheduler.log`. This log file can be useful for debugging and tracking the scheduler's behavior.

## Conclusion

The CLI Task Scheduler is a powerful tool for scheduling and executing tasks at specific times. With its simple command-line interface and persistent storage, it provides a reliable way to manage your tasks. If you have any questions or need further assistance, feel free to reach out to the support team.

---

This manual provides a comprehensive overview of the CLI Task Scheduler, including installation, usage, and troubleshooting. It should help users get started with the tool and make the most of its features.