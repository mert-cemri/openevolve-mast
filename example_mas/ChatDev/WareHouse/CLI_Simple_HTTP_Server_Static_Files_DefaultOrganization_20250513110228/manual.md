# Static File Server

A simple CLI HTTP server application that serves static files (HTML, CSS, JS, images) from a specified local directory and listens on a configurable port.

## Overview

This application allows users to easily serve static files over HTTP from a specified directory on their local machine. It provides both a command-line interface (CLI) and a graphical user interface (GUI) for configuring and starting the server.

## Features

- **Serve Static Files**: Serve HTML, CSS, JavaScript, and image files from a specified directory.
- **Configurable Port**: Choose the port number on which the server listens.
- **Command-Line Interface**: Start the server using command-line arguments.
- **Graphical User Interface**: Use a simple GUI to configure and start the server.

## Installation

### Prerequisites

- Python 3.6 or above

### Install Environment Dependencies

To install the necessary dependencies, ensure you have Python installed and run the following command:

```bash
pip install -r requirements.txt
```

This will ensure that your environment is set up correctly to run the application.

## Usage

### Command-Line Interface

To start the server using the command-line interface, run the following command:

```bash
python main.py <directory> <port>
```

- `<directory>`: The path to the directory containing the static files you want to serve.
- `<port>`: The port number on which the server should listen.

Example:

```bash
python main.py /path/to/static/files 8080
```

This command will start the server, serving files from `/path/to/static/files` on port `8080`.

### Graphical User Interface

To start the server using the graphical user interface, run the following command:

```bash
python gui.py
```

1. **Select Directory**: Click the "Browse" button to select the directory containing the static files.
2. **Enter Port**: Enter the port number in the "Port" field.
3. **Start Server**: Click the "Start Server" button to start serving files.

A message box will confirm that the server has started successfully, and you can access the server at `http://localhost:<port>`.

## Documentation

For more detailed information on using the application, please refer to the source code comments and docstrings in `main.py`, `server.py`, and `gui.py`.

## Support

If you encounter any issues or have questions, please contact our support team for assistance. We are here to help you make the most of this application.