```markdown
# Dou Dizhu Game Application

Welcome to the Dou Dizhu Game Application, a digital implementation of the popular Chinese card game for three players. This application allows you to experience the strategic and exciting gameplay of Dou Dizhu, where one player is designated as the 'landlord' and the objective is to be the first to run out of cards or prevent the landlord from doing so.

## Main Functions

- **Game Setup**: Automatically deals cards to three players and determines the landlord.
- **Gameplay**: Players take turns playing valid card combinations according to Dou Dizhu rules.
- **Winning Conditions**: The game checks for win conditions after each turn, declaring a winner when a player runs out of cards.
- **Graphical User Interface**: Provides a visual representation of the game state, including players' hands and game actions.

## Quick Install

To install the required environment dependencies, ensure you have Python installed and then run the following command to install the necessary package:

```bash
pip install pygame>=2.0.0
```

## How to Use/Play

### Running the Game

1. **Clone the Repository**: Ensure you have access to the game files, including `main.py`, `game.py`, `player.py`, `deck.py`, `gui.py`, and `rules.py`.

2. **Install Dependencies**: As mentioned above, install the `pygame` library using pip.

3. **Start the Game**: Run the `main.py` file to start the game application. You can do this by navigating to the directory containing the files and executing:

   ```bash
   python main.py
   ```

### Playing the Game

- **Game Interface**: Once the game starts, a window will open displaying the game interface. Each player's hand is shown, and the game progresses turn by turn.

- **Player Actions**: Players can interact with the game using keyboard inputs. For example, pressing the spacebar can be used to play selected cards (additional logic for card selection needs to be implemented).

- **Game Rules**: The game follows standard Dou Dizhu rules for valid card combinations, including singles, pairs, triples, straights, bombs, and rockets. The rules are implemented in `rules.py`.

- **Winning the Game**: The game will automatically detect when a player has won by running out of cards and will display a message indicating the winner.

## Documentation

For more detailed information on the game's rules and gameplay mechanics, please refer to the `rules.py` file, which contains the logic for validating card combinations. Additional game logic can be found in `game.py`, which handles the main game flow and player interactions.

Enjoy playing Dou Dizhu, and may the best strategist win!
```