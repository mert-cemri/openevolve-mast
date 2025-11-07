# Docker Container Manager CLI

## Overview

The Docker Container Manager CLI is a command-line interface tool designed to manage Docker containers. It allows users to list running or all containers, start or stop containers by their ID or name, and view logs of a container. This tool is built using Python and leverages the Docker CLI commands under the hood.

## Prerequisites

- Docker must be installed on your system and the user must have the necessary permissions to manage Docker containers.
- Python 3.x must be installed on your system.

## Installation

This project does not require any external dependencies beyond Python's standard library. Therefore, no additional installation steps are necessary other than ensuring Python is installed.

## Usage

### Command Structure

The Docker Container Manager CLI follows a simple command structure:

```
python main.py <command> [args]
```

### Commands

#### List Containers

To list all running containers, use:

```
python main.py list
```

To list all containers (including stopped ones), use:

```
python main.py list --all
```

#### Start Container

To start a container by its ID or name, use:

```
python main.py start <container_id_or_name>
```

#### Stop Container

To stop a container by its ID or name, use:

```
python main.py stop <container_id_or_name>
```

#### View Logs

To view the logs of a container by its ID or name, use:

```
python main.py logs <container_id_or_name>
```

### Examples

1. **List all running containers:**

   ```
   python main.py list
   ```

2. **List all containers (including stopped ones):**

   ```
   python main.py list --all
   ```

3. **Start a container with ID `abc123`:**

   ```
   python main.py start abc123
   ```

4. **Stop a container with name `my_container`:**

   ```
   python main.py stop my_container
   ```

5. **View logs for a container with ID `def456`:**

   ```
   python main.py logs def456
   ```

## GUI Usage

The project also includes a simple GUI interface built using `tkinter`. To use the GUI, follow these steps:

1. Ensure you have Python installed on your system.
2. Run the following command:

   ```
   python gui.py
   ```

3. A window will appear with buttons for each of the available commands. Click the desired button and follow the prompts to manage your Docker containers.

## Troubleshooting

- **Docker not installed or not running:** Ensure Docker is installed and running on your system.
- **Permission issues:** Ensure the user running the script has the necessary permissions to manage Docker containers.
- **Python not installed:** Ensure Python 3.x is installed on your system.

## Contributing

Contributions to this project are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

This manual should provide a comprehensive guide for users to understand and use the Docker Container Manager CLI effectively. If you have any specific questions or need further assistance, feel free to reach out!