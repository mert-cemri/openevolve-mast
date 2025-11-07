manual.md

```
# Two-Player Pong Game 🎮

Welcome to the Two-Player Pong Game! This classic arcade-style game allows two players to compete against each other by controlling vertical paddles to bounce a ball back and forth. Score points by making your opponent miss the ball. The first player to reach the winning score threshold wins the game!

---

## 🚀 Main Features

- **Two-Player Gameplay:** Compete against a friend locally on the same computer.
- **Responsive Controls:** Smooth paddle movements using keyboard inputs.
- **Dynamic Ball Movement:** Ball bounces realistically off paddles and screen edges.
- **Scoring System:** Automatic scoring when a player misses the ball.
- **Winning Threshold:** First player to reach 5 points wins.
- **Automatic Ball Reset:** Ball resets to the center after each point scored.

---

## 🛠️ Installation

### Step 1: Clone the Repository

Clone the game repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Set Up Python Environment

Make sure you have Python installed (version 3.7 or higher recommended). You can download Python from [python.org](https://www.python.org/downloads/).

### Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

---

## 🎮 How to Play

### Launching the Game

Run the game by executing the following command in your terminal:

```bash
python main.py
```

### Game Controls

| Player | Move Paddle Up ⬆️ | Move Paddle Down ⬇️ |
|--------|-------------------|---------------------|
| Left   | `W`               | `S`                 |
| Right  | `UP Arrow`        | `DOWN Arrow`        |

### Gameplay Instructions

- Each player controls a paddle on their respective side of the screen.
- Move your paddle vertically to bounce the ball back to your opponent.
- Score points by making your opponent miss the ball.
- The ball will bounce off the top and bottom edges of the screen.
- After each point, the ball resets to the center with random initial velocity.
- The first player to reach 5 points wins the game.

---

## 🏆 Winning the Game

- The game automatically ends when a player reaches the winning score threshold (5 points).
- The winner will be displayed in the terminal window.
- To play again, simply restart the game by running `python main.py` again.

---

## 📂 Project Structure

```
Two-Player-Pong-Game/
├── main.py           # Main game logic and execution
├── paddle.py         # Paddle class definition
├── ball.py           # Ball class definition
└── requirements.txt  # Python dependencies
```

---

## 📌 Dependencies

The game relies on the following Python library:

- **pygame** (version 2.0.0 or higher)

---

## 🛎️ Support & Feedback

If you encounter any issues or have suggestions for improvements, please reach out to our support team or open an issue in the repository.

Enjoy the game and have fun competing with your friends! 🎉

---