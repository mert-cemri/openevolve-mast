manual.md

```
# Trivia Quiz Application

A simple and interactive trivia quiz program designed to test your knowledge across various topics. This application supports both multiple-choice and short-answer questions, tracks your score, and optionally displays correct answers after completion.

---

## 🚀 Main Features

- **Multiple Question Types**: Supports both multiple-choice and short-answer questions.
- **Score Tracking**: Automatically tracks and displays your score at the end of the quiz.
- **Configurable Question Bank**: Easily customize and expand the question set.
- **Optional Answer Display**: Choose whether to view correct answers after completing the quiz.

---

## 📋 Installation

### Prerequisites

- Python 3.x installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

### Dependencies

This application does not require any external dependencies. However, ensure your Python environment is correctly set up.

```bash
# No external dependencies required for this project.
```

### Downloading the Application

Clone or download the application files (`main.py`, `quiz.py`, `question.py`) to your local machine.

```bash
git clone <repository-url>
cd trivia-quiz
```

---

## 🎮 How to Play

### Running the Quiz

Navigate to the directory containing the application files and run the following command in your terminal:

```bash
python main.py
```

### Gameplay Instructions

1. **Start the Quiz**: Upon running the application, you will see a welcome message.

2. **Answer Display Option**: You will be prompted to choose whether you want to see the correct answers after finishing the quiz. Type `yes` or `no` and press Enter.

```
Would you like to see correct answers after the quiz? (yes/no): yes
```

3. **Answering Questions**:
   - For **multiple-choice questions**, you can enter either the option number or the exact text of the option.
   - For **short-answer questions**, simply type your answer and press Enter.

Example of a multiple-choice question:

```
What is the capital of France?
1. Paris
2. London
3. Berlin
4. Madrid
Your answer: 1
```

Example of a short-answer question:

```
What is the chemical symbol for water?
Your answer: H2O
```

4. **Quiz Completion**: After answering all questions, your total score will be displayed.

```
Quiz Completed!
Your total score: 4/5
```

5. **Viewing Correct Answers** (optional): If you chose to view correct answers, they will be displayed along with your responses and correctness status.

```
Correct Answers:

1. What is the capital of France?
Your answer: Paris (Correct)
Correct answer: paris

2. Who wrote 'Romeo and Juliet'?
Your answer: Charles Dickens (Incorrect)
Correct answer: william shakespeare
...
```

---

## 🛠️ Customizing the Question Bank

You can easily customize the quiz by modifying the `load_questions()` function in the `quiz.py` file. Add, remove, or edit questions as needed.

### Example of Adding a New Question:

```python
Question(
    text="What is the largest ocean on Earth?",
    correct_answer="Pacific Ocean",
    options=["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"]
),
```

---

## 📞 Support

For any questions, issues, or feature requests, please contact our support team or open an issue in the project's repository.

Happy quizzing! 🎉
```