manual.md

```
# Simplified Monopoly Go!

A simplified Python implementation of the classic Monopoly board game, featuring essential mechanics such as rolling dice, moving around properties, buying properties, collecting rent, handling chance events, and managing special positions like Jail and Free Parking.

---

## 🎲 Game Features

- **Dice Rolling:** Players roll a dice to move around the board.
- **Property Management:** Players can buy properties, pay rent, and manage their finances.
- **Chance Cards:** Random events that can positively or negatively affect players' finances or positions.
- **Special Positions:** Includes Jail, Free Parking, and Go positions with simplified rules.
- **Player Management:** Tracks player money, property ownership, and jail status.
- **Game Over Conditions:** The game ends when a player goes bankrupt, declaring the other player as the winner.

---

## 💻 Installation and Setup

### Prerequisites

- Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Dependencies

This project does not require any external dependencies. However, ensure your Python environment is properly set up.

### Installation Steps

1. **Clone the Repository**

```bash
git clone <repository-url>
cd <repository-directory>
```

2. **Verify Python Installation**

```bash
python --version
```

Ensure Python 3.x is installed.

---

## 🚀 How to Play

### Starting the Game

Run the following command in your terminal from the project's root directory:

```bash
python main.py
```

### Gameplay Instructions

- The game supports two players: Player 1 and Player 2.
- Each player starts with $1500.
- Players take turns rolling a dice to move around the board.
- Landing on an unowned property gives the player the option to buy it.
- Landing on a property owned by another player requires paying rent.
- Landing on "Chance" triggers a random event card.
- Landing on "Jail" sends the player to jail, where they must roll a 4 or higher to get out on their next turn.
- Landing on "Free Parking" has no effect.
- Passing or landing on "Go" awards the player $200.

### Game Flow

- **Roll Dice:** Press Enter when prompted to roll the dice.
- **Buy Properties:** When landing on an available property, type `y` to buy or `n` to skip.
- **Pay Rent:** Automatically handled when landing on another player's property.
- **Chance Cards:** Automatically drawn and executed when landing on a Chance position.
- **Jail:** Automatically handled; roll dice to attempt to leave jail.

### Ending the Game

- The game ends automatically when a player goes bankrupt (money reaches $0).
- The player with remaining money is declared the winner.

---

## 📂 Project Structure

```
SimplifiedMonopolyGo/
├── main.py             # Entry point to start the game
├── game.py             # Manages game flow and player turns
├── player.py           # Defines player attributes and actions
├── property.py         # Defines properties on the board
├── chance.py           # Defines chance cards and their effects
├── board.py            # Manages the game board and positions
└── requirements.txt    # Lists external dependencies (none required)
```

---

## 📖 Example Gameplay

```
Welcome to Simplified Monopoly Go!

Player 1's turn. Current balance: $1500
Press Enter to roll dice...
Player 1 rolled a 4
Player 1 moved to position 4
Player 1 landed on an empty space. Nothing happens.

Player 2's turn. Current balance: $1500
Press Enter to roll dice...
Player 2 rolled a 3
Player 2 moved to position 3
Property 3 is available for $120. Buy? (y/n): y
Player 2 bought Property 3 for $120

Player 1's turn. Current balance: $1500
Press Enter to roll dice...
Player 1 rolled a 6
Player 1 moved to position 10
Player 1 landed in Jail!

Player 2's turn. Current balance: $1380
Press Enter to roll dice...
Player 2 rolled a 4
Player 2 moved to position 7
Chance Card: Win lottery! Collect $200
Player 2's new balance: $1580
```

---

## 🛠️ Troubleshooting

- **Game won't start:** Ensure Python is correctly installed and you're running the command from the correct directory.
- **Unexpected behavior:** Restart the game and ensure no files have been modified unintentionally.

---

## 📞 Support

For further assistance or to report issues, please contact our support team or open an issue in the project's repository.

Enjoy playing Simplified Monopoly Go! 🎉
```