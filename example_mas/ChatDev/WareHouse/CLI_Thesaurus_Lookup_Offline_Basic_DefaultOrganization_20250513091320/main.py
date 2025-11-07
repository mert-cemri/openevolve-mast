'''
Main application file for the CLI thesaurus lookup tool.
'''
from thesaurus import Thesaurus
def main():
    thesaurus = Thesaurus('thesaurus.txt')
    while True:
        word = input("Enter a word (or type 'exit' to quit): ").strip()
        if word.lower() == 'exit':
            break
        synonyms = thesaurus.get_synonyms(word)
        antonyms = thesaurus.get_antonyms(word)
        if synonyms:
            print(f"Synonyms for '{word}': {', '.join(synonyms)}")
        else:
            print(f"No synonyms found for '{word}'.")
        if antonyms:
            print(f"Antonyms for '{word}': {', '.join(antonyms)}")
        else:
            print(f"No antonyms found for '{word}'.")
if __name__ == "__main__":
    main()