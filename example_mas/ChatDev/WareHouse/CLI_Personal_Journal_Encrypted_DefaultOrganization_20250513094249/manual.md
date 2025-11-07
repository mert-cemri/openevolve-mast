```markdown
# CLI Personal Journal Application

This application is a command-line interface (CLI) tool designed for personal journaling. It allows users to create, encrypt, and store journal entries locally. Each entry is timestamped and can be encrypted with a user-provided password to ensure privacy.

## Main Functions

1. **Add Entry**: Create a new journal entry. The entry is automatically timestamped and encrypted using a password provided by the user.
2. **View Entries**: Display all journal entries. Entries are decrypted using the user's password before being displayed.
3. **Save Entries**: Save all current journal entries to a local file (`journal.json`). This file includes encrypted entries and a salt used for encryption.
4. **Load Entries**: Load journal entries from the local file. Entries are decrypted using the user's password.
5. **Exit**: Exit the application.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Quick Install

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**

   Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the `cryptography` package, which is necessary for encrypting and decrypting journal entries.

## How to Use

1. **Run the Application**

   Navigate to the directory containing the `main.py` file and run the application:

   ```bash
   python main.py
   ```

2. **Enter Your Password**

   When prompted, enter a password that will be used to encrypt and decrypt your journal entries. Remember this password, as it is required to view and load your entries.

3. **Choose an Option**

   The application will present you with a menu of options:

   - **1. Add Entry**: Enter your journal entry text. The entry will be encrypted and stored in memory.
   - **2. View Entries**: View all entries currently in memory. Entries will be decrypted using your password.
   - **3. Save Entries**: Save all entries to the `journal.json` file.
   - **4. Load Entries**: Load entries from the `journal.json` file. Entries will be decrypted using your password.
   - **5. Exit**: Exit the application.

4. **Exit the Application**

   Select option 5 to exit the application. Ensure you save your entries before exiting to avoid losing any data.

## Security Note

- The application uses a password-based encryption mechanism to secure your journal entries. Ensure that your password is strong and kept confidential.
- The `journal.json` file contains encrypted entries and should be stored securely to prevent unauthorized access.

## Support

For any issues or questions, please contact our support team at [support@chatdev.com](mailto:support@chatdev.com).
```
