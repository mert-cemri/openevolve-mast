'''
Main entry point for the directory synchronizer application.
'''
from gui import DirectorySynchronizerGUI
def main():
    '''
    Main function to run the directory synchronizer application.
    '''
    try:
        app = DirectorySynchronizerGUI()
        app.run()
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()