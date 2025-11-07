# String to MD5 Converter

This software provides a simple function to convert a given string into its MD5 hash equivalent. It is designed to be lightweight and efficient, focusing solely on the task of generating MD5 hashes.

## Main Functionality

The primary function provided by this software is `string_to_md5`. This function takes a string as input and returns its MD5 hash equivalent. If the input string is empty, the function returns `None`.

### Function Details

- **Function Name**: `string_to_md5`
- **Input**: A string `text`
- **Output**: A string representing the MD5 hash of the input text, or `None` if the input is an empty string.

#### Example Usage

```python
>>> string_to_md5('Hello world')
'3e25960a79dbc69b674cd4ec67a72c62'
```

## Installation

To use this software, you need to have Python installed on your system. The software is compatible with Python version 3.6 and above.

### Step-by-Step Installation

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change into the project directory.

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**: Install the necessary dependencies using pip.

   ```bash
   pip install -r requirements.txt
   ```

   Ensure that your Python version is 3.6 or above as specified in the `requirements.txt`.

## How to Use

1. **Import the Function**: In your Python script, import the `string_to_md5` function.

   ```python
   from main import string_to_md5
   ```

2. **Call the Function**: Use the function by passing a string to it.

   ```python
   result = string_to_md5('Hello world')
   print(result)  # Output: 3e25960a79dbc69b674cd4ec67a72c62
   ```

3. **Handle Empty Strings**: If you pass an empty string, the function will return `None`.

   ```python
   result = string_to_md5('')
   print(result)  # Output: None
   ```

## Additional Information

This software is designed to be simple and efficient, with no additional features or GUI components. It is ideal for developers who need a straightforward solution for generating MD5 hashes in their applications.

For any issues or contributions, please refer to the project's repository on GitHub.