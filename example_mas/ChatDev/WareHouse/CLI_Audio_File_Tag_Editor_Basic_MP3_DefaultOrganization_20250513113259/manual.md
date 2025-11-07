```markdown
# CLI MP3 Tag Editor

A command-line interface (CLI) application for editing ID3 tags of MP3 files. This tool allows users to view and modify basic ID3 tags such as title, artist, album, and year.

## Quick Install

To install the necessary environment dependencies, ensure you have Python installed, then use pip to install the required library:

```bash
pip install -r requirements.txt
```

This will install the `mutagen` library, which is used for MP3 tag manipulation.

## 🤔 What is this?

The CLI MP3 Tag Editor is a simple yet powerful tool designed to help users manage the metadata of their MP3 files. With this application, you can easily view and edit the title, artist, album, and year tags of your MP3 files directly from the command line.

## 📖 Main Functions

### Viewing MP3 Tags

You can view the current ID3 tags of an MP3 file using the `--view` option. This will display all the tags present in the file.

**Example:**

```bash
python main.py yourfile.mp3 --view
```

### Editing MP3 Tags

To edit a specific tag, use the `--edit` option followed by the tag name and the new value. Supported tags include `title`, `artist`, `album`, and `year`.

**Example:**

```bash
python main.py yourfile.mp3 --edit title "New Song Title"
```

```bash
python main.py yourfile.mp3 --edit artist "New Artist Name"
```

```bash
python main.py yourfile.mp3 --edit album "New Album Name"
```

```bash
python main.py yourfile.mp3 --edit year 2023
```

## 🛠️ How to Use

1. **Clone the Repository:**

   Clone the repository to your local machine using Git.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies:**

   Install the required Python packages using pip.

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**

   Use the `main.py` script to interact with your MP3 files.

   - To view tags:

     ```bash
     python main.py yourfile.mp3 --view
     ```

   - To edit a tag:

     ```bash
     python main.py yourfile.mp3 --edit <tag> <value>
     ```

   Replace `<tag>` with `title`, `artist`, `album`, or `year`, and `<value>` with the desired new value.

## ⚠️ Notes

- Ensure the MP3 file path is correct when using the application.
- The `year` tag must be a valid four-digit year.
- The application currently supports basic ID3 tags only.

## 📚 Documentation

For more detailed information on the `mutagen` library used for tag manipulation, please refer to the [Mutagen Documentation](https://mutagen.readthedocs.io/).

```