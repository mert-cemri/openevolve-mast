'''
Main executable file for palindrome detection supporting word and phrase-level detection.
'''
from palindrome_detector import PalindromeDetector
def main():
    file_path = input("Enter the path to the text file: ")
    detector = PalindromeDetector(file_path)
    try:
        word_palindromes, phrase_palindromes = detector.find_palindromes()
        if word_palindromes:
            print("\nWord-level palindromes found in the file:")
            for palindrome in word_palindromes:
                print(f"- {palindrome}")
        else:
            print("\nNo word-level palindromes found in the file.")
        if phrase_palindromes:
            print("\nPhrase-level palindromes found in the file:")
            for palindrome in phrase_palindromes:
                print(f"- {palindrome}")
        else:
            print("\nNo phrase-level palindromes found in the file.")
    except FileNotFoundError:
        print(f"\nError: File '{file_path}' not found.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
if __name__ == "__main__":
    main()