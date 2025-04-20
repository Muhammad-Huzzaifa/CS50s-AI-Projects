# Minesweeper

## Overview
The Minesweeper project is a Python-based implementation of the classic Minesweeper game, enhanced with an AI agent. The game allows players to reveal cells, flag mines, and win by correctly identifying all mines on the board. The AI uses logical reasoning to make safe moves and infer the locations of mines.

This project is part of the CS50's Introduction to Artificial Intelligence with Python course and demonstrates the use of propositional logic and game AI.

## Project Structure
- `minesweeper.py`: Contains the Minesweeper game logic and the AI implementation.
- `runner.py`: The main script to run the game with a graphical interface using Pygame.
- `assets/`: Contains fonts and images used in the graphical interface.
  - `fonts/OpenSans-Regular.ttf`: Font used for text rendering.
  - `images/flag.png`: Image used to represent flagged cells.
  - `images/mine.png`: Image used to represent mines.
- `requirements.txt`: Lists the dependencies required to run the project.

## Setup
1. Clone the repository to your local machine.
2. Ensure you have Python installed (version 3.6 or higher).
3. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
4. Ensure Pygame is installed for the graphical interface.

## Usage
1. Navigate to the `minesweeper` directory in your terminal.
2. Run the game using the following command:
   ```
   python runner.py
   ```
3. Follow the on-screen instructions to play the game.

## Game Instructions
- Left-click on a cell to reveal it.
- Right-click on a cell to flag it as a mine.
- Use the "AI Move" button to let the AI make a move.
- Use the "Reset" button to restart the game.

## Example
When you start the game, you will see a grid representing the Minesweeper board. The goal is to reveal all safe cells without clicking on a mine. The AI can assist by making safe or random moves based on its knowledge.

## Notes
- The AI uses a knowledge base of logical sentences to infer safe moves and mine locations.
- The game board size and number of mines can be adjusted in `runner.py` by modifying the `HEIGHT`, `WIDTH`, and `MINES` variables.

## License
This project is part of the CS50's Introduction to Artificial Intelligence with Python course and is for educational purposes.