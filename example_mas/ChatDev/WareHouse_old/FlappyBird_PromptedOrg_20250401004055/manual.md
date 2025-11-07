manual.md

```
# Flappy Bird Clone

A simple yet addictive Flappy Bird clone built using Python and Pygame. Navigate your bird through randomly generated pipes by pressing the spacebar to flap and keep your bird airborne. Each successful pass through a pipe increases your score, but beware: colliding with a pipe or hitting the ground will end your game. As your score increases, the game gradually becomes more challenging with narrower gaps and faster pipes.

---

## 🚀 Features

- **Simple Controls:** Press the spacebar to flap and control your bird.
- **Dynamic Difficulty:** Gradually increasing difficulty with narrower gaps and faster pipes as your score increases.
- **Score Tracking:** Keep track of your highest scores and challenge yourself to improve.
- **Instant Restart:** Quickly restart the game after a game over by pressing the spacebar.

---

## 📦 Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone the repository or download the provided source code files.

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

---

## 🎮 How to Play

### Starting the Game

Run the game using the provided shell script or directly via Python:

**Using shell script (Linux/MacOS):**

```bash
sh run.sh
```

**Directly via Python (All platforms):**

```bash
python main.py
```

### Game Controls

- **Flap:** Press the `SPACEBAR` to flap and keep your bird flying.
- **Restart:** After a game over, press the `SPACEBAR` again to restart the game.

---

## 📖 Gameplay Instructions

- Your goal is to navigate your bird safely through the gaps between the pipes.
- Each successful pass through a pair of pipes increases your score by 1.
- The game gradually increases in difficulty:
  - Pipes move faster.
  - Gaps between pipes become narrower.
- The game ends if:
  - Your bird collides with a pipe.
  - Your bird hits the ground or flies off the top of the screen.

---

## 🛠️ Project Structure

```
FlappyBirdClone/
├── bird.py          # Bird class handling bird physics and rendering
├── pipe.py          # Pipe class handling pipe obstacles and collisions
├── game.py          # Game class managing the game loop and logic
├── main.py          # Main file to run the game
├── requirements.txt # Python dependencies
└── run.sh           # Shell script to run the game
```

---

## 🐞 Troubleshooting

### Game doesn't start or crashes immediately:

- Ensure Python 3.6+ is installed correctly.
- Verify that all dependencies are installed by running:
```bash
pip install -r requirements.txt
```

### Controls not responding:

- Make sure the game window is active and selected.
- Press the `SPACEBAR` to flap.

---

## 📌 Dependencies

- [Pygame](https://www.pygame.org/) (version 2.0.0 or higher)

---

## 📧 Support

For any issues, questions, or suggestions, please contact our support team or open an issue in the project's repository.

Enjoy playing and challenge your friends to beat your high score!

```