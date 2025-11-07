```markdown
# SSH Alias Manager

A command-line interface (CLI) tool to manage SSH connection aliases, making it easier to connect to remote servers by storing connection details in a configuration file.

## Main Functions

The SSH Alias Manager provides the following main functions:

- **Add SSH Alias**: Add a new SSH alias with specified connection details.
- **Remove SSH Alias**: Remove an existing SSH alias.
- **List SSH Aliases**: List all stored SSH aliases and their details.

## Installation

### Prerequisites

- Python 3.6 or higher is required to run the SSH Alias Manager.

### Quick Install

1. **Clone the Repository**: Clone the project repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Install the required Python dependencies.

   ```bash
   pip install -r requirements.txt
   ```

## Usage

The SSH Alias Manager can be used through the command line to manage your SSH connection aliases.

### Add an SSH Alias

To add a new SSH alias, use the following command:

```bash
python main.py add <alias_name> <hostname> <user> <port> <key_file>
```

- `alias_name`: A unique name for the SSH alias.
- `hostname`: The hostname of the SSH server.
- `user`: The username for the SSH connection.
- `port`: The port number for the SSH connection.
- `key_file`: The path to the SSH key file.

### Remove an SSH Alias

To remove an existing SSH alias, use the following command:

```bash
python main.py remove <alias_name>
```

- `alias_name`: The name of the SSH alias to remove.

### List SSH Aliases

To list all stored SSH aliases, use the following command:

```bash
python main.py list
```

This command will display all the aliases along with their connection details.

## Example

Here is an example of how to use the SSH Alias Manager:

1. **Add an Alias**:

   ```bash
   python main.py add myserver example.com user 22 ~/.ssh/id_rsa
   ```

2. **List Aliases**:

   ```bash
   python main.py list
   ```

   Output:

   ```
   myserver: {'hostname': 'example.com', 'user': 'user', 'port': '22', 'key_file': '~/.ssh/id_rsa'}
   ```

3. **Remove an Alias**:

   ```bash
   python main.py remove myserver
   ```

   Output:

   ```
   Alias removed successfully!
   ```

## Documentation

For more detailed information and advanced usage, please refer to the source code and comments within the `ssh_alias_manager.py` and `main.py` files.

```