# Checksum Calculator CLI Utility

This user manual provides detailed instructions on how to use the Checksum Calculator CLI utility, which calculates and displays the MD5 and SHA256 checksums of a given file. The utility is implemented in Python and can be used via the command line interface.

## Main Functions

The Checksum Calculator CLI utility offers the following main functions:

- **Calculate MD5 Checksum**: Computes the MD5 checksum of a specified file.
- **Calculate SHA256 Checksum**: Computes the SHA256 checksum of a specified file.

## Installation

To use the Checksum Calculator CLI utility, you need to have Python installed on your system. Follow these steps to set up the environment and install necessary dependencies:

1. **Install Python**: Ensure that Python 3.x is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Install Required Packages**: The utility requires the `argparse` and `hashlib` modules, which are included in the Python standard library. No additional packages are needed.

3. **Download the Source Code**: Clone or download the source code from the repository where the utility is hosted.

## Usage

Once you have set up the environment, you can use the Checksum Calculator CLI utility as follows:

1. **Open a Terminal**: Navigate to the directory where the source code is located.

2. **Run the Utility**: Execute the following command to calculate the checksums of a file:

   ```bash
   python main.py <file_path>
   ```

   Replace `<file_path>` with the path to the file for which you want to calculate the checksums.

3. **View the Results**: The utility will output the MD5 and SHA256 checksums of the specified file in the terminal.

   Example output:
   ```
   MD5: d41d8cd98f00b204e9800998ecf8427e
   SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
   ```

## Error Handling

If an error occurs during the execution, the utility will display an error message in the terminal. Common errors include:

- **File Not Found**: Ensure that the file path is correct and the file exists.
- **Permission Denied**: Check the file permissions and ensure you have the necessary access rights.

## Additional Information

For any further assistance or to report issues, please contact the support team or refer to the documentation provided with the source code.

This concludes the user manual for the Checksum Calculator CLI utility. Enjoy using the tool to verify file integrity efficiently!