'''
Main file to handle command-line interface for MP3 tag editor.
This script allows users to view and modify basic ID3 tags of MP3 files.
Usage:
    python main.py yourfile.mp3 --title "New Title" --artist "New Artist" --album "New Album" --year "2023"
    python main.py yourfile.mp3 --view
'''
import argparse
import os
import sys
try:
    from tag_editor import TagEditor
except ModuleNotFoundError:
    print("Error: The 'mutagen' library is not installed.")
    print("Please install it using the following command:")
    print("pip install mutagen")
    sys.exit(1)
def main():
    parser = argparse.ArgumentParser(description='MP3 Tag Editor')
    parser.add_argument('file', help='MP3 file to edit')
    parser.add_argument('--title', help='Set the title of the MP3 file')
    parser.add_argument('--artist', help='Set the artist of the MP3 file')
    parser.add_argument('--album', help='Set the album of the MP3 file')
    parser.add_argument('--year', help='Set the year of the MP3 file')
    parser.add_argument('--view', action='store_true', help='View current tags')
    args = parser.parse_args()
    if not os.path.isfile(args.file):
        print(f"Error: File '{args.file}' does not exist.")
        return
    if not args.file.lower().endswith('.mp3'):
        print(f"Error: File '{args.file}' is not an MP3 file.")
        return
    editor = TagEditor(args.file)
    if args.view:
        tags = editor.get_tags()
        print(f"Title: {tags.get('title', 'N/A')}")
        print(f"Artist: {tags.get('artist', 'N/A')}")
        print(f"Album: {tags.get('album', 'N/A')}")
        print(f"Year: {tags.get('year', 'N/A')}")
    else:
        if any(not isinstance(value, str) for value in [args.title, args.artist, args.album, args.year] if value is not None):
            print("Error: All tag values must be strings.")
            return
        editor.set_tags(title=args.title, artist=args.artist, album=args.album, year=args.year)
        editor.save_file()
        print("Tags updated successfully.")
if __name__ == '__main__':
    main()