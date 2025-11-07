# CLI Environment Variable Manager

## Overview

The CLI Environment Variable Manager is a command-line tool designed to simplify the management of environment variables. It allows users to list, set, and unset environment variables both for the current session and persistently via the shell profile.

## Features

- **List Environment Variables:** View all environment variables currently set in the session.
- **Set Environment Variables:** Add new environment variables or update existing ones for the current session or persistently.
- **Unset Environment Variables:** Remove environment variables from the current session or the shell profile.

## Installation

### Prerequisites

- Python 3.6 or higher installed on your system.
- Supported shells: Bash, Zsh, or Fish.

### Steps to Install

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ChatDev/cli-env-manager.git
   cd cli-env-manager
   ```

2. **Install Dependencies:**

   This project uses only Python's standard library, so no additional dependencies are required. However, ensure that you have Python installed on your system.

   ```bash
   python --version
   ```

   If Python is not installed, download and install it from the [official Python website](https://www.python.org/downloads/).

## Usage

### Basic Commands

1. **List Environment Variables:**

   To list all environment variables, use the `list` command.

   ```bash
   python main.py list
   ```

2. **Set Environment Variables:**

   To set an environment variable for the current session, use the `set` command.

   ```bash
   python main.py set MY_VARIABLE my_value
   ```

   To set an environment variable persistently (i.e., it will be available in future sessions), add the `-p` or `--persistent` flag.

   ```bash
   python main.py set MY_VARIABLE my_value -p
   ```

3. **Unset Environment Variables:**

   To unset an environment variable from the current session, use the `unset` command.

   ```bash
   python main.py unset MY_VARIABLE
   ```

   If the variable was set persistently, it will also be removed from the shell profile.

### Advanced Usage

- **Persistent Variables:**

  When setting a variable persistently, the tool automatically detects the user's shell and updates the appropriate profile file (e.g., `.bashrc`, `.zshrc`, or `config.fish`).

- **Shell Support:**

  The tool supports Bash, Zsh, and Fish shells. If your shell is not supported, you will need to manually specify the profile path.

## Troubleshooting

### Unsupported Shell

If you encounter an error indicating that your shell is unsupported, you can manually specify the profile path by editing the `ShellProfileManager` class in `shell_profile_manager.py`.

### Environment Variables Not Persisting

Ensure that your shell profile file is being sourced correctly. For example, after editing `.bashrc`, you can source it using:

```bash
source ~/.bashrc
```

## Contributing

We welcome contributions to the CLI Environment Variable Manager. If you have any ideas, bug fixes, or improvements, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/ChatDev/cli-env-manager).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This manual provides a comprehensive guide on how to use the CLI Environment Variable Manager, including installation, basic and advanced usage, and troubleshooting tips. If you have any further questions or need additional assistance, please don't hesitate to reach out.