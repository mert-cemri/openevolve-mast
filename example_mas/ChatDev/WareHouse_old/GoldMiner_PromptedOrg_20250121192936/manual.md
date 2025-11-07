# Gold Miner Game

Welcome to the Gold Miner Game! This is a simple yet engaging game where you control a claw to collect gold and other objects. The goal is to collect enough gold before the time runs out.

## Main Functions

- **Claw Movement**: The claw moves back and forth across the screen. You can time your grab to collect objects.
- **Object Collection**: Each object has a value and takes time to reel in. Objects include gold and rocks, each with different values.
- **Win Condition**: The level ends when the time runs out or the minimum gold value is met.
- **Display**: The game displays the position of the claw and objects, updating after each grab.

## Installation

### Environment Setup

To play the Gold Miner Game, you need to have Python installed on your system. Follow these steps to set up your environment:

1. **Install Python**: If you don't have Python installed, download and install it from [python.org](https://www.python.org/).

2. **Clone the Repository**: Clone the game repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: Currently, there are no external dependencies required. However, if you plan to enhance the game with graphical features using `pygame`, you can uncomment the line in `requirements.txt` and install it.

   ```bash
   # Uncomment the following line in requirements.txt if using pygame
   # pygame==2.0.1

   pip install -r requirements.txt
   ```

## How to Play

1. **Start the Game**: Run the main module to start the game.

   ```bash
   python main.py
   ```

2. **Game Controls**:
   - The claw will automatically move back and forth.
   - Press 'g' to grab an object when the claw is in the desired position.
   - Press 'c' to continue without grabbing.

3. **Objective**: Collect enough gold to meet or exceed the minimum gold value before the time runs out.

4. **Game Display**: The game will display the current position of the claw and the status of objects (whether they are collected or available).

5. **Win/Lose Conditions**:
   - Win: Collect the minimum required gold value before time runs out.
   - Lose: Time runs out before collecting enough gold.

Enjoy playing the Gold Miner Game and challenge yourself to collect as much gold as possible!