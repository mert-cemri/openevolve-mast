# Docker CLI Manager

A simple command-line interface (CLI) and graphical user interface (GUI) application for managing Docker containers. This tool allows users to list, start, stop, and view logs of Docker containers.

## Main Functions

### CLI Features
- **List Containers**: View all running containers or all containers (including stopped ones).
- **Start Container**: Start a container using its ID.
- **Stop Container**: Stop a running container using its ID.
- **View Logs**: Display logs for a specific container using its ID.

### GUI Features
- **Interactive Container Management**: Use a graphical interface to start, stop, and view logs of containers.
- **Real-time Updates**: Automatically refresh the list of containers to reflect their current state.

## Installation

### Prerequisites
- Ensure Docker is installed and running on your system.
- Ensure you have the necessary permissions to manage Docker containers.

### Environment Setup
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**
   Use the following command to install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the CLI

1. **Navigate to the Project Directory**
   ```bash
   cd <repository-directory>
   ```

2. **Execute the CLI Application**
   ```bash
   python main.py <command> [<args>]
   ```

   **Commands:**
   - `list [--all]`: List running containers or all containers if `--all` is specified.
   - `start <id>`: Start a container by its ID.
   - `stop <id>`: Stop a container by its ID.
   - `logs <id>`: View logs of a container by its ID.

   **Example Usage:**
   ```bash
   python main.py list --all
   python main.py start <container-id>
   python main.py stop <container-id>
   python main.py logs <container-id>
   ```

### Running the GUI

1. **Navigate to the Project Directory**
   ```bash
   cd <repository-directory>
   ```

2. **Execute the GUI Application**
   ```bash
   python docker_gui.py
   ```

3. **Using the GUI**
   - **List Containers**: The main window displays all containers. Use the refresh button to update the list.
   - **Start/Stop Containers**: Select a container from the list and click the "Start Container" or "Stop Container" button.
   - **View Logs**: Select a container and click the "View Logs" button to open a new window displaying the container's logs.

## Documentation

For further details on the implementation and usage, please refer to the source code and comments within the files. This application is designed to be straightforward and user-friendly, providing a simple interface for managing Docker containers.