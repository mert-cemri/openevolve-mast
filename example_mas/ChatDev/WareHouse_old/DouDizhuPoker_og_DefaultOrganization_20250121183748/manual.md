# Dou Dizhu Game Application

Welcome to the Dou Dizhu Game Application, a digital implementation of the popular Chinese card game, Dou Dizhu. This application allows you to play Dou Dizhu with three players, including one designated as the 'landlord'. The objective is to be the first to run out of cards or prevent the landlord from doing so, following the standard Dou Dizhu rules.

## Main Functions

- **Game Setup**: Initialize the game with three players, shuffle the deck, and deal cards.
- **Player Turns**: Players take turns to play valid card combinations.
- **Card Combinations**: Supports singles, pairs, triples, straights, full houses, bombs, and more.
- **Winning Condition**: The game checks for a winner when a player runs out of cards.
- **Graphical User Interface**: A simple GUI to interact with the game.

## Installation

To run the Dou Dizhu Game Application, you need to set up your environment with the necessary dependencies. Follow these steps to install the required packages:

1. **Clone the Repository**: First, clone the repository to your local machine.

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install Dependencies**: Use `pip` to install the required Python packages listed in `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

    This will install the following packages:
    - `pyvirtualdisplay`: For managing virtual displays, especially useful in headless environments.
    - `Pillow`: A Python Imaging Library used for image processing.

## How to Play

1. **Start the Application**: Run the `main.py` file to start the game.

    ```bash
    python main.py
    ```

2. **Game Interface**: A window will open with a "Start Game" button. Click this button to begin the game.

3. **Gameplay**:
    - The game will shuffle the deck and deal cards to each player.
    - The landlord will receive three extra cards.
    - Players take turns to play valid card combinations.
    - The game will display whose turn it is and update the status as the game progresses.

4. **Winning the Game**: The game ends when a player runs out of cards. The winner's name will be displayed.

## Additional Information

- **Game Rules**: The game follows standard Dou Dizhu rules. Players can play singles, pairs, triples, straights, full houses, and bombs. The game logic ensures that only valid plays are accepted.
- **User Interface**: The application uses `tkinter` for the graphical user interface, providing a simple and interactive way to play the game.

Enjoy playing Dou Dizhu and may the best strategist win! If you encounter any issues or have questions, please refer to the documentation or contact support for assistance.