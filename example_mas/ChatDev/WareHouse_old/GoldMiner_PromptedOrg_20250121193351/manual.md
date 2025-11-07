# Gold Miner Game

Welcome to the Gold Miner Game! This game challenges players to collect gold and other objects using a claw that moves back and forth. The player must time their grabs to collect objects, each with a specific value and weight. The game ends when the time runs out or the minimum gold value is met.

## Main Functions

- **Claw Movement**: The claw moves left and right across the screen. The player controls the movement to position the claw over objects.
- **Object Grabbing**: The player can grab objects when the claw is positioned correctly. Each object has a value and weight that affects the game outcome.
- **Game Conditions**: The game ends when the player collects enough gold to meet the minimum value or when the time limit is reached.
- **Display**: The game displays the current position of the claw and the status of objects (grabbed or available).

## Installation

### Environment Setup

The Gold Miner Game is developed in Python and does not require any external dependencies. Ensure you have Python installed on your system.

### Installation Steps

1. **Clone the Repository**: Download the game files from the repository or copy the provided code into your local directory.

2. **Navigate to the Game Directory**: Open your terminal or command prompt and navigate to the directory containing the game files.

3. **Run the Game**: Execute the following command to start the game:
   ```bash
   python main.py
   ```

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game. The game will initialize and display the starting positions of the claw and objects.

2. **Control the Claw**: Use the following keyboard inputs to control the claw:
   - Press `'l'` to move the claw left.
   - Press `'r'` to move the claw right.
   - Press `'g'` to grab an object.

3. **Objective**: Collect objects to accumulate a total value that meets or exceeds the minimum gold value before the time runs out.

4. **Game End**: The game will display a message indicating whether you win by collecting enough gold or if the time has run out.

5. **Replay**: Restart the game by running the `main.py` file again.

## Game Strategy

- **Timing**: Pay attention to the timing of your grabs. Objects have different weights, affecting how long it takes to reel them in.
- **Positioning**: Move the claw strategically to position it over high-value objects.
- **Time Management**: Keep an eye on the remaining time and prioritize grabbing objects that will help you reach the minimum gold value quickly.

Enjoy playing the Gold Miner Game and challenge yourself to collect the most gold!