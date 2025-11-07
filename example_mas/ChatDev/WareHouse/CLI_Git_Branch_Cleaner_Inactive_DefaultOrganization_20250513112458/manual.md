```markdown
# Git Branch Cleaner CLI Tool

A command-line interface (CLI) tool designed to help developers efficiently manage their local Git branches by listing branches that have been merged into the main/master branch and are inactive (old commit date), with an option to delete them.

## Quick Install

To get started with the Git Branch Cleaner CLI Tool, follow these steps:

1. **Clone the Repository:**

   First, clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up the Environment:**

   Ensure you have Python 3.6 or higher installed. You can check your Python version with:

   ```bash
   python --version
   ```

   If you need to install Python, download it from [python.org](https://www.python.org/downloads/).

3. **Install Dependencies:**

   Install the necessary dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

## 🤔 What is this?

The Git Branch Cleaner CLI Tool is designed to streamline the process of managing local Git branches. It helps developers identify branches that are no longer active and have already been merged into the main or master branch, offering an option to delete them to keep the repository clean and organized.

### Main Functions

- **List Merged and Inactive Branches:**

  The tool lists all branches that have been merged into the main/master branch and have not been updated in the last 30 days.

- **Delete Branches:**

  Provides an option to delete specified branches after confirmation, helping to maintain a tidy repository.

## 📖 How to Use

### Listing Merged and Inactive Branches

To list all branches that have been merged into the main/master branch and are inactive, use the following command:

```bash
python main.py --list
```

This command will output a list of branches that meet the criteria.

### Deleting a Branch

To delete a specific branch, use the following command:

```bash
python main.py --delete <branch-name>
```

You will be prompted to confirm the deletion. Type `yes` to proceed with the deletion or `no` to cancel.

### Example Usage

1. **List Inactive Branches:**

   ```bash
   python main.py --list
   ```

   Output:

   ```
   feature/old-feature
   bugfix/old-bugfix
   ```

2. **Delete a Branch:**

   ```bash
   python main.py --delete feature/old-feature
   ```

   Output:

   ```
   Are you sure you want to forcefully delete the branch 'feature/old-feature'? This action cannot be undone. (yes/no): yes
   Branch 'feature/old-feature' has been deleted.
   ```

## Support

For any issues or questions, please contact our support team or visit our [GitHub repository](<repository-url>) for more information and updates.
```
