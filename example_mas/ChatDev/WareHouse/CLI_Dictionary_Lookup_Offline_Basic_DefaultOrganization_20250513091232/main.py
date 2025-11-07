'''
Main entry point for the CLI dictionary lookup tool.
'''
def load_dictionary(filepath):
    '''
    Load the dictionary from a file.
    :param filepath: Path to the dictionary file.
    :return: Dictionary with words as keys and definitions as values.
    '''
    dictionary = {}
    try:
        with open(filepath, 'r') as file:
            for line in file:
                if ':' in line:
                    word, definition = line.strip().split(':', 1)
                    dictionary[word.strip()] = definition.strip()
                else:
                    print(f"Warning: Skipping improperly formatted line: {line.strip()}")
    except FileNotFoundError:
        print("Error: Dictionary file not found.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
    return dictionary
def lookup_word(dictionary):
    '''
    Retrieve and display the definition of the input word.
    :param dictionary: The dictionary to lookup words from.
    '''
    while True:
        word = input("Enter word (or type 'exit' to quit): ").strip()
        if word.lower() == 'exit':
            break
        definition = dictionary.get(word, "Word not found in dictionary.")
        print(f"Definition: {definition}")
def main():
    dictionary = load_dictionary("dictionary.txt")
    lookup_word(dictionary)
if __name__ == "__main__":
    main()