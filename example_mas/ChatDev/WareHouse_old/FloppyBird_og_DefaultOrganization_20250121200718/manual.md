manual.md

```
# Flappy Bird Clone

Welcome to the Flappy Bird Clone! This is a simple yet addictive game where you control a bird trying to fly through gaps in pipes without hitting them or the ground. Each successful pass through a gap increases your score. The game ends if the bird collides with a pipe or the ground.

## Main Functions

- **Bird Control**: Press the spacebar to make the bird flap its wings and ascend. The bird will descend gradually due to gravity.
- **Pipe Obstacles**: Pipes with gaps will move from right to left. Navigate the bird through these gaps to score points.
- **Scoring System**: Each successful pass through a pipe gap increases your score by one point.
- **Game Over**: The game ends if the bird collides with a pipe or the ground.

## Installation

To play the Flappy Bird Clone, you need to have Python and Pygame installed on your system. Follow the steps below to set up your environment:

### Step 1: Install Python

Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Pygame

Pygame is a set of Python modules designed for writing video games. You can install it using pip:

```bash
pip install pygame==2.1.2
```

Alternatively, you can use the `requirements.txt` file provided with the project to install dependencies:

```bash
pip install -r requirements.txt
```

## How to Play

1. **Clone the Repository**: Download or clone the repository containing the game code to your local machine.

2. **Navigate to the Game Directory**: Open a terminal or command prompt and navigate to the directory where the game files are located.

3. **Run the Game**: Execute the following command to start the game:

   ```bash
   python main.py
   ```

4. **Control the Bird**: Use the spacebar to make the bird flap its wings. Try to navigate through the gaps in the pipes.

5. **Score Points**: Each time you successfully pass through a pipe gap, your score increases.

6. **Game Over**: The game will end if the bird hits a pipe or the ground. You can restart the game by running the `main.py` file again.

## Additional Information

- **Customization**: You can modify the game parameters such as screen size, bird speed, pipe speed, and gap size by editing the constants in the respective Python files (`main.py`, `bird.py`, `pipe.py`).

- **Future Extensions**: The `utils.py` file is currently empty but can be used for adding utility functions or additional features in the future.

Enjoy playing the Flappy Bird Clone and challenge yourself to achieve the highest score possible!
```