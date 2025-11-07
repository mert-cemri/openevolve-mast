```markdown
# Git Branch Cleaner CLI Tool

A command-line interface (CLI) tool designed to help developers manage their local Git branches by listing branches that have been merged into the main/master branch and are inactive (based on an old commit date), with an option to delete them.

## Quick Install

### Prerequisites

- **Python 3.6 or higher**: Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).
- **Git**: This tool requires Git to be installed on your system. You can download it from the [official Git website](https://git-scm.com/downloads).

### Installation

1. **Clone the Repository**: First, clone the repository containing the Git Branch Cleaner CLI tool to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Python Dependencies**: Use `pip` to install the necessary Python dependencies.

   ```bash
   pip install -r requirements.txt
   ```

## 🤔 What is this?

The Git Branch Cleaner CLI tool is designed to streamline the process of cleaning up local Git branches. It identifies branches that have been merged into the main or master branch and are inactive based on a specified period (default is 30 days). The tool then provides an option to delete these branches, helping to keep your local repository organized and free of clutter.

## 📖 How to Use

### Listing Merged and Inactive Branches

To list branches that have been merged into the main/master branch and are inactive for more than 30 days, use the following command:

```bash
python main.py --list
```

This command will output a list of branches that meet the criteria.

### Deleting Branches

To delete specific branches, use the `--delete` option followed by the branch names you wish to remove:

```bash
python main.py --delete branch1 branch2
```

This command will delete the specified branches from your local repository.

## Documentation

For further information and detailed documentation, please refer to the source code comments and function docstrings within the `main.py` and `git_manager.py` files. These provide insights into the implementation details and the logic behind each function.

## Support

For any issues or questions, please contact our support team or refer to our [GitHub Issues page](<repository-issues-url>) for community assistance.

```
