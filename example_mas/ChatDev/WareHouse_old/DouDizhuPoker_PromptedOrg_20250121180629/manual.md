# Dou Dizhu Game User Manual

Welcome to the Dou Dizhu game, a classic Chinese poker game for three players. This software allows you to experience the excitement of Dou Dizhu, where one player becomes the 'landlord' and the others work together to prevent the landlord from winning. The objective is to be the first to run out of cards or to stop the landlord from doing so.

## Main Functions

- **Game Initialization**: Start a new game with three players, one of whom will be randomly assigned as the landlord.
- **Card Dealing**: Automatically shuffle and deal cards to each player.
- **Gameplay**: Players take turns playing valid combinations of cards, such as singles, pairs, straights, and more.
- **Landlord Determination**: The game determines the landlord at the beginning of each game.
- **Win Condition**: The game ends when a player runs out of cards, and the winner is declared.

## Installation

To play the Dou Dizhu game, you need to have Python installed on your system. Follow these steps to set up the environment and run the game:

### Step 1: Install Python

Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Clone the Repository

Clone the repository containing the Dou Dizhu game code to your local machine:

```bash
git clone <repository-url>
```

### Step 3: Navigate to the Project Directory

Change your current directory to the project directory:

```bash
cd <repository-directory>
```

### Step 4: Install Dependencies

The game does not require any external Python packages beyond the standard library. However, if any dependencies are added in the future, you can install them using:

```bash
pip install -r requirements.txt
```

### Step 5: Run the Game

Execute the main script to start the game:

```bash
python main.py
```

## How to Play

1. **Start the Game**: Run the `main.py` script to initialize the game. The game will automatically shuffle and deal cards to the three players.

2. **Determine the Landlord**: The game will randomly assign one player as the landlord. The landlord has a slight advantage with extra cards.

3. **Take Turns**: Players take turns playing valid card combinations. The game will prompt each player to play their turn.

4. **Valid Combinations**: The game supports various card combinations, including:
   - Singles: One card.
   - Pairs: Two cards of the same rank.
   - Triples: Three cards of the same rank.
   - Bomb: Four cards of the same rank.
   - Rocket: Two Jokers.
   - Straight: A sequence of at least five consecutive cards.

5. **Winning the Game**: The game ends when a player runs out of cards. The first player to do so wins the game.

6. **Prevent the Landlord**: If the landlord runs out of cards first, the landlord wins. The other players must work together to prevent this.

## Additional Information

For more information on the rules and strategies of Dou Dizhu, you can refer to online resources or tutorials on Chinese poker games.

Enjoy playing Dou Dizhu and may the best strategist win!