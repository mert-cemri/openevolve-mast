# Wordle Game User Manual

Welcome to the Wordle Game! This manual will guide you through the installation and usage of the Wordle game, a simple command-line game implemented in Python. The game challenges you to guess a daily 5-letter word within 6 attempts, providing feedback on each guess.

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [How to Play](#how-to-play)
4. [Game Functions](#game-functions)

## Introduction

The Wordle Game is a text-based game that you can play directly from your Linux Terminal. The objective is to guess a randomly selected 5-letter word within 6 attempts. After each guess, you will receive feedback indicating which letters are correct and in the correct position (green), which letters are correct but in the wrong position (yellow), and which letters are incorrect (grey).

## Installation

### Prerequisites

- Python 3.x must be installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Steps

1. **Clone the Repository:**
   Open your terminal and run the following command to clone the repository:
   ```bash
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**
   ```bash
   cd <repository-directory>
   ```
   Replace `<repository-directory>` with the name of the cloned directory.

3. **Install Dependencies:**
   The game does not require any external dependencies, so you can skip this step. However, ensure that your Python environment is set up correctly.

## How to Play

1. **Start the Game:**
   Run the following command in your terminal to start the game:
   ```bash
   python main.py
   ```

2. **Game Instructions:**
   - You will be prompted to enter a 5-letter word as your guess.
   - After each guess, feedback will be displayed:
     - **Green**: Correct letter in the correct position.
     - **Yellow**: Correct letter in the wrong position.
     - **Grey**: Incorrect letter.
   - You have a total of 6 attempts to guess the word correctly.

3. **Winning the Game:**
   - If you guess the word correctly within 6 attempts, a congratulatory message will be displayed.

4. **Losing the Game:**
   - If you fail to guess the word within 6 attempts, the correct word will be revealed.

## Game Functions

- **get_daily_word()**: Selects a random 5-letter word from a predefined list to be the word of the day.
- **get_user_guess()**: Prompts the user to enter a valid 5-letter word as their guess.
- **evaluate_guess(guess, daily_word)**: Compares the user's guess with the daily word and provides feedback on each letter.
- **display_feedback(guess, feedback)**: Displays the feedback for each guess using color-coded text in the terminal.
- **play_game()**: Manages the game flow, including attempts and win/lose conditions.
- **main()**: The main function that initiates the game loop.

Enjoy playing the Wordle Game and challenge yourself to guess the word of the day!