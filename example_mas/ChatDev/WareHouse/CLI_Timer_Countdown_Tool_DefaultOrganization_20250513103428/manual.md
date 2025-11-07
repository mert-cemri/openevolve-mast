# CLI Timer and Countdown Tool

Welcome to the CLI Timer and Countdown Tool, a simple command-line application designed to help you manage your time effectively. This tool allows you to start a timer that counts up from zero or a countdown from a specified duration, notifying you when the countdown is complete.

## Main Functions

- **Timer**: Counts up from zero, displaying the elapsed time in hours, minutes, and seconds.
- **Countdown**: Counts down from a user-specified duration (e.g., 5m, 1h30s), notifying you when the countdown is complete.

## Installation

### Prerequisites

- Ensure you have Python 3.6 or higher installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory**

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the name of the cloned directory.

3. **Install Dependencies**

   Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## How to Use

### Starting the Timer

To start the timer, open your terminal, navigate to the project directory, and run the following command:

```bash
python main.py --timer
```

The timer will start counting up from zero, displaying the elapsed time in the format `HH:MM:SS`. To stop the timer, press `Ctrl + C`.

### Starting the Countdown

To start a countdown, specify the duration using the `--countdown` flag followed by the desired time. For example, to start a countdown for 5 minutes, use the following command:

```bash
python main.py --countdown 5m
```

You can specify the duration in hours, minutes, and seconds (e.g., `1h30s` for 1 hour and 30 seconds). The countdown will display the remaining time in the format `HH:MM:SS`. When the countdown reaches zero, you will be notified with a message. To stop the countdown prematurely, press `Ctrl + C`.

## Additional Information

- **Time Format**: The tool supports time input in hours (`h`), minutes (`m`), and seconds (`s`). You can combine these units to specify complex durations (e.g., `2h15m30s`).

- **Notifications**: Notifications are displayed directly in the console output. When the countdown is complete, a message will appear to inform you.

We hope this tool helps you manage your time more effectively. If you have any questions or need further assistance, please feel free to reach out.