# Simple CLI HTTP Server

A simple command-line interface (CLI) HTTP server for serving static files (HTML, CSS, JS, images) from a specified local directory. This server listens on a configurable port, making it easy to serve files locally for development or testing purposes.

## Main Functions

- **Serve Static Files**: The server can serve static files such as HTML, CSS, JavaScript, and images from a specified directory.
- **Configurable Port**: Users can specify the port on which the server listens, allowing flexibility in network configurations.
- **Simple Command-Line Interface**: The server is operated via a simple command-line interface, making it easy to use for developers.

## Installation

### Prerequisites

- **Python 3.x**: Ensure you have Python 3.x installed on your system. The server uses Python's built-in `http.server` module, which is available in Python 3.x.

### Environment Setup

1. **Clone the Repository**: Clone the repository containing the server code to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Python**: If Python is not already installed, download and install Python 3.x from the [official Python website](https://www.python.org/downloads/).

3. **Verify Python Installation**: Verify that Python is installed correctly by running:

   ```bash
   python --version
   ```

   Ensure the version is 3.6 or higher.

## Usage

1. **Navigate to the Project Directory**: Open a terminal and navigate to the directory where the server code is located.

2. **Run the Server**: Use the following command to start the server, specifying the directory to serve files from and the port to listen on.

   ```bash
   python main.py <directory> <port>
   ```

   - `<directory>`: The path to the directory containing the static files you want to serve.
   - `<port>`: The port number on which the server will listen for incoming requests.

   Example:

   ```bash
   python main.py ./static 8080
   ```

   This command will serve files from the `./static` directory on port `8080`.

3. **Access the Server**: Open a web browser and navigate to `http://localhost:<port>` to access the files served by the server.

   Example:

   ```bash
   http://localhost:8080
   ```

4. **Stop the Server**: To stop the server, press `Ctrl + C` in the terminal where the server is running.

## Notes

- The server does not require any external packages, as it utilizes Python's built-in modules.
- Ensure that the specified directory contains the files you wish to serve.
- The server is intended for local development and testing purposes. For production use, consider using a more robust server solution.

This simple CLI HTTP server provides a straightforward way to serve static files locally, making it an ideal tool for developers working on web projects.