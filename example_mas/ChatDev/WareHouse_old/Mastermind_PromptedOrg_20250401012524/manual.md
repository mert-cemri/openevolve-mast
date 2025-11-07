manual.md

```
# 🎲 Mastermind Game 🎲

Welcome to the Mastermind Game! This classic code-breaking game challenges your logic and deduction skills. Can you crack the hidden code?

---

## 📖 Overview

Mastermind is a classic puzzle game where the computer selects a hidden sequence of digits, and your goal is to guess this sequence within a limited number of attempts. After each guess, you'll receive feedback indicating:

- ✅ **Exact Matches**: Number of digits that are correct and in the correct position.
- 🔄 **Partial Matches**: Number of digits that are correct but in the wrong position.

Use this feedback to refine your guesses and crack the code!

---

## 🚀 Features

- Randomly generated hidden code for each new game.
- Customizable code length, digit range, and number of attempts.
- Clear feedback after each guess to guide your next move.
- User-friendly interface with clear win/lose outcomes.

---

## 🛠️ Installation

### Prerequisites

- Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Dependencies

This project does not require any external dependencies. However, ensure your Python environment is properly set up.

You can verify your Python installation by running:

```bash
python --version
```

---

## 🎮 How to Play

### Step 1: Download the Game Files

Ensure you have the following files in the same directory:

- `main.py`
- `game.py`

### Step 2: Run the Game

Open your terminal or command prompt, navigate to the directory containing the game files, and execute:

```bash
python main.py
```

### Step 3: Gameplay Instructions

- The computer will select a hidden sequence of digits (default length is 4 digits, each digit ranging from 0 to 5).
- You have a limited number of attempts (default is 10) to guess the correct sequence.
- Enter your guess as a sequence of digits (e.g., `1234`) and press Enter.
- After each guess, you'll receive feedback:
  - ✅ **Exact Matches**: Correct digit in the correct position.
  - 🔄 **Partial Matches**: Correct digit but in the wrong position.
- Continue guessing based on the feedback until you either crack the code or run out of attempts.

### Example Gameplay:

```
🎲 Welcome to Mastermind! 🎲

🔒 I have selected a hidden sequence of 4 digits (0-5).
You have 10 attempts to guess it correctly. Good luck! 🍀

Attempt 1/10: Enter your guess (e.g., 1234): 1234
✅ Exact matches (correct digit and position): 1
🔄 Partial matches (correct digit, wrong position): 2

Attempt 2/10: Enter your guess (e.g., 1234): 1243
✅ Exact matches (correct digit and position): 2
🔄 Partial matches (correct digit, wrong position): 1

...

🎉 Congratulations! You've cracked the code '1423' in 5 attempts! 🎉
```

---

## ⚙️ Customizing the Game (Optional)

You can customize the game parameters by editing the `main.py` file:

- `code_length`: Number of digits in the hidden code.
- `max_attempts`: Maximum number of guesses allowed.
- `digit_range`: Range of digits (0 to digit_range - 1).

Example:

```python
code_length = 6
max_attempts = 12
digit_range = 8  # Digits from 0 to 7
```

---

## 📌 Troubleshooting

- **Invalid Input**: Ensure your guess matches the required length and digit range. The game will prompt you if your input is invalid.
- **Python Errors**: Verify that both `main.py` and `game.py` are in the same directory and that you are running the command from the correct location.

---

## 📞 Support

If you encounter any issues or have suggestions for improvements, please contact our support team. We are here to help!

---

## 🎯 Enjoy the Game!

We hope you enjoy playing Mastermind and sharpening your logical thinking skills. Good luck cracking the code! 🍀🎲
```