# ChatDev CLI Pomodoro Timer

## Introduction

The ChatDev CLI Pomodoro Timer is a command-line interface application designed to help you manage your time effectively using the Pomodoro Technique. This technique involves working in focused intervals, traditionally 25 minutes in length, separated by short breaks, typically 5 minutes. The application allows you to start, stop, reset, and exit the timer, with configurable durations and session notifications.

## Quick Install

To install the ChatDev CLI Pomodoro Timer, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository and install the required dependencies using pip:

1. Clone the repository:
   ```bash
   git clone https://github.com/ChatDev/pomodoro-timer.git
   cd pomodoro-timer
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🤔 What is this?

The ChatDev CLI Pomodoro Timer is a simple yet powerful tool that leverages the Pomodoro Technique to enhance your productivity. It provides a straightforward interface to manage your work and break sessions, making it easy to stay focused and avoid burnout.

## 📖 Documentation

### Main Functions

- **Start**: Begins a new work session or break session.
- **Stop**: Pauses the current session.
- **Reset**: Stops the timer and resets it to the initial work duration.
- **Exit**: Closes the application.

### Configurable Durations

You can specify custom durations for work and break sessions using command-line arguments:

- `--work`: Sets the work duration in minutes (default: 25).
- `--break`: Sets the break duration in minutes (default: 5).

Example:
```bash
python main.py --work 30 --break 10
```

### Notifications

When a session or break completes, the application will display a notification. The notification method depends on your operating system:

- **macOS**: Uses `osascript` to display a notification.
- **Linux**: Uses `notify-send` to display a notification.
- **Windows**: Uses the `plyer` library to display a notification. If `plyer` is not installed, the application will prompt you to install it.

### How to Use

1. **Start the Application**:
   ```bash
   python main.py
   ```

2. **Enter Commands**:
   - `start`: Begins a new work session or break session.
   - `stop`: Pauses the current session.
   - `reset`: Stops the timer and resets it to the initial work duration.
   - `exit`: Closes the application.

Example session:
```bash
Pomodoro Timer CLI
Commands: start, stop, reset, exit
Enter command: start
Timer started.
Time remaining: 24:59
Time remaining: 24:58
...
Enter command: stop
Timer stopped.
Enter command: reset
Timer reset.
Enter command: exit
```

## 🛠️ Dependencies

The ChatDev CLI Pomodoro Timer requires the following dependencies:

- `plyer` (only for Windows notifications)

You can install these dependencies using pip:

```bash
pip install -r requirements.txt
```

## 🙌 Contributing

We welcome contributions to the ChatDev CLI Pomodoro Timer! If you have any ideas or improvements, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/ChatDev/pomodoro-timer).

## 📝 License

The ChatDev CLI Pomodoro Timer is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

This manual should provide a comprehensive guide for users to understand and use the ChatDev CLI Pomodoro Timer effectively.