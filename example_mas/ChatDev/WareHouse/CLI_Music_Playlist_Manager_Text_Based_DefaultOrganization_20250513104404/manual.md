```markdown
# Music Playlist Manager

A Command-Line Interface (CLI) application to manage your music playlists with ease.

## Introduction

The Music Playlist Manager is a simple yet powerful tool that allows users to create and manage music playlists directly from the command line. Users can create playlists, add songs with details such as song title, artist, and album, remove songs, and view their playlists. All data is stored in a text file for persistence.

## Quick Install

### Prerequisites

- Ensure you have Python 3.6 or higher installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Installation Steps

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the name of the cloned repository.

3. **Install Dependencies:**

   Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## How to Use

### Running the Application

To start the Music Playlist Manager, run the following command in your terminal:

```bash
python main.py
```

### Main Functions

1. **Create Playlist:**

   - Select option `1` from the menu.
   - Enter the desired name for your new playlist.
   - The playlist will be created and stored in the system.

2. **Add Song:**

   - Select option `2` from the menu.
   - Enter the playlist name where you want to add the song.
   - Provide the song title, artist, and album details.
   - The song will be added to the specified playlist.

3. **Remove Song:**

   - Select option `3` from the menu.
   - Enter the playlist name and the song title you wish to remove.
   - The song will be removed from the specified playlist.

4. **View Playlist:**

   - Select option `4` from the menu.
   - Enter the playlist name you want to view.
   - The application will display all songs in the specified playlist.

5. **Exit:**

   - Select option `5` to save your changes and exit the application.

### Data Persistence

All playlists and songs are stored in a text file named `playlists.txt`. The application automatically loads data from this file on startup and saves changes upon exiting.

## Support

For any issues or feature requests, please contact our support team or open an issue in the repository.

Enjoy managing your music playlists with ease!
```