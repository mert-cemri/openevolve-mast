```markdown
# CLI Environment Variable Manager

A simple and efficient command-line interface (CLI) tool for managing environment variables. This tool allows users to list, set, and unset environment variables both for the current session and persistently via shell profiles.

## Quick Install

This project does not require any external dependencies. You only need Python installed on your system.

## 🤔 What is this?

The CLI Environment Variable Manager is designed to simplify the management of environment variables directly from the command line. It provides a straightforward way to:

- **List** all current environment variables.
- **Set** an environment variable for the current session or persistently by adding it to the shell profile.
- **Unset** an environment variable from the current session or remove it from the shell profile.

## 📖 Documentation

### Installation

1. **Ensure Python is installed**: This tool requires Python to be installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

2. **Clone the repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory**:
   ```bash
   cd <project-directory>
   ```

### Usage

The CLI Environment Variable Manager is executed via the command line. Below are the main functions and how to use them:

#### List Environment Variables

To list all current environment variables, use the following command:
```bash
python main.py list
```

#### Set an Environment Variable

To set an environment variable, use the following command:
```bash
python main.py set --name <VARIABLE_NAME> --value <VARIABLE_VALUE>
```
- To make the change persistent, add the `--persistent` flag:
  ```bash
  python main.py set --name <VARIABLE_NAME> --value <VARIABLE_VALUE> --persistent
  ```

#### Unset an Environment Variable

To unset an environment variable, use the following command:
```bash
python main.py unset --name <VARIABLE_NAME>
```
- To remove the variable from the shell profile as well, add the `--persistent` flag:
  ```bash
  python main.py unset --name <VARIABLE_NAME> --persistent
  ```

### Examples

- **List all environment variables**:
  ```bash
  python main.py list
  ```

- **Set a new environment variable for the current session**:
  ```bash
  python main.py set --name MY_VAR --value "my_value"
  ```

- **Set a new environment variable persistently**:
  ```bash
  python main.py set --name MY_VAR --value "my_value" --persistent
  ```

- **Unset an environment variable from the current session**:
  ```bash
  python main.py unset --name MY_VAR
  ```

- **Unset an environment variable and remove it from the shell profile**:
  ```bash
  python main.py unset --name MY_VAR --persistent
  ```

## Support

For any issues or questions, please contact our support team or visit our [GitHub repository](<repository-url>) for more information and updates.
```
