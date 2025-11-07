# SSH Alias Manager

## Overview

The SSH Alias Manager is a command-line interface (CLI) tool designed to simplify the management of SSH connection aliases. It allows users to add, list, and remove SSH aliases, which include details such as hostname, user, port, and key file. These aliases are stored in a configuration file, making it easier to connect to remote servers.

## Quick Install

To install the SSH Alias Manager, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository and install the required dependencies using pip:

```bash
git clone https://github.com/ChatDev/ssh-alias-manager.git
cd ssh-alias-manager
pip install -r requirements.txt
```

Alternatively, you can install the package directly from PyPI:

```bash
pip install ssh-alias-manager
```

## 🤔 What is this?

The SSH Alias Manager is a tool that helps you manage SSH connections more efficiently. Instead of remembering or typing out the full SSH command each time, you can create an alias that stores all the necessary information. This makes it easier to connect to remote servers, especially when you have multiple connections to manage.

## 📖 Documentation

### Main Functions

The SSH Alias Manager provides the following main functions:

- **Add Alias:** Create a new SSH alias by providing the hostname, user, port, and key file.
- **List Aliases:** Display all the SSH aliases stored in the configuration file.
- **Remove Alias:** Delete an existing SSH alias by specifying the hostname.

### How to Use

#### Command-Line Interface (CLI)

The SSH Alias Manager can be run from the command line. To start the CLI, navigate to the directory where the `main.py` file is located and run the following command:

```bash
python main.py
```

Once the CLI is running, you can use the following commands:

- **add:** Create a new SSH alias.
- **list:** Display all SSH aliases.
- **remove:** Delete an existing SSH alias.
- **exit:** Exit the CLI.

#### Adding an Alias

To add a new SSH alias, use the `add` command. You will be prompted to enter the hostname, user, port, and key file.

```bash
Enter command (add, list, remove, exit): add
Enter hostname: example.com
Enter user: username
Enter port: 22
Enter key file: /path/to/keyfile
Alias example.com added successfully.
```

#### Listing Aliases

To list all SSH aliases, use the `list` command.

```bash
Enter command (add, list, remove, exit): list
Hostname: example.com, User: username, Port: 22, Key File: /path/to/keyfile
```

#### Removing an Alias

To remove an existing SSH alias, use the `remove` command. You will be prompted to enter the hostname of the alias you want to remove and confirm the operation.

```bash
Enter command (add, list, remove, exit): remove
Enter hostname to remove: example.com
Are you sure you want to remove the alias example.com? (y/n): y
Alias example.com removed successfully.
```

#### Graphical User Interface (GUI)

The SSH Alias Manager also provides a graphical user interface (GUI) for those who prefer a visual interface. To start the GUI, run the following command:

```bash
python main.py --gui
```

The GUI provides buttons to add, list, and remove SSH aliases, as well as an exit button to close the application.

### Configuration File

The SSH Alias Manager stores all SSH aliases in a configuration file named `ssh_aliases.json`. This file is located in the same directory as the `main.py` file. You can manually edit this file if needed, but it is recommended to use the CLI or GUI to manage aliases.

### Error Handling

The SSH Alias Manager includes error handling to ensure that you provide valid input when adding or removing aliases. If you enter invalid data, the application will display an error message and prompt you to try again.

## 🛠️ Dependencies

The SSH Alias Manager requires the following dependencies:

- `tkinter` (for the GUI interface)
- `json` (for reading and writing the configuration file)

These dependencies are included in the standard Python library, so you do not need to install them separately.

## 🤝 Contributing

We welcome contributions to the SSH Alias Manager! If you have any ideas for improvements or bug fixes, please feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/ChatDev/ssh-alias-manager).

## 📝 License

The SSH Alias Manager is licensed under the MIT License. See the [LICENSE](https://github.com/ChatDev/ssh-alias-manager/blob/main/LICENSE) file for more information.

---

This manual should provide a comprehensive guide for users to install, understand, and use the SSH Alias Manager effectively. Let me know if you need any further adjustments or additional information.