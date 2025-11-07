```markdown
# Blackjack Game User Manual

Welcome to the Blackjack Game! This application allows you to play the classic card game Blackjack, also known as 21, against a computer dealer. The game follows standard Blackjack rules and provides an interactive graphical user interface (GUI) for an engaging experience.

## Main Functions

- **Hit**: Draw an additional card to your hand.
- **Stand**: Keep your current hand and end your turn.
- **Double Down**: Double your initial bet, draw one more card, and then stand.
- **Game Logic**: The dealer hits until their hand value is at least 17. The winner is determined based on the hand values, with the goal being to get as close to 21 as possible without exceeding it.

## Installation

### Prerequisites

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: Download the game code to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: This game does not require any external Python packages, so no additional installations are necessary.

## How to Play

1. **Run the Game**: Navigate to the directory containing the game files and execute the main script.
   ```bash
   python main.py
   ```

2. **Game Interface**: Once the game starts, a window will appear with buttons for "Hit", "Stand", and "Double Down". The current scores for both the player and the dealer will be displayed.

3. **Start a New Round**: The game begins with an initial bet (default is 10). You can adjust this in the code if desired.

4. **Player Actions**:
   - **Hit**: Click the "Hit" button to draw another card.
   - **Stand**: Click the "Stand" button to end your turn and let the dealer play.
   - **Double Down**: Click the "Double Down" button to double your bet, draw one more card, and end your turn.

5. **Determine the Winner**: After the player stands or busts, the dealer will play their hand. The game will then display the result, indicating whether the player or dealer has won, or if it's a tie.

6. **Restart**: To play another round, simply close the game window and restart the application.

## Additional Information

- **Game Rules**: The dealer must hit until their hand value is at least 17. Aces count as 1 or 11, depending on which value is more favorable for the hand.
- **Winning Conditions**: The player wins if their hand value is closer to 21 than the dealer's without exceeding 21. If both the player and dealer have the same hand value, it's a tie.

Enjoy playing Blackjack and may the best hand win!
```
