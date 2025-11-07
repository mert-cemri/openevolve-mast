# Firewall CLI Utility User Manual

## Overview

The Firewall CLI Utility is a Python-based command-line interface (CLI) tool designed to simplify the process of adding, removing, and listing basic firewall rules using `iptables` on Linux systems. This utility requires `sudo` privileges to execute `iptables` commands.

## Main Functions

### Add a Rule
- **Purpose:** Allows or blocks traffic on a specific port using a specified protocol.
- **Command:** `firewall add <action> <protocol> <port>`
- **Parameters:**
  - `<action>`: `allow` or `block`
  - `<protocol>`: `tcp`, `udp`, etc.
  - `<port>`: Port number (e.g., `80` for HTTP)

### Remove a Rule
- **Purpose:** Removes an existing rule based on the specified protocol and port.
- **Command:** `firewall remove <protocol> <port>`
- **Parameters:**
  - `<protocol>`: `tcp`, `udp`, etc.
  - `<port>`: Port number (e.g., `80` for HTTP)

### List Rules
- **Purpose:** Displays all current firewall rules.
- **Command:** `firewall list`

## Installation

### Prerequisites
- **Python 3.6+**: Ensure Python is installed on your system.
- **`iptables`**: Ensure `iptables` is installed and properly configured on your Linux system.
- **`sudo` Privileges**: The utility requires `sudo` privileges to execute `iptables` commands.

### Steps to Install

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ChatDev/firewall-cli-utility.git
   cd firewall-cli-utility
   ```

2. **Install Dependencies:**
   The `requirements.txt` file is currently empty, but if additional dependencies are added in the future, you can install them using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Make the Script Executable:**
   ```bash
   chmod +x main.py
   ```

4. **Create a Symlink (Optional):**
   For easier access, you can create a symlink to the script in a directory included in your `PATH`:
   ```bash
   sudo ln -s /path/to/firewall-cli-utility/main.py /usr/local/bin/firewall
   ```

## Usage

### Adding a Rule

To allow traffic on port 80 using TCP:
```bash
sudo firewall add allow tcp 80
```

To block traffic on port 22 using SSH:
```bash
sudo firewall add block tcp 22
```

### Removing a Rule

To remove the rule for port 80 using TCP:
```bash
sudo firewall remove tcp 80
```

### Listing Rules

To list all current firewall rules:
```bash
sudo firewall list
```

## Troubleshooting

- **Permission Denied:** Ensure you are running the commands with `sudo` privileges.
- **Command Not Found:** If you created a symlink, ensure the path is correct and the symlink points to the `main.py` script.
- **Invalid Protocol/Port:** Ensure the protocol and port are correctly specified.

## Contributing

We welcome contributions to improve the Firewall CLI Utility. Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This manual provides a comprehensive guide for users to understand and utilize the Firewall CLI Utility effectively. If you have any questions or encounter issues, feel free to reach out to our support team.