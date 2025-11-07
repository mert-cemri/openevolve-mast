#!/usr/bin/env python3
import argparse
import sys
from dictionary import Dictionary
def main():
    parser = argparse.ArgumentParser(description='CLI dictionary lookup tool')
    parser.add_argument('word', help='word to look up')
    args = parser.parse_args()
    dictionary = Dictionary()
    if args.word:
        if len(args.word) > 0 and args.word.isalnum():
            definition = dictionary.lookup(args.word)
            if definition:
                print(definition)
            else:
                print(f'No definition found for "{args.word}"')
        else:
            print('Please enter a valid word')
    else:
        print('Please enter a word')
if __name__ == '__main__':
    main()