# Music Playlist Manager CLI

## Overview

The Music Playlist Manager CLI is a command-line interface application designed to help users manage their music playlists. It allows users to create, delete, add songs to, remove songs from, and view playlists. All playlist data is stored in a text file named `playlists.txt`.

## Features

- **Create Playlist**: Create a new playlist with a specified name.
- **Delete Playlist**: Delete an existing playlist.
- **Add Song**: Add a song to a specified playlist by providing the song title, artist, and album.
- **Remove Song**: Remove a song from a specified playlist by providing the song title.
- **View Playlist**: View all songs in a specified playlist.
- **Save and Load Playlists**: Automatically save playlists to a text file and load them when the application starts.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps to Install

1. **Clone the Repository** (if you haven't already):
   ```bash
   git clone https://github.com/your-repo/music-playlist-manager.git
   cd music-playlist-manager
   ```

2. **Install Dependencies**:
   The project currently does not require any external dependencies beyond Python's standard library. However, if you have a `requirements.txt` file with dependencies, you can install them using:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

To start the Music Playlist Manager CLI, run the following command in your terminal:
```bash
python main.py
```

### Commands

- **Create Playlist**:
  ```bash
  create
  ```
  Enter the playlist name when prompted.

- **Delete Playlist**:
  ```bash
  delete
  ```
  Enter the playlist name you wish to delete when prompted.

- **Add Song**:
  ```bash
  add
  ```
  Enter the playlist name, song title, artist, and album when prompted.

- **Remove Song**:
  ```bash
  remove
  ```
  Enter the playlist name and the song title you wish to remove when prompted.

- **View Playlist**:
  ```bash
  view
  ```
  Enter the playlist name you wish to view when prompted.

- **Exit**:
  ```bash
  exit
  ```
  This command will save all changes to `playlists.txt` and exit the application.

## Data Storage

All playlist data is stored in a text file named `playlists.txt` in the same directory as the application. The file format is as follows:

```
Playlist: PlaylistName
SongTitle - Artist - Album
SongTitle - Artist - Album
...
```

Each playlist is separated by a line starting with `Playlist:`, followed by the playlist name. Each song in the playlist is listed on a new line in the format `SongTitle - Artist - Album`.

## Example Workflow

1. **Start the Application**:
   ```bash
   python main.py
   ```

2. **Create a Playlist**:
   ```
   Enter a command (create, delete, add, remove, view, exit): create
   Enter playlist name: My Favorite Songs
   Playlist 'My Favorite Songs' created.
   ```

3. **Add Songs**:
   ```
   Enter a command (create, delete, add, remove, view, exit): add
   Enter playlist name: My Favorite Songs
   Enter song title: Bohemian Rhapsody
   Enter artist: Queen
   Enter album: The Game
   Song 'Bohemian Rhapsody' added to playlist 'My Favorite Songs'.
   ```

4. **View Playlist**:
   ```
   Enter a command (create, delete, add, remove, view, exit): view
   Enter playlist name: My Favorite Songs
   Playlist 'My Favorite Songs':
    - Bohemian Rhapsody by Queen from The Game
   ```

5. **Exit the Application**:
   ```
   Enter a command (create, delete, add, remove, view, exit): exit
   Playlists saved.
   Exiting...
   ```

## Troubleshooting

- **Application Crashes**: Ensure that Python is correctly installed and that you are running the application from the correct directory.
- **Data Loss**: If you encounter issues with data persistence, ensure that the `playlists.txt` file is not being modified or deleted outside of the application.

## Contributing

We welcome contributions to the Music Playlist Manager CLI. Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or need further assistance!

---

This manual should provide a comprehensive guide for users to understand and use the Music Playlist Manager CLI effectively.