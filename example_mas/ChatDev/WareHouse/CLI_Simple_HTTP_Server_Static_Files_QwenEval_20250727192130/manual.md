# Simple CLI HTTP Server User Manual

## Overview

This document provides a detailed guide on how to install, configure, and use the Simple CLI HTTP Server. This server is designed to serve static files (HTML, CSS, JS, images) from a specified local directory and listens on a configurable port.

## Features

- **Command-Line Interface (CLI):** Start the server from the command line with various options.
- **Configurable Port:** Specify the port on which the server should listen.
- **Directory Specification:** Define the directory from which files will be served.
- **Graphical User Interface (GUI):** Optionally start a GUI for server management.

## Quick Install

### Prerequisites

- Python 3.6 or higher installed on your system.
- `pip` installed (usually comes with Python).

### Installation Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-repo/simple-cli-http-server.git
   cd simple-cli-http-server
   ```

2. **Install Dependencies:**

   This project does not require any external dependencies beyond Python's standard library. However, if you have a `requirements.txt` file, you can install dependencies using:

   ```bash
   pip install -r requirements.txt
   ```

   In this case, the `requirements.txt` file is empty as no external dependencies are needed.

## Usage

### Command-Line Interface (CLI)

1. **Start the Server:**

   ```bash
   python main.py --port 8000 --directory /path/to/your/directory
   ```

   - `--port`: Specifies the port number on which the server will listen. Default is `8000`.
   - `--directory`: Specifies the directory from which files will be served. Default is the current directory (`.`).
   - `--gui`: Starts the graphical user interface for server management.

2. **Access the Server:**

   Open a web browser and navigate to `http://localhost:8000` (or the specified port and directory).

### Graphical User Interface (GUI)

1. **Start the Server with GUI:**

   ```bash
   python main.py --gui
   ```

2. **Manage the Server:**

   - **Start Server:** Click the "Start Server" button to start the server.
   - **Stop Server:** Click the "Stop Server" button to stop the server.
   - **Status:** The status label will indicate whether the server is running or stopped.

## Examples

### Example 1: Serve Files from the Current Directory on Port 8000

```bash
python main.py
```

### Example 2: Serve Files from a Specific Directory on Port 9000

```bash
python main.py --port 9000 --directory /path/to/your/directory
```

### Example 3: Start the Server with GUI

```bash
python main.py --gui
```

## Troubleshooting

- **Port Already in Use:** If the specified port is already in use, you will receive an error. Choose a different port or stop the process using the port.
- **File Not Found:** Ensure that the specified directory exists and contains the files you want to serve.

## Conclusion

The Simple CLI HTTP Server is a versatile tool for serving static files locally. Whether you prefer using the command line or the graphical user interface, this server provides an easy-to-use solution for your needs.

If you encounter any issues or have suggestions for improvement, please feel free to reach out to the development team.

---

This manual should provide a comprehensive guide for users to understand and use the Simple CLI HTTP Server effectively.