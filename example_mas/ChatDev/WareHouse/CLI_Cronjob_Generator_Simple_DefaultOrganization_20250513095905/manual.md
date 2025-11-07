```
# CLI Cronjob Generator

A user-friendly command-line interface (CLI) tool for generating cron job schedules. This tool allows you to easily create common cron job schedules and outputs the corresponding crontab line.

## Quick Install

This project does not require any external dependencies. Simply clone the repository and run the script.

```bash
git clone <repository-url>
cd <repository-directory>
```

## 🤔 What is this?

The CLI Cronjob Generator is designed to simplify the process of creating cron job schedules. Cron jobs are scheduled tasks in Unix-based systems that run at specified intervals. This tool provides a straightforward way to generate cron expressions for common schedules such as:

- Daily at 3 AM
- Every 15 minutes
- Every hour
- Weekly on Sunday

Additionally, it allows for custom cron expressions to be specified.

## 📖 How to Use

### Running the Application

To run the CLI Cronjob Generator, navigate to the directory containing the `main.py` file and execute the following command:

```bash
python main.py <schedule>
```

### Available Schedules

The following predefined schedules are available:

- `daily_3am`: Runs daily at 3 AM
- `every_15_minutes`: Runs every 15 minutes
- `every_hour`: Runs every hour
- `weekly_sunday`: Runs weekly on Sunday

Example usage:

```bash
python main.py daily_3am
```

This command will output the cron expression for running a job daily at 3 AM.

### Custom Cron Expressions

If you need to specify a custom cron expression, you can use the `--custom` flag:

```bash
python main.py --custom "*/5 * * * *"
```

This command will output the custom cron expression you provided.

### Output

The application will print the cron expression to the console. For example:

```
Cron Expression: 0 3 * * *
```

This output represents the cron expression for the selected schedule.

## 📚 Documentation

For more detailed information on cron expressions and how they work, please refer to the [crontab documentation](https://man7.org/linux/man-pages/man5/crontab.5.html).

```