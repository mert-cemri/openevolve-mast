```markdown
# CLI MP3 Tag Editor

A command-line interface (CLI) application for editing ID3 tags of MP3 files. This tool allows users to view and modify basic tags such as title, artist, album, and year using the `mutagen` library.

## Quick Install

To use the CLI MP3 Tag Editor, you need to have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## 🤔 What is this?

The CLI MP3 Tag Editor is a simple yet powerful tool for managing ID3 tags in MP3 files. ID3 tags are metadata containers used to store information about the audio file, such as the title, artist, album, and year of release. This application allows you to view and edit these tags directly from the command line.

## Main Functions

- **View Tags**: Display the current ID3 tags of an MP3 file.
- **Edit Tags**: Modify the title, artist, album, or year tags of an MP3 file.

## 📖 How to Use

### Viewing Tags

To view the tags of an MP3 file, use the following command:

```bash
python main.py <file_path> view
```

Replace `<file_path>` with the path to your MP3 file. This command will display the current tags: Title, Artist, Album, and Year.

### Editing Tags

To edit a specific tag, use the following command:

```bash
python main.py <file_path> edit <tag> <value>
```

- `<file_path>`: Path to your MP3 file.
- `<tag>`: The tag you want to edit (options: `title`, `artist`, `album`, `year`).
- `<value>`: The new value for the specified tag.

For example, to change the title of an MP3 file, you would use:

```bash
python main.py my_song.mp3 edit title "New Song Title"
```

### Saving Changes

After editing a tag, the changes are automatically saved to the file. If there is an error during the save process, an error message will be displayed.

## Troubleshooting

- Ensure that the file path is correct and that the file is accessible.
- Make sure the `mutagen` library is installed by running `pip install mutagen`.
- If you encounter any errors, check the console output for specific error messages.

## Additional Resources

For more information on ID3 tags and the `mutagen` library, you can refer to the following resources:

- [ID3 Tag Specification](https://id3.org/)
- [Mutagen Documentation](https://mutagen.readthedocs.io/)

This user manual provides a comprehensive guide to using the CLI MP3 Tag Editor. If you have any further questions or require support, please contact our support team.
```