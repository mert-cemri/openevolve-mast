'''
Main module to execute the palindrome detection program.
'''
from file_handler import FileHandler
from palindrome_detector import PalindromeDetector
def main():
    # Define the path to the text file
    file_path = 'input.txt'
    # Read the content of the file
    content = FileHandler.read_file(file_path)
    # Detect palindromes in the content
    palindromes = PalindromeDetector.find_palindromes(content)
    # Print the detected palindromes
    print("Detected Palindromes:")
    for palindrome in palindromes:
        print(palindrome)
if __name__ == "__main__":
    main()