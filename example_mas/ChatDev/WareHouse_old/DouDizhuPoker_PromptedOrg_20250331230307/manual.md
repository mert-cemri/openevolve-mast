manual.md

```
# Dou Dizhu (Chinese Poker) Game

Welcome to the Dou Dizhu (Chinese Poker) Game, a Python-based interactive application that allows three players to enjoy the classic Chinese card game Dou Dizhu. This software faithfully implements the standard rules, including bidding to determine the landlord, valid card combinations, and the pass-or-beat logic.

---

## 🎴 Overview of Dou Dizhu

Dou Dizhu (斗地主), literally "Fight the Landlord," is a popular Chinese card game played by three players. One player becomes the "landlord," and the other two players form a team to compete against the landlord. The objective is to be the first player to discard all cards or, if you're on the opposing team, prevent the landlord from doing so.

---

## 🚀 Main Features

- **Standard 54-card Deck:** Includes two Jokers (Black Joker and Red Joker).
- **Automatic Shuffling and Dealing:** Cards are shuffled and dealt automatically.
- **Interactive Bidding Phase:** Players bid to become the landlord.
- **Landlord Determination:** The landlord receives three extra bottom cards.
- **Valid Card Combinations:** Supports singles, pairs, and Joker bombs.
- **Pass-or-Beat Logic:** Players must beat the previous combination or pass.
- **Interactive Gameplay:** Players input their moves via the command line.
- **Win Condition:** Automatically detects and announces the winner.

---

## 📥 Installation and Setup

### Prerequisites

- Python 3.x installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation Steps

1. **Clone or Download the Repository**

   Clone the repository using Git:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

   Alternatively, download and extract the ZIP file.

2. **Install Dependencies**

   This project does not require any external dependencies. However, ensure your Python environment is properly set up.

   ```bash
   # No external dependencies required for this project.
   ```

---

## 🎮 How to Play

### Starting the Game

Navigate to the project directory and run the game using the following command:

```bash
python main.py
```

### Gameplay Instructions

1. **Bidding Phase**

   - Each player will be shown their hand.
   - Players will be prompted to bid for the landlord position by typing `y` (yes) or `n` (no).
   - The first player to bid becomes the landlord and receives the three bottom cards. If no player bids, the first player becomes the landlord by default.

2. **Playing Cards**

   - Players take turns playing cards or passing.
   - When prompted, enter the cards you wish to play separated by spaces (e.g., `3♠ 3♦`) or type `pass` to skip your turn.
   - Valid combinations include:
     - **Single Card:** Any single card.
     - **Pair:** Two cards of the same rank.
     - **Joker Bomb:** Both Jokers played together (Black Joker and Red Joker), which beats any other combination.

3. **Pass-or-Beat Logic**

   - You must play a combination that beats the previously played combination or pass.
   - If no previous combination exists (e.g., after everyone passes), you can play any valid combination.

4. **Winning the Game**

   - The first player to discard all their cards wins.
   - If the landlord wins, the landlord wins individually.
   - If either of the other two players wins, both non-landlord players win as a team.

---

## 🃏 Example Gameplay

```
Player1's hand: 3♠ 4♦ 5♣ 6♥ 7♠ 8♦ 9♣ 10♥ J♠ Q♦ K♣ A♥ 2♠ 2♦ Black Joker Red Joker
Player1, do you want to bid as landlord? (y/n): y
Player1 is the landlord.

Player1's turn.
Player1's hand: 3♠ 4♦ 5♣ 6♥ 7♠ 8♦ 9♣ 10♥ J♠ Q♦ K♣ A♥ 2♠ 2♦ Black Joker Red Joker
Player1, enter cards to play separated by spaces (or 'pass'): 3♠

Player1 played: 3♠

Player2's turn.
Player2's hand: 4♠ 4♥ 5♦ 5♥ 6♣ 6♦ 7♥ 7♦ 8♣ 8♠ 9♦ 9♥ 10♣ 10♦ J♣
Player2, enter cards to play separated by spaces (or 'pass'): pass
Player2 passes.

Player3's turn.
Player3's hand: 3♦ 3♣ 4♣ 5♠ 6♠ 7♣ 8♥ 9♠ 10♠ J♦ Q♣ K♦ A♣ 2♣ 2♥
Player3, enter cards to play separated by spaces (or 'pass'): 4♣

Player3 played: 4♣
```

---

## 📖 Project Structure

```
DouDizhuGame/
├── card.py          # Defines the Card class
├── deck.py          # Handles card creation, shuffling, and dealing
├── player.py        # Represents each player and their actions
├── game_logic.py    # Contains the game logic, bidding, and validation
├── main.py          # Entry point to start the game
└── requirements.txt # Lists external dependencies (none required)
```

---

## 📞 Support and Feedback

If you encounter any issues or have suggestions for improvements, please reach out to our support team or open an issue on our GitHub repository.

Enjoy playing Dou Dizhu!

--- 

© 2023 ChatDev. All rights reserved.
```