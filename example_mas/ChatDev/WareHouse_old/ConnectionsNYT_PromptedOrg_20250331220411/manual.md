manual.md

````markdown
# Puzzle Game: Word Grouping Challenge 🎲

Welcome to the Puzzle Game, an engaging and challenging word puzzle designed to test your categorization skills and logical thinking. Every day, a new puzzle awaits you, offering fresh words and categories to explore. Can you group all 16 words correctly before making 4 mistakes?

---

## 🚀 Main Features

- **Daily Puzzle Generation:** A unique puzzle is generated every day, ensuring fresh and exciting gameplay.
- **4x4 Word Grid:** Words are displayed in a clear 4x4 grid format for easy selection.
- **Hidden Categories:** Group words into four hidden categories, each containing exactly four words.
- **Color-Coded Difficulty:** Categories are revealed with difficulty levels indicated by colors:
  - 🟨 **Yellow** (Easy)
  - 🟩 **Green** (Medium)
  - 🟦 **Blue** (Hard)
  - 🟪 **Purple** (Very Hard)
- **Shuffle Functionality:** Shuffle the grid anytime to view words from a new perspective.
- **Immediate Feedback:** Receive instant feedback on your guesses, helping you strategize better.
- **Mistake Limit:** You have a maximum of 4 mistakes allowed per puzzle—use them wisely!

---

## 🛠️ Installation Guide

Follow these simple steps to set up the Puzzle Game on your local machine:

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd puzzle-game
```

*(Replace `<repository-url>` with the actual URL of the repository.)*

### Step 2: Set Up Python Environment

Ensure Python (version 3.7 or higher) is installed on your system. You can verify your Python version by running:

```bash
python --version
```

### Step 3: Install Dependencies

Install the required Python dependencies using pip:

```bash
pip install -r requirements.txt
```

*(This will install the `colorama` library required for colored terminal output.)*

---

## 🎮 How to Play

### Starting the Game

Run the game by executing the following command in your terminal:

```bash
python main.py
```

### Gameplay Instructions

1. **View the Puzzle Grid:**  
   The game displays a 4x4 grid of words. Your goal is to identify four groups of four words each, based on hidden categories.

2. **Selecting Words:**  
   Type exactly four words separated by commas to form a group. For example:

   ```
   Apple, Banana, Orange, Grape
   ```

3. **Shuffle Words:**  
   If you're stuck, you can shuffle the words to see them in a new arrangement. Simply type:

   ```
   shuffle
   ```

4. **Feedback and Mistakes:**  
   - **Correct Guess:** The words are removed from the grid, and the category along with its difficulty level is revealed in color.
   - **Incorrect Guess:** You receive immediate feedback, and your mistake count increases by one. Remember, you can only make 4 mistakes!

5. **Winning the Game:**  
   Successfully group all words into their correct categories before reaching 4 mistakes to win the game.

6. **Game Over:**  
   If you reach 4 mistakes, the game ends, and you'll have to wait until tomorrow for a new puzzle.

---

## 📌 Example Gameplay

```
Current Puzzle Grid:
Apple          Dog            Red            Car            
Banana         Cat            Blue           Bike           
Orange         Rabbit         Green          Bus            
Grape          Hamster        Yellow         Train          

Mistakes: 0/4
Select 4 words separated by commas (or type 'shuffle' to shuffle): Apple, Banana, Orange, Grape
Correct! Category: Fruits (Difficulty: Yellow)

Current Puzzle Grid:
Dog            Red            Car            Cat            
Blue           Bike           Rabbit         Green          
Bus            Hamster        Yellow         Train          

Mistakes: 0/4
Select 4 words separated by commas (or type 'shuffle' to shuffle): Dog, Cat, Rabbit, Hamster
Correct! Category: Pets (Difficulty: Green)

...
```

---

## 🧩 Tips and Strategies

- **Look for Patterns:** Words may seem to fit multiple categories. Think carefully before making your selection.
- **Use Shuffle Wisely:** Shuffling can help you see new connections between words.
- **Manage Mistakes:** Be cautious with your guesses to avoid reaching the mistake limit too quickly.

---

## 📞 Support and Feedback

Encountered an issue or have suggestions? We'd love to hear from you! Please reach out to our support team or open an issue in our repository.

Happy puzzling! 🧠✨

````