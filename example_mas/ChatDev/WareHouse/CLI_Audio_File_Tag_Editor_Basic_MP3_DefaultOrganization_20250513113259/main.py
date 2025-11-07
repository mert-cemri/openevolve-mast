'''
Main module for the CLI MP3 tag editor application.
'''
import argparse
from mp3_tag_editor import MP3TagEditor
def main():
    parser = argparse.ArgumentParser(description='CLI MP3 Tag Editor')
    parser.add_argument('file', help='Path to the MP3 file')
    parser.add_argument('--view', action='store_true', help='View MP3 tags')
    parser.add_argument('--edit', nargs=2, metavar=('TAG', 'VALUE'), help='Edit a specific MP3 tag')
    args = parser.parse_args()
    editor = MP3TagEditor(args.file)
    if args.view:
        editor.view_tags()
    elif args.edit:
        tag, value = args.edit
        editor.edit_tag(tag, value)
    else:
        print("Please specify an action: --view or --edit TAG VALUE")
if __name__ == '__main__':
    main()