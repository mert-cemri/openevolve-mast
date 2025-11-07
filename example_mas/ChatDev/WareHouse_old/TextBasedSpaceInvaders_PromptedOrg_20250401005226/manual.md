# Space Invaders Game Manual

Welcome to the simplified Space Invaders game! This manual will guide you through installing, setting up, and playing the game. Enjoy defending the galaxy from alien invaders!

---

## 🚀 Introduction

Space Invaders is a simplified version of the classic arcade game. You control a spaceship at the bottom of the screen, moving horizontally to dodge and shoot descending alien rows. Your goal is to destroy all aliens before they reach the bottom of the screen. You have a limited number of lives, and your score increases as you eliminate aliens.

---

## 🎮 Main Features

- **Player Ship Control:** Move horizontally using the left and right arrow keys.
- **Shooting:** Fire bullets using the spacebar to destroy aliens.
- **Multiple Alien Rows:** Face multiple rows of descending aliens.
- **Limited Lives:** You start with a limited number of lives. The game ends if you lose all lives.
- **Score Tracking:** Your score increases with each alien you destroy. Try to achieve the highest score possible!

---

## 🛠️ Installation

Follow these simple steps to install and run the game on your computer.

### Step 1: Clone or Download the Repository

Clone the repository using git:

```bash
git clone <repository-url>
cd <repository-directory>
```

Alternatively, download and extract the ZIP file containing the game files.

### Step 2: Set Up Python Environment

Make sure you have Python installed (version 3.7 or higher recommended). You can download Python from [python.org](https://www.python.org/downloads/).

Verify your Python installation by running:

```bash
python --version
```

### Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

This will install the necessary `pygame` library.

---

## ▶️ How to Play

### Starting the Game

Run the game by executing the following command in your terminal:

```bash
python main.py
```

### Controls

- **Left Arrow Key (←):** Move the spaceship left.
- **Right Arrow Key (→):** Move the spaceship right.
- **Spacebar:** Fire bullets to destroy aliens.

### Gameplay

- Your spaceship is positioned at the bottom of the screen. Move left and right to aim at aliens.
- Fire bullets to destroy aliens before they reach the bottom.
- You can fire a limited number of bullets at a time (default is 3).
- Each alien destroyed increases your score.
- If an alien reaches the bottom, you lose one life.
- The game ends when you lose all your lives or successfully destroy all aliens.

---

## 🏆 Scoring and Lives

- **Score:** Displayed at the top-left corner of the screen. Each alien destroyed adds points to your score.
- **Lives:** Displayed below the score. You start with a limited number of lives (default is 3). Losing all lives results in a game over.

---

## ❌ Exiting the Game

To exit the game at any time, simply close the game window or press the close button on the window.

---

## 📌 Troubleshooting

- **Game doesn't start:** Ensure Python and pygame are correctly installed. Check your Python version and dependencies.
- **Controls not responding:** Make sure the game window is active and selected.

---

## 📞 Support

If you encounter any issues or have suggestions, please contact our support team or open an issue in the repository.

---

Enjoy playing Space Invaders and defend the galaxy! 🌌🚀