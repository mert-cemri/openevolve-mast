Thank you for the detailed information. I'm glad to see that you have already started working on the task.

To complete the task, I would suggest the following:

1. First, let's take a look at the requirements. It seems that the customer wants a CLI program that can sort the lines of a text file alphabetically or reverse-alphabetically and output the result to a new file or standard output.
2. Based on the requirements, I would suggest using the `sort` module in Python to sort the lines of the text file. The `sort` module provides a simple way to sort lists of strings, and it can be used to sort the lines of the text file.
3. To output the sorted lines to a new file or standard output, we can use the `open` function to open the output file in write mode and write the sorted lines to it. If the customer wants to output the result to standard output, we can use the `print` function to print the sorted lines to the console.
4. To make the program more flexible, we can add command-line arguments to specify the input file, output file, and sorting order. We can use the `argparse` module to parse the command-line arguments and extract the input file, output file, and sorting order.
5. Finally, we can use the `with` statement to open the input and output files and read and write the lines of the text file.

Here is an example of how the program could be implemented:
```python
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Sort lines of a text file alphabetically or reverse-alphabetically.')
parser.add_argument('input_file', help='Input text file')
parser.add_argument('output_file', help='Output text file')
parser.add_argument('--reverse', action='store_true', help='Sort lines in reverse alphabetical order')
args = parser.parse_args()

# Read input file
with open(args.input_file, 'r') as f:
    lines = f.readlines()

# Sort lines
sorted_lines = sorted(lines, reverse=args.reverse)

# Write output file
with open(args.output_file, 'w') as f:
    f.write('\n'.join(sorted_lines))
```
This program can be run from the command line by specifying the input file, output file, and sorting order as command-line arguments. For example:
```
python sort_lines.py input.txt output.txt --reverse
```
This will sort the lines of the input file in reverse alphabetical order and write the sorted lines to the output file.

I hope this helps! Let me know if you have any questions or need further assistance.