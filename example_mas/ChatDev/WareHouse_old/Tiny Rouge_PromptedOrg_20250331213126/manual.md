manual.md

```
# Tower of the Sorcerer Roguelike Game

Welcome to the Tower of the Sorcerer inspired roguelike game! This manual provides detailed instructions on how to install, run, and play the game.

---

## 🎮 Overview

In this roguelike adventure, you control a brave hero navigating through a challenging dungeon. Your goal is to reach the door at the end of each level while battling monsters and collecting treasures to restore your health. Each level is randomly generated, ensuring a unique experience every time you play.

---

## 🚀 Features

- **Randomly Generated Levels:** Each playthrough provides a unique 80x80 grid map with guaranteed valid paths.
- **Simple Controls:** Move your character using the W/A/S/D keys.
- **Combat System:** Engage monsters by moving onto their tile; combat is resolved instantly by subtracting the monster's HP from your HP.
- **Treasure Chests:** Restore your HP by 20–30 points when you collect treasure chests.
- **Minimal UI:** Clearly displays your current HP and encountered monster stats.

---

## 🛠️ Installation

### Prerequisites

Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Step-by-Step Installation

1. **Clone or Download the Repository**

   Clone the repository using git:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

   Alternatively, download and extract the ZIP file.

2. **Set up a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**

   Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running the Game

To start the game, run the following command from the project's root directory:

```bash
python main.py
```

---

## 🎯 How to Play

### Controls

- **W:** Move Up
- **A:** Move Left
- **S:** Move Down
- **D:** Move Right

### Gameplay Mechanics

- **Movement:** You can only move onto floor tiles (black tiles). Walls (gray tiles) are impassable.
- **Combat:** When you move onto a tile occupied by a monster (red tile), combat occurs automatically. Your HP will decrease by the monster's HP, and the monster will be defeated.
- **Treasure Chests:** Collect treasures (gold tiles) to restore your HP by 20–30 points. Your HP cannot exceed 100.
- **Door:** Reach the green tile (door) to complete the level and win the game.

### UI Elements

- **Player HP:** Displayed at the top-left corner of the screen, indicating your current health points.

---

## 🐞 Troubleshooting

- **Game Doesn't Start:** Ensure all dependencies are installed correctly. Reinstall dependencies if necessary.
- **Performance Issues:** Close other resource-intensive applications to improve game performance.

---

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 📞 Support

For further assistance or to report bugs, please contact our support team or open an issue on the project's GitHub repository.

Enjoy your adventure in the Tower of the Sorcerer Roguelike Game!

```