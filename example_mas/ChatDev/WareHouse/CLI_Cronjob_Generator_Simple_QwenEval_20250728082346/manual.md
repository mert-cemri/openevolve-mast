# Cronjob Generator CLI

## Introduction

The Cronjob Generator CLI is a tool designed to simplify the creation of cron job schedules. It provides a user-friendly interface to generate crontab lines for common schedules, such as daily at 3 AM, every 15 minutes, and more. The tool supports both command-line interface (CLI) and graphical user interface (GUI) modes.

## Main Functions

### CLI Mode

- **Input**: Accepts a schedule as a command-line argument.
- **Output**: Generates and prints the corresponding crontab line.

### GUI Mode

- **Input**: Allows users to enter a schedule through a graphical interface.
- **Output**: Displays the generated crontab line in the GUI.

### Supported Schedules

- daily at 3 AM
- every 15 minutes
- weekly on Monday at 4 AM
- monthly on the 1st at 5 AM
- hourly
- every 5 minutes
- every 30 minutes
- daily at midnight
- daily at noon

## Installation

### Prerequisites

- **Go**: Ensure you have Go installed on your system. You can download it from [here](https://golang.org/dl/).

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/chatdev.git
   cd chatdev
   ```

2. **Install Dependencies**

   The project uses Go modules to manage dependencies. Ensure you have the `go.mod` file in the root directory. You can install the dependencies by running:

   ```bash
   go mod download
   ```

3. **Build the Application**

   Compile the application using the following command:

   ```bash
   go build -o cronjob-generator
   ```

   This will create an executable named `cronjob-generator`.

## Usage

### CLI Mode

To use the tool in CLI mode, run the executable with a schedule as an argument:

```bash
./cronjob-generator "daily at 3 AM"
```

This will output:

```
0 3 * * *
```

### GUI Mode

To use the tool in GUI mode, simply run the executable without any arguments:

```bash
./cronjob-generator
```

A window will appear, allowing you to enter a schedule and generate the corresponding crontab line.

### Supported Schedules

Here are the schedules you can use with the tool:

- `daily at 3 AM`
- `every 15 minutes`
- `weekly on Monday at 4 AM`
- `monthly on the 1st at 5 AM`
- `hourly`
- `every 5 minutes`
- `every 30 minutes`
- `daily at midnight`
- `daily at noon`

## Troubleshooting

### Invalid Schedule

If you enter an unsupported schedule, the tool will output an error message:

```
Invalid schedule. Please use one of the following: daily at 3 AM, every 15 minutes, weekly on Monday at 4 AM, monthly on the 1st at 5 AM, hourly, every 5 minutes, every 30 minutes, daily at midnight, daily at noon
```

### Dependency Issues

If you encounter issues with dependencies, ensure you have the `go.mod` file in the root directory and run:

```bash
go mod download
```

## Contributing

We welcome contributions to the Cronjob Generator CLI. If you have any ideas or improvements, feel free to open an issue or submit a pull request on [GitHub](https://github.com/yourusername/chatdev).

## License

The Cronjob Generator CLI is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This manual should provide a comprehensive guide for users to understand and use the Cronjob Generator CLI effectively.