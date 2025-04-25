# Crossword

## Overview
The Crossword project is a Python-based program that generates and solves crossword puzzles. It uses constraint satisfaction problems (CSP) to fill in the crossword grid with valid words from a given word list.

This project is part of the CS50's Introduction to Artificial Intelligence with Python course and demonstrates the use of CSPs and backtracking algorithms.

## Project Structure
- `crossword.py`: Contains the logic for representing and solving crossword puzzles.
- `generate.py`: The main script to generate and solve crossword puzzles.
- `data/`: Contains word lists and crossword structures.
  - `words0.txt`, `words1.txt`, `words2.txt`: Word lists used for filling the crossword.
  - `structure0.txt`, `structure1.txt`, `structure2.txt`: Predefined crossword structures.
- `assets/`: Contains fonts used in the graphical interface.
  - `fonts/OpenSans-Regular.ttf`: Font used for text rendering.

## Setup
1. Clone the repository to your local machine.
2. Ensure you have Python installed (version 3.6 or higher).
3. Install any required dependencies (if applicable).

## Usage
1. Navigate to the `crossword` directory in your terminal.
2. Run the program using the following command:
   ```
   python generate.py data/structure0.txt data/words0.txt output.png
   ```
3. Follow the prompts to select a crossword structure and word list. The program will generate and solve the crossword puzzle.

## Example
When you run the program, you will be prompted to select a crossword structure and word list. The program will then attempt to fill the crossword grid with valid words, displaying the solution if one is found.

## Notes
- The program uses CSPs and backtracking to solve the crossword puzzles.
- You can add your own word lists and structures in the `data/` directory to create custom puzzles.

## License
This project is part of the CS50's Introduction to Artificial Intelligence with Python course and is for educational purposes.