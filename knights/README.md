# Knights

## Overview
The Knights project is a Python-based program that solves logical puzzles involving knights and knaves. Knights always tell the truth, while knaves always lie. The program uses propositional logic to determine the truthfulness of statements made by characters in the puzzle.

This project is part of the CS50's Introduction to Artificial Intelligence with Python course and demonstrates the use of logical reasoning and inference.

## Project Structure
- `logic.py`: Contains the logic and helper functions for solving the puzzles.
- `puzzle.py`: Defines the puzzles and uses the logic to solve them.

## Setup
1. Clone the repository to your local machine.
2. Ensure you have Python installed (version 3.6 or higher).
3. Install any required dependencies (if applicable).

## Usage
1. Navigate to the `knights` directory in your terminal.
2. Run the program using the following command:
   ```
   python puzzle.py
   ```
3. The program will output the solution to the defined puzzles, indicating which characters are knights and which are knaves.

## Example
For a puzzle where:
- A says: "I am a knight."
- B says: "A is a knave."

The program might output:
```
A is a knave.
B is a knight.
```

## Notes
- The program uses propositional logic to model the statements and solve the puzzles.
- You can define additional puzzles in `puzzle.py` by following the existing structure.

## License
This project is part of the CS50's Introduction to Artificial Intelligence with Python course and is for educational purposes.