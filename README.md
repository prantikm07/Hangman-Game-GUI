# Hangman Game (Tkinter GUI)

A fun, interactive Hangman game built in Python with a graphical interface using Tkinter. In this game, players guess letters in a hidden word within a limited number of lives.

## Game Description

The Hangman game challenges you to guess a randomly selected word from a given list. Each incorrect guess reduces your remaining lives and progresses the drawing of a hangman figure. The game ends if:
1. You guess the word correctly and win.
2. You run out of lives and lose.

## How to Play

1. Run the program to launch the GUI.
2. The game window shows underscores representing each letter of the hidden word.
3. Enter one letter at a time in the input box and click "Guess a letter."
   - Correct guesses reveal the letter's position(s) in the word.
   - Incorrect guesses reduce your lives and progress the hangman drawing.
4. Continue guessing until either:
   - The word is fully revealed, and you win.
   - All lives are lost, resulting in a game over.

## Features

- **Random Word Selection:** The word is randomly chosen from a list of fruits.
- **Lives Tracking:** The game displays remaining lives with visual feedback.
- **Hangman Drawing Progression:** A hangman figure progresses with each incorrect guess.
- **Input Validation:** Only single, alphabetical letters are allowed.

## Game Stages

Each wrong guess progresses the hangman drawing in stages:
1. Starting with a blank gallows.
2. Incremental drawing as lives are lost.
3. Complete hangman figure if all lives are exhausted.

## Requirements

- **Python 3.x**
- **Tkinter library**

This game can be run in any Python IDE or from the command line.

## How to Run

1. Ensure Python 3.x and Tkinter are installed.
2. Save the code in a file named `hangman_gui.py`.
3. Run the game with the command:

   ```bash
   python hangmanui.py
   ```

## Future Enhancements

Planned additions:
- Additional word lists for various difficulty levels.
- Scoring and leaderboard feature.
- More visual effects and improved graphics.

## License

This project is open-source and available for modification and distribution.
