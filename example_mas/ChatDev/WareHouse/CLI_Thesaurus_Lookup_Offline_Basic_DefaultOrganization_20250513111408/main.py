'''
This is the main script to run the CLI thesaurus lookup tool.
'''
from thesaurus import Thesaurus
from cli import CLI
def main():
    '''
    The entry point of the application.
    '''
    thesaurus_file = 'thesaurus.json'  # Path to the local thesaurus JSON file
    thesaurus = Thesaurus(thesaurus_file)
    cli = CLI(thesaurus)
    cli.run()
if __name__ == '__main__':
    main()