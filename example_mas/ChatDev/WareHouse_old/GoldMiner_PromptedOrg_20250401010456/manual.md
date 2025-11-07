manual.md

```
# Gold Miner Game 🎮

Welcome to the Gold Miner Game, an exciting Python-based game where you control a claw to collect valuable objects like gold and diamonds while avoiding obstacles like rocks. The game challenges your timing and strategy skills, with increasing difficulty as you progress through levels.

---

## 🚀 Features

- **Dynamic Claw Movement:** Control a claw that moves horizontally back and forth, automatically grabbing objects within range.
- **Multiple Object Types:** Collect gold, diamonds, and avoid rocks. Each object has unique values and weights affecting your score and reel-in time.
- **Level Progression:** Complete levels by achieving a minimum gold value within a time limit. Each level increases in difficulty with more obstacles and tighter time constraints.
- **Real-time Updates:** Clear and informative updates on claw position, objects collected, and current scores.

---

## 🛠️ Installation

### Prerequisites

- Python 3.x installed on your system. You can download Python from [here](https://www.python.org/downloads/).

### Dependencies

This game requires no external dependencies. However, ensure your Python environment is correctly set up.

You can verify your Python installation by running:

```bash
python --version
```

---

## 📂 Project Structure

```
GoldMinerGame/
├── claw.py
├── game.py
├── gameobject.py
├── level.py
├── main.py
└── requirements.txt
```

---

## ▶️ How to Play

### Step 1: Run the Game

Navigate to the project directory and execute the following command in your terminal:

```bash
python main.py
```

### Step 2: Gameplay Mechanics

- The claw moves automatically from left to right and vice versa.
- When the claw is close enough to an object, it automatically grabs and reels it in.
- Each object has:
  - **Value:** Amount of gold earned when collected.
  - **Weight:** Determines how long it takes to reel in.
- The level ends when:
  - You collect enough gold to meet the level's requirement, or
  - The time limit expires.

### Step 3: Level Progression

- Successfully meeting the gold requirement advances you to the next level.
- Each new level introduces:
  - More obstacles (rocks).
  - Higher gold requirements.
  - Shorter time limits.

---

## 🎯 Game Objective

- Collect as much gold and diamonds as possible.
- Avoid grabbing rocks, as they waste valuable time and yield no gold.
- Progress through levels by meeting or exceeding the gold requirement within the given time limit.

---

## 🕹️ Controls and Gameplay Tips

- **Automatic Movement:** The claw moves automatically; your main task is timing and strategy.
- **Timing is Key:** Pay attention to the claw's position and the objects' locations to maximize your gold collection.
- **Prioritize Valuable Objects:** Diamonds and larger gold nuggets are more valuable but may take longer to reel in. Balance your strategy accordingly.

---

## 📋 Example Gameplay Output

```
Welcome to Gold Miner!

Starting Level 1
Objects generated for this level:
Gold at position 3, value: 20, weight: 1.50
Rock at position 7, value: 3, weight: 3.20
Diamond at position 5, value: 50, weight: 0.80
...

Claw position: 2
No object within grabbing range.
Claw position: 3
Automatically grabbing Gold (value: 20, weight: 1.50)
Reeling in Gold...
Collected Gold worth 20 gold. Level gold: 20, Total gold: 20
...
Level 1 completed!

Starting Level 2
...
```

---

## 🛎️ Support and Feedback

Encountered an issue or have suggestions? Please reach out to our support team or submit your feedback. We continually strive to improve your gaming experience.

Enjoy mining gold and becoming the ultimate Gold Miner! 🥇⛏️
```