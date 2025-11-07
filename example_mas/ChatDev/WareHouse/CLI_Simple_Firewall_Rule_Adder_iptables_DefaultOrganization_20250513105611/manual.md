```markdown
# Firewall Manager CLI Utility

A simple command-line interface (CLI) utility to manage basic firewall rules using `iptables` on Linux systems. This utility allows users to easily add or remove rules to allow or block traffic on specific ports.

## Quick Install

### Prerequisites

- **Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **iptables**: This utility requires `iptables` to be installed on your Linux system. It is typically pre-installed on most Linux distributions.

### Installation

1. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: This project does not require any external Python packages, so no additional installation is needed for dependencies.

## 🤔 What is this?

The Firewall Manager CLI Utility is designed to simplify the process of managing firewall rules on Linux systems. By using this utility, users can quickly allow or block traffic on specific ports without needing to manually enter complex `iptables` commands.

## 📖 Documentation

### Main Functions

- **Allow Traffic on a Port**: Add a rule to allow incoming traffic on a specified port.
- **Block Traffic on a Port**: Remove a rule to block incoming traffic on a specified port.

### How to Use

1. **Open Terminal**: Open your terminal or command line interface.

2. **Navigate to the Project Directory**: Ensure you are in the directory where the `main.py` file is located.

3. **Run the Utility**: Use the following command structure to run the utility:
   ```bash
   python main.py <action> <port>
   ```
   - `<action>`: Specify `allow` to permit traffic or `block` to restrict traffic.
   - `<port>`: Specify the port number you wish to allow or block.

   **Examples**:
   - To allow traffic on port 80:
     ```bash
     python main.py allow 80
     ```
   - To block traffic on port 80:
     ```bash
     python main.py block 80
     ```

### Important Notes

- **Sudo Privileges**: This utility requires `sudo` privileges to modify `iptables` rules. Ensure you have the necessary permissions to execute commands with `sudo`.
- **Error Handling**: The utility provides feedback on the success or failure of each command. Ensure you enter valid port numbers to avoid errors.

For any further assistance or inquiries, please contact our support team.

```
