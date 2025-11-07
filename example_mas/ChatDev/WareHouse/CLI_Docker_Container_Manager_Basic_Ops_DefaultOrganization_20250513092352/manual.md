# Docker CLI Manager User Manual

Welcome to the Docker CLI Manager, a command-line interface tool designed to help you manage Docker containers efficiently. This tool allows you to list, start, stop, and view logs of Docker containers using simple commands.

## Main Functions

The Docker CLI Manager provides the following main functionalities:

1. **List Containers**: View all or only running Docker containers.
2. **Start Container**: Start a Docker container by specifying its ID or name.
3. **Stop Container**: Stop a Docker container by specifying its ID or name.
4. **View Logs**: Display logs of a specific Docker container by ID or name.

## Installation

### Prerequisites

- Ensure Docker is installed on your system and you have the necessary permissions to manage Docker containers.
- Python 3.x should be installed on your system.

### Install Environment Dependencies

To install the required dependencies for the Docker CLI Manager, follow these steps:

1. Clone the repository or download the source code.
2. Navigate to the directory containing the source code.
3. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

This will install the Docker SDK for Python, which is necessary for interacting with Docker.

## Usage

### Running the CLI

To use the Docker CLI Manager, open a terminal and navigate to the directory containing the `main.py` file. Use the following command format to execute different operations:

```bash
python main.py <command> [options]
```

#### Commands

- **List Containers**: To list all running containers, use:

  ```bash
  python main.py list
  ```

  To list all containers (including stopped ones), use:

  ```bash
  python main.py list --all
  ```

- **Start Container**: To start a container, specify its ID or name:

  ```bash
  python main.py start <container_id_or_name>
  ```

- **Stop Container**: To stop a container, specify its ID or name:

  ```bash
  python main.py stop <container_id_or_name>
  ```

- **View Logs**: To view logs of a container, specify its ID or name:

  ```bash
  python main.py logs <container_id_or_name>
  ```

### Running the GUI

In addition to the CLI, a graphical user interface (GUI) is available using Tkinter. To launch the GUI, execute the following command:

```bash
python docker_gui.py
```

The GUI provides buttons to list running containers, start/stop containers, and view logs. Simply select a container from the list and click the appropriate button to perform an action.

## Documentation

For further details and advanced usage, please refer to the source code and comments within the files. The `docker_manager.py` file contains the core logic for interacting with Docker, while `docker_gui.py` provides the GUI implementation.

We hope this tool enhances your Docker container management experience. If you encounter any issues or have suggestions, please feel free to contribute or reach out to us.