```markdown
# Blackjack Game

Welcome to the Blackjack Game, a classic card game implemented in Python with a graphical user interface (GUI) using Tkinter. This game allows you to play Blackjack against a dealer following standard rules.

## Main Features

- **Player Actions**: Choose to 'Hit', 'Stand', or 'Double Down' during your turn.
- **Dealer Rules**: The dealer hits until reaching a total of 17 or more.
- **Game Logic**: Automatically tracks totals, detects busts, and determines the winner after each round.
- **Graphical User Interface**: Easy-to-use interface built with Tkinter.

## Installation Guide

### Prerequisites

- Ensure you have Python installed on your system. The game is compatible with Python 3.6 and above.

### Installing Dependencies

1. Clone the repository or download the source code files to your local machine.
2. Navigate to the directory containing the source code.
3. Install the required dependencies using pip. Open your terminal or command prompt and run:

   ```bash
   pip install -r requirements.txt
   ```

   Note: The `requirements.txt` file is currently empty as the game primarily uses the standard library. Ensure Tkinter is available in your Python installation.

## How to Play

1. **Start the Game**: Run the `main.py` file to launch the game. You can do this by executing the following command in your terminal:

   ```bash
   python main.py
   ```

2. **Game Interface**: Once the game starts, a window will appear displaying the player's and dealer's hands.

3. **Player Actions**:
   - **Hit**: Click the "Hit" button to draw another card.
   - **Stand**: Click the "Stand" button to end your turn and let the dealer play.
   - **Double Down**: Click the "Double Down" button to double your bet, draw one more card, and then stand.

4. **Game Outcome**: The game will automatically determine the winner based on the rules of Blackjack:
   - If your hand exceeds 21, you bust, and the dealer wins.
   - If the dealer busts, you win.
   - If neither busts, the hand with the higher total wins.
   - If both hands have the same total, it's a tie.

5. **New Game**: Click the "New Game" button to start a new round.

## Additional Information

- **Card Values**: Number cards are worth their face value, face cards (Jack, Queen, King) are worth 10, and Aces can be worth 1 or 11, depending on which is more favorable for the hand.
- **Dealer Strategy**: The dealer will continue to draw cards until their hand totals 17 or more.

Enjoy playing Blackjack and may the best hand win!
```
