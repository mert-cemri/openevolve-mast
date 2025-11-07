'''
This is the main file for the CLI dictionary lookup tool.
It reads from a local dictionary file and allows the user to input a word to get its definition.
'''
def load_dictionary(file_path):
    '''
    Loads the dictionary from a specified file path.
    Returns a dictionary with words as keys and definitions as values.
    '''
    dictionary = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                word, definition = line.strip().split(':', 1)
                dictionary[word.strip()] = definition.strip()
    except FileNotFoundError:
        print(f"Error: Dictionary file '{file_path}' not found.")
    return dictionary
def lookup_word(dictionary):
    '''
    Continuously retrieves the definition of the word entered by the user.
    Displays the definition or an error message if the word is not found.
    Allows the user to exit the lookup loop.
    '''
    while True:
        word = input("Enter a word (or type 'exit' to quit): ").strip()
        if word.lower() == 'exit':
            print("Exiting the dictionary lookup tool.")
            break
        definition = dictionary.get(word)
        if definition:
            print(f"Definition: {definition}")
        else:
            print("Word not found in dictionary.")
def main():
    '''
    Main function to start the CLI dictionary lookup tool.
    '''
    dictionary = load_dictionary("dictionary.txt")
    if dictionary:
        lookup_word(dictionary)
if __name__ == "__main__":
    main()