'''
This is the main entry point for the CLI MP3 tag editor application. It handles command-line arguments and invokes the MP3TagEditor class methods.
'''
import sys
from mp3_tag_editor import MP3TagEditor
def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <file_path> <command> [<tag> <value>]")
        print("Commands:")
        print("  view - View all tags")
        print("  edit <tag> <value> - Edit a specific tag")
        sys.exit(1)
    file_path = sys.argv[1]
    command = sys.argv[2]
    editor = MP3TagEditor(file_path)
    if command == "view":
        editor.view_tags()
    elif command == "edit":
        if len(sys.argv) != 5:
            print("Usage: python main.py <file_path> edit <tag> <value>")
            sys.exit(1)
        tag = sys.argv[3]
        value = sys.argv[4]
        editor.edit_tag(tag, value)
        editor.save_changes()
    else:
        print("Unknown command:", command)
        sys.exit(1)
if __name__ == "__main__":
    main()