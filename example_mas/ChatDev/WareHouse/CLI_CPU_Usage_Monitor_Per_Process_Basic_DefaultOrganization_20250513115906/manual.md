```markdown
# CLI CPU Usage Monitor

A command-line interface (CLI) application to monitor CPU usage per process, similar to a simplified `top` command. It updates periodically and can focus on a specific process if a PID is given.

## Quick Install

To get started with the CLI CPU Usage Monitor, you need to install the required dependencies. The application is written in Python and requires the `psutil` library.

### Step 1: Install Python

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Install Dependencies

The application requires the `psutil` library. You can install it using pip:

```bash
pip install -r requirements.txt
```

This command will install the version specified in the `requirements.txt` file:

```
psutil==5.9.0
```

## 🤔 What is this?

The CLI CPU Usage Monitor is a tool designed to help users track CPU usage for all running processes or a specific process if a process ID (PID) is provided. This can be particularly useful for system administrators and developers who need to monitor system performance and resource usage.

## 📖 Main Functions

- **Monitor CPU Usage for All Processes**: By default, the application displays CPU usage for all running processes.
- **Focus on a Specific Process**: If a PID is provided, the application focuses on monitoring the CPU usage of that specific process.
- **Periodic Updates**: The application updates the CPU usage data every 2 seconds, providing real-time monitoring.

## How to Use

### Running the Application

To run the application, navigate to the directory containing `main.py` and execute the following command:

```bash
python main.py
```

### Monitoring a Specific Process

If you want to monitor a specific process, provide the PID using the `--pid` argument:

```bash
python main.py --pid <PID>
```

Replace `<PID>` with the actual process ID you wish to monitor.

### Output

The application displays the CPU usage data in a tabular format:

```
PID       Name                     CPU Usage (%)
--------------------------------------------------
1234      python                   5.0
5678      chrome                   12.5
```

The table updates every 2 seconds, providing a continuous view of CPU usage.

## Additional Information

- **Error Handling**: If a process with the specified PID does not exist, the application will notify you with a message: "No process found with PID <PID>".
- **Access Denied**: Some processes may not be accessible due to permission restrictions. These processes will be skipped in the output.

By using this CLI CPU Usage Monitor, you can effectively track and manage CPU usage on your system, ensuring optimal performance and resource allocation.
```