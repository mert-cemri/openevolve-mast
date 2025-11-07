# CLI Cronjob Generator

A user-friendly command-line interface (CLI) tool for generating common cron job schedules. This tool simplifies the process of creating cron expressions for scheduling tasks in Unix-based systems.

## Main Functions

The CLI Cronjob Generator provides an easy way to generate cron expressions for the following common schedules:

- **Daily at 3 AM**: Schedule a task to run every day at 3 AM.
- **Every 15 Minutes**: Schedule a task to run every 15 minutes.
- **Hourly**: Schedule a task to run at the start of every hour.
- **Weekly**: Schedule a task to run once a week at midnight on Sunday.

## Installation

### Prerequisites

- **Python 3.x**: Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: Clone the project repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: This project does not require any external dependencies, so you can skip this step.

## How to Use

1. **Navigate to the Project Directory**: Open your terminal and navigate to the directory where the project is located.

   ```bash
   cd <repository-directory>
   ```

2. **Run the CLI Tool**: Use the following command to run the CLI tool and generate a cron expression based on your desired schedule.

   ```bash
   python main.py <schedule>
   ```

   Replace `<schedule>` with one of the following options:

   - `daily_3am`
   - `every_15_minutes`
   - `hourly`
   - `weekly`

   Example:

   ```bash
   python main.py daily_3am
   ```

   This will output:

   ```
   Cron Expression: 0 3 * * *
   ```

3. **Use the Generated Cron Expression**: Copy the generated cron expression and use it in your crontab file to schedule your tasks.

## Additional Information

- **Cron Expressions**: Cron expressions are used to schedule tasks in Unix-based systems. They consist of five fields representing minute, hour, day of the month, month, and day of the week.

- **Documentation**: For more information on cron expressions and how to use them, refer to the [cron documentation](https://en.wikipedia.org/wiki/Cron).

This tool is designed to simplify the process of creating cron expressions, making it accessible even for users who are not familiar with the syntax. Enjoy scheduling your tasks effortlessly!