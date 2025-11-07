'''
Main file to run the music playlist manager.
'''
from cli import CLI
def main():
    print("Welcome to the Music Playlist Manager!")
    cli = CLI()
    cli.run()
if __name__ == "__main__":
    main()