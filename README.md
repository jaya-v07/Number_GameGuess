# Number Guessing Game 🎯

A simple and interactive Python console game where players try to guess a randomly generated number between 1 and 100.

## 📝 Description

This is a classic number guessing game implemented in Python. The computer randomly selects a number between 1 and 100, and the player has to guess it with the help of hints. The game provides feedback after each guess, telling the player whether their guess is "Too High," "Too Low," or if they're "Very Close" to the target number.

## 🎮 How to Play

1. Run the program
2. The computer will randomly choose a number between 1 and 100
3. Enter your guess when prompted
4. Receive hints:
   - **"Too High!"** - Your guess is higher than the target number
   - **"Too Low!"** - Your guess is lower than the target number
   - **"You are very close!"** - Your guess is within 1 of the target number
5. Keep guessing until you find the correct number
6. The game will display your total number of attempts when you win
7. Type 'exit' or 'quit' anytime to end the game

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/number-guessing-game.git
```

2. Navigate to the project directory:
```bash
cd number-guessing-game
```

3. Run the game:
```bash
python guess_game.py
```

## 💡 Features

- **Random Number Generation**: Each game uses a different target number
- **Input Validation**: Handles invalid inputs gracefully
- **Range Checking**: Ensures guesses are between 1 and 100
- **Proximity Hints**: Special "very close" hint when within 1 of the target
- **Attempt Tracking**: Counts and displays the number of guesses
- **Exit Option**: Players can quit anytime by typing 'exit' or 'quit'
- **Error Handling**: Robust handling of non-integer inputs

## 🎯 Example Gameplay

```
----GUESS THE NUMBER GAME----
You have to guess a number between 1 and 100.
After each guess, you'll receive hints like 'Too High' or 'Too Low'.
Type 'exit' anytime to quit the game.
The game ends when you guess correctly, and it will display the number of attempts.

Enter your guess (between 1 and 100 or type 'exit' to quit): 50
Too High!
Enter your guess (between 1 and 100 or type 'exit' to quit): 25
Too Low!
Enter your guess (between 1 and 100 or type 'exit' to quit): 37
You are very close!
Enter your guess (between 1 and 100 or type 'exit' to quit): 38
Congratulations! You've guessed the number 38 in 4 attempts.
```

## 🔧 Code Structure

The game is organized using functions for better code maintainability:

- **`guess_game()`**: Main game logic function
- **Error Handling**: Try-catch blocks for input validation
- **Input Validation**: Checks for valid integer inputs within range
- **Game Loop**: Continues until correct guess or user exits


### Potential Improvements

- Add difficulty levels (different number ranges)
- Implement a high score system
- Add a graphical user interface
- Include sound effects
- Add multiplayer functionality

## 📋 Requirements

- Python 3.x
- No external dependencies required

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---
