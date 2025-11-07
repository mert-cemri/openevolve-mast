# CPU Usage Monitor CLI Application

## Overview

The CPU Usage Monitor CLI Application is a tool designed to monitor and display the CPU usage of processes running on your system. It provides a simplified interface similar to the `top` command, updating periodically. You can focus on a specific process by providing its Process ID (PID).

## Quick Install

To use the CPU Usage Monitor, you need to have Python installed on your system. The application uses the `psutil` library for system monitoring, which can be installed via pip.

### Install Dependencies

```bash
pip install psutil
```

## 🤔 What is this?

The CPU Usage Monitor CLI Application is a command-line tool that allows you to monitor the CPU usage of processes on your system. It can be used to identify processes that are consuming a significant amount of CPU resources, helping you to optimize system performance or troubleshoot issues.

## 📖 Documentation

### Main Functions

- **Monitor All Processes**: By default, the application will monitor and display the CPU usage of all processes running on your system.
- **Focus on a Specific Process**: You can focus on a specific process by providing its PID. The application will then display the CPU usage of only that process.
- **Periodic Updates**: The application updates the CPU usage data at a specified interval (default is 1 second).

### How to Use

#### Basic Usage

To start monitoring all processes, simply run the application without any arguments:

```bash
python main.py
```

#### Monitor a Specific Process

To monitor a specific process, provide its PID using the `--pid` argument:

```bash
python main.py --pid <PID>
```

Replace `<PID>` with the Process ID of the process you want to monitor.

#### Change Update Interval

To change the update interval, use the `--interval` argument:

```bash
python main.py --interval <seconds>
```

Replace `<seconds>` with the desired update interval in seconds. The default interval is 1 second.

### Example Usage

1. **Monitor All Processes with Default Interval**

   ```bash
   python main.py
   ```

2. **Monitor a Specific Process with Default Interval**

   ```bash
   python main.py --pid 1234
   ```

3. **Monitor All Processes with 2-Second Interval**

   ```bash
   python main.py --interval 2
   ```

4. **Monitor a Specific Process with 5-Second Interval**

   ```bash
   python main.py --pid 1234 --interval 5
   ```

### Exit the Application

To stop monitoring and exit the application, press `Ctrl+C`.

## 🛠️ Troubleshooting

- **Process Not Found**: If you provide a PID that does not exist, the application will display "Process not found" for that PID.
- **Access Denied**: If the application does not have permission to access a process, it will display "Access denied" for that PID.

## 📝 Notes

- The application clears the terminal before displaying new data to provide a clean and updated view.
- The CPU usage data is displayed in a tabular format, with columns for PID and CPU Usage (%).

## 🙌 Contributing

We welcome contributions to the CPU Usage Monitor CLI Application. If you have any ideas or improvements, feel free to open an issue or submit a pull request on our GitHub repository.

---

This manual provides a comprehensive guide on how to install, use, and troubleshoot the CPU Usage Monitor CLI Application. We hope you find it helpful!