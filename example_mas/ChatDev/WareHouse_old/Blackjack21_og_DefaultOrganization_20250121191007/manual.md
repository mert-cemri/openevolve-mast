```markdown
# Blackjack Game User Manual

Welcome to the Blackjack Game! This application allows you to play a classic game of Blackjack against a dealer. The game follows standard Blackjack rules, where the dealer hits up to 16 and stands on 17 or above. As a player, you can choose to 'hit,' 'stand,' or 'double down' when appropriate. The game tracks totals, detects busts, and determines the winner after each round.

## Main Functions

- **Start Game**: Begin a new game of Blackjack. The player and dealer are each dealt two cards initially.
- **Player Actions**: Choose from 'hit,' 'stand,' or 'double down' during your turn.
  - **Hit**: Draw an additional card.
  - **Stand**: End your turn without drawing more cards.
  - **Double Down**: Double your bet, draw one more card, and end your turn.
- **Dealer Actions**: The dealer automatically plays after the player stands or busts, hitting until reaching at least 17.
- **Determine Winner**: After both the player and dealer have completed their turns, the game determines the winner based on the card values.

## Installation

This application is built using Python and requires no external dependencies. Follow these steps to set up and run the game:

### Prerequisites

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: Download the game files to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Game**: Execute the main script to start the game.
   ```bash
   python main.py
   ```

## How to Play

1. **Launch the Game**: Run the `main.py` script to start the game. A graphical user interface (GUI) will appear.

2. **Game Interface**: 
   - The GUI displays the current card values for both the player and the dealer.
   - Use the buttons to choose your action: 'Hit', 'Stand', or 'Double Down'.

3. **Gameplay**:
   - The player starts with a bankroll of 100 units and can place bets at the beginning of each round.
   - After placing a bet, the player is dealt two cards, and the dealer is dealt one card face up and one card face down.
   - The player can choose to 'hit' to receive another card, 'stand' to end their turn, or 'double down' to double their bet and receive one final card.
   - The dealer will then play according to the rules, hitting until their hand value is at least 17.

4. **Winning the Game**:
   - The winner is determined based on the card values. If the player's hand exceeds 21, they bust, and the dealer wins. If the dealer busts or the player's hand is closer to 21 than the dealer's, the player wins.

5. **End of Round**: After determining the winner, the game resets for another round, allowing the player to continue playing with their remaining bankroll.

Enjoy playing Blackjack and may the odds be in your favor!
```