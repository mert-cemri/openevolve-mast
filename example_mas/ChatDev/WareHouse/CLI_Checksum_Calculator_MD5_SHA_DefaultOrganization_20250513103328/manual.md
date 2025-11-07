# Checksum Calculator CLI Utility

A command-line interface (CLI) utility to calculate and display the MD5 and SHA256 checksums of a given file. This utility is designed to be simple and efficient, allowing users to verify file integrity easily.

## Quick Install

To set up the environment and install the necessary dependencies, ensure you have Python 3.6 or higher installed on your system. You can check your Python version by running:

```bash
python --version
```

### Installation Steps

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies. Create and activate a virtual environment using:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install the required dependencies using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

## 🤔 What is this?

This utility provides a straightforward way to calculate the MD5 and SHA256 checksums of any file specified by the user. Checksums are commonly used to verify the integrity of files, ensuring that they have not been altered or corrupted.

## 📖 How to Use

### Running the Utility

Once you have installed the necessary dependencies, you can run the utility from the command line. Use the following command to calculate the checksums of a file:

```bash
python main.py <file_path>
```

Replace `<file_path>` with the path to the file you want to check. For example:

```bash
python main.py /path/to/your/file.txt
```

### Output

The utility will output the MD5 and SHA256 checksums of the specified file in the following format:

```
MD5: <md5_checksum>
SHA256: <sha256_checksum>
```

### Error Handling

If there is an error (e.g., the file does not exist or cannot be read), the utility will display an error message indicating the issue.

## Documentation

For more detailed documentation and examples, please refer to the source code comments and docstrings within the `main.py` and `checksum_calculator.py` files. These provide insights into the implementation details and can help with further customization or troubleshooting.

## Support

For any issues or questions, please contact our support team or refer to the project's issue tracker on the repository page.

---

This user manual provides all the necessary information to install, run, and understand the functionality of the Checksum Calculator CLI Utility. Enjoy verifying your files with ease!