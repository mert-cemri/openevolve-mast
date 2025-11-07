# Cyclic Encoder/Decoder

This software provides functions to encode and decode strings by cycling groups of three characters. It is a simple utility that can be used for encoding messages in a reversible manner.

## Main Functions

### 1. `encode_cyclic(s: str) -> str`

This function takes a string `s` as input and returns an encoded string by cycling groups of three characters. If the length of the string is not a multiple of three, the remaining characters are left unchanged.

**Example:**
```python
encoded = encode_cyclic("abcdefghi")
print(encoded)  # Output: "bcadefghi"
```

### 2. `decode_cyclic(s: str) -> str`

This function takes an encoded string `s` (encoded with the `encode_cyclic` function) as input and returns the original decoded string.

**Example:**
```python
decoded = decode_cyclic("bcadefghi")
print(decoded)  # Output: "abcdefghi"
```

## Installation

This software does not require any external dependencies. It is implemented purely in Python and can be run in any standard Python environment.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Clone the repository or download the `main.py` file to your local machine.

3. No additional installation steps are required as there are no external dependencies.

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the script using Python:
   ```bash
   python main.py
   ```

4. The script will execute and demonstrate the encoding and decoding functions with an example string. You can modify the `original` string in the `main.py` file to test with different inputs.

## Example

Here's a quick example of how you can use the functions in your own Python script:

```python
from main import encode_cyclic, decode_cyclic

original = "hello world"
encoded = encode_cyclic(original)
decoded = decode_cyclic(encoded)

print(f"Original: {original}")
print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")
```

This will output:
```
Original: hello world
Encoded: ehll oowlrd
Decoded: hello world
```

Feel free to integrate these functions into your own projects or modify them to suit your needs!