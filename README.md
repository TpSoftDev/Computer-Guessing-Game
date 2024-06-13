# Computer Guessing Game

## Overview
This Python script implements a computer guessing game where the user thinks of a number within a specified range, and the computer tries to guess it. The user provides feedback to the computer after each guess, indicating whether the guess is too high, too low, or correct. The computer adjusts its guesses based on the user's feedback until it correctly guesses the number.

## How to Play
1. Run the Python script `computer_guess.py`.
2. Think of a number within the specified range.
3. Respond to the computer's guesses with 'H' (too high), 'L' (too low), or 'C' (correct).
4. Based on your feedback, the computer will adjust its guesses until it correctly guesses your number.
5. Once the computer guesses your number correctly, the game ends.

## Programming Techniques
- **Random Number Generation**: The script uses the `random.randint()` function to generate random guesses within the specified range.
- **User Input**: It utilizes the `input()` function to receive feedback from the user.
- **Looping**: A `while` loop is employed to repeatedly guess until the correct number is guessed.
- **Conditional Statements**: `if-elif-else` statements are used to adjust the guessing range based on the user's feedback.
- **Function Definition**: The functionality of the game is encapsulated within a function `computer_guess_number()` for modularity and reusability.
- **Documentation**: The script includes comments to explain the purpose of each section of code and adheres to Python docstring standards for documenting the function.

## Example
```
Is 7 too high (H), too low (L), or correct (C)? h
Is 4 too high (H), too low (L), or correct (C)? l
Is 5 too high (H), too low (L), or correct (C)? c
Yay! The computer guessed your number 5 correctly!
```
