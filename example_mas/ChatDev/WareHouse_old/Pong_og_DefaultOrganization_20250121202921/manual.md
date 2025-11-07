```markdown
# Pong Game

A classic two-player Pong game developed using Python and Pygame. Each player controls a vertical paddle, moving up and down to bounce a ball back. The ball bounces between the two paddles and off the top and bottom edges. Players score a point when the opponent misses the ball.

## Main Functions

- **Two-Player Mode**: Engage in a competitive match with another player.
- **Paddle Control**: Each player controls a paddle using keyboard keys.
- **Ball Dynamics**: The ball bounces off paddles and screen edges, increasing speed with each paddle hit.
- **Score Tracking**: A scoreboard displays the current score of both players.

## Installation

### Environment Setup

To run the Pong game, you need to have Python and Pygame installed on your system. Follow the steps below to set up your environment:

1. **Install Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Pygame**: Use pip to install Pygame, a set of Python modules designed for writing video games.

   Open your terminal or command prompt and run the following command:

   ```bash
   pip install pygame==2.1.2
   ```

   Alternatively, you can use a `requirements.txt` file to install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## How to Play

1. **Start the Game**: Run the `main.py` file to start the game. You can do this by navigating to the directory containing the game files and executing:

   ```bash
   python main.py
   ```

2. **Control the Paddles**:
   - Player 1 uses the `W` key to move the paddle up and the `S` key to move it down.
   - Player 2 uses the `UP` arrow key to move the paddle up and the `DOWN` arrow key to move it down.

3. **Game Objective**: The objective is to bounce the ball back to the opponent using your paddle. If the opponent misses the ball, you score a point.

4. **Winning the Game**: The game continues until you decide to quit. Keep track of your score on the scoreboard displayed at the top of the screen.

5. **Quit the Game**: To exit the game, close the game window or press `ESC` to quit.

Enjoy playing the classic Pong game with a friend and test your reflexes and skills!

## Additional Information

For any issues or further assistance, please contact our support team or refer to the Pygame documentation for more details on game development using Pygame.
```