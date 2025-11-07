'''
Main executable file for palindrome detection application.
'''
import sys
from palindrome_detector import PalindromeDetector
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    detector = PalindromeDetector(file_path)
    palindromes = detector.find_palindromes()
    if palindromes:
        print("Palindromes found in the file:")
        for palindrome in palindromes:
            print(f"- {palindrome}")
    else:
        print("No palindromes found in the file.")
if __name__ == "__main__":
    main()