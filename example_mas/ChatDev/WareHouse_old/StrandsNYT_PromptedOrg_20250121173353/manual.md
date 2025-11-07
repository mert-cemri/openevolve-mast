# NYT Strands Puzzle

Welcome to the NYT Strands Puzzle! This application allows players to connect word segments to form valid words or phrases. Each connected segment should produce a meaningful solution, and players receive confirmation for correct strand formations.

## Main Functions

The NYT Strands Puzzle application consists of the following main components:

1. **WordSegment Class**: Represents a segment of a word or phrase in the puzzle.
2. **Puzzle Class**: Manages the collection of word segments and validates connections between them.
3. **Game Class**: Handles the game logic, including user interactions and confirmations.
4. **Main Script**: Initiates the game and allows players to start playing.

## Installation

To run the NYT Strands Puzzle, you need to have Python installed on your system. Follow these steps to set up the environment and install necessary dependencies:

1. **Clone the Repository**: Clone the project repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment**: It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**: Install the required dependencies using pip.

   ```bash
   pip install -r requirements.txt
   ```

   Note: Ensure that you have a `dictionary.txt` file in the project directory containing a list of valid words, one per line.

## How to Play

1. **Start the Game**: Run the main script to start the game.

   ```bash
   python main.py
   ```

2. **Game Instructions**: Once the game starts, you will see a list of available word segments.

3. **Make Selections**: Select two segments by entering their indices to attempt to form a valid word or phrase.

4. **Receive Feedback**: The game will confirm if the connection is correct or prompt you to try again if it's invalid.

5. **Repeat**: Continue making selections until you successfully connect all segments or decide to exit the game.

Enjoy playing the NYT Strands Puzzle and challenge yourself to form as many valid words or phrases as possible!