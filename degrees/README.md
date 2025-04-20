# Degrees

## Overview
The Degrees project is a Python-based program that determines the shortest path between two actors or actresses through their shared movie roles. This is commonly referred to as the "Six Degrees of Kevin Bacon" problem, where the goal is to find the shortest connection between two individuals in the film industry.

The program uses a breadth-first search algorithm to find the shortest path between two people in a dataset of movies and actors.

## Project Structure
- `degrees.py`: The main script that runs the program.
- `util.py`: Contains utility functions for the project.
- `large/` and `small/`: Directories containing datasets of movies, people, and stars in CSV format.
  - `movies.csv`: Contains movie data.
  - `people.csv`: Contains actor/actress data.
  - `stars.csv`: Contains relationships between movies and actors/actresses.

## Setup
1. Clone the repository to your local machine.
2. Ensure you have Python installed (version 3.6 or higher).
3. Install any required dependencies (if applicable).

## Usage
1. Navigate to the `degrees` directory in your terminal.
2. Run the program using the following command:
   ```
   python degrees.py large
   ```
   or
   ```
   python degrees.py small
   ```
3. Follow the prompts to input the names of two actors/actresses. The program will output the shortest path between them, if one exists.

## Example
If you input:
- Person 1: Kevin Bacon
- Person 2: Tom Hanks

The program might output:
```
1: Kevin Bacon and Tom Hanks starred in Apollo 13
```

## Notes
- The `large/` dataset contains a comprehensive list of movies and actors, while the `small/` dataset is a smaller subset for testing purposes.
- The program uses a breadth-first search algorithm to ensure the shortest path is found.

## License
This project is part of the CS50's Introduction to Artificial Intelligence with Python course and is for educational purposes.