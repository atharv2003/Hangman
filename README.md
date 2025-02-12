# Hangman Game

## Overview
This is a simple text-based Hangman game implemented in Python. The game randomly selects a word from a predefined list, and the player must guess the word letter by letter before running out of lives.

## Features
- Random word selection from a predefined list.
- ASCII art representation of the hangman stages.
- Tracks previously guessed letters to prevent duplicate guesses.
- User-friendly interaction with clear feedback on guesses.
- Win or lose message displayed at the end.

## Files
- `main.py`: The main script that runs the game logic.
- `hangman_words.py`: Contains a list of possible words for the game.
- `hangman_art.py`: Contains ASCII art for the hangman stages and the game logo.

## How to Play
1. Run `main.py` using Python:
   ```bash
   python main.py
   ```
2. The game will display the Hangman logo and select a random word.
3. The player will be prompted to guess a letter.
4. If the letter is in the word, it will be revealed in its correct positions.
5. If the letter is incorrect, the player loses a life and the hangman drawing progresses.
6. The game continues until:
   - The player correctly guesses all letters (win).
   - The player runs out of lives (lose).

## Example Gameplay
```
Guess a letter: a
_ _ a _ _

Guess a letter: z
Wrong guess! 'z' is not in word
You have 5 lives left.
```

## Installation
No external libraries are required. Ensure you have Python installed, then clone the repository and run the script:
```bash
git clone https://github.com/your-username/hangman-game.git
cd hangman-game
python main.py
```

## Contributions
Feel free to submit a pull request if you'd like to improve the game!

## License
This project is open-source and available under the MIT License.

