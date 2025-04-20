# Tic-Tac-Toe

## Overview
The Tic-Tac-Toe project is a Python-based implementation of the classic Tic-Tac-Toe game, enhanced with an AI agent. The game allows players to compete against an AI opponent that uses the Minimax algorithm to make optimal moves.

This project is part of the CS50's Introduction to Artificial Intelligence with Python course and demonstrates the use of game theory and AI decision-making.

## Project Structure
- `tictactoe.py`: Contains the game logic and the AI implementation using the Minimax algorithm.
- `runner.py`: The main script to run the game with a graphical interface using Pygame.
- `requirements.txt`: Lists the dependencies required to run the project.
- `assets/`: Contains fonts used in the graphical interface.
  - `fonts/OpenSans-Regular.ttf`: Font used for text rendering.

## Setup
1. Clone the repository to your local machine.
2. Ensure you have Python installed (version 3.6 or higher).
3. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
4. Ensure Pygame is installed for the graphical interface.

## Usage
1. Navigate to the `tictactoe` directory in your terminal.
2. Run the game using the following command:
   ```
   python runner.py
   ```
3. Follow the on-screen instructions to play the game.

## Game Instructions
- Choose to play as X or O at the start of the game.
- Click on a cell to make your move.
- The AI will make its move after yours.
- The game ends when there is a winner or the board is full.

## Example
When you start the game, you will see a 3x3 grid representing the Tic-Tac-Toe board. The goal is to align three of your symbols (X or O) in a row, column, or diagonal before the AI does.

## Notes
- The AI uses the Minimax algorithm to make optimal moves.
- The game board and logic are implemented in `tictactoe.py`, while the graphical interface is handled in `runner.py`.

## License
This project is part of the CS50's Introduction to Artificial Intelligence with Python course and is for educational purposes.