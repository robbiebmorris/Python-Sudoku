# Sudoku Game

This project is a Sudoku game that allows you to play and solve Sudoku puzzles. It provides a graphical user interface (GUI) using the Tkinter library and supports importing and exporting puzzles from/to a CSV file.

## Getting Started

To get started with this project, follow the instructions below.

### Prerequisites

Make sure you have the following dependencies installed:

- Python 3.x
- Tkinter (usually included with Python)

### Installation

1. Clone the repository:

   ```shell
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```shell
   cd sudoku-game
   ```

### Usage

To play the Sudoku game, follow these steps:

1. Import the necessary modules:

   ```python
   import csv
   import tkinter as tk
   ```

2. Create an instance of the `Sudoku` class:

   ```python
   sudoku = Sudoku(file_location="data.csv", data=board_data)
   ```

   - `file_location` (optional): The path to the CSV file containing a Sudoku puzzle. If not specified, a default puzzle will be used.
   - `data` (optional): A 2D array of tuples representing the Sudoku puzzle. Each tuple consists of two values: the given value and the correct value. If not specified, the puzzle will be imported from the CSV file.

3. Run the Sudoku game by calling the `main()` function:

   ```python
   sudoku.main()
   ```

   This will open a GUI window displaying the Sudoku board.

4. Interact with the Sudoku game by entering numbers into the empty spaces on the board.

   - The given values in the puzzle are displayed in gray and cannot be modified.
   - Press the "Done" button to check your solution.
   - Incorrect spaces will turn red, and correct spaces will turn green.
   - The number of incorrect spaces will be displayed in a pop-up window.

5. You can export the current Sudoku game to a CSV file by clicking the "Export" button.

6. If you want to import a new Sudoku game from a CSV file, click the "Import" button and select the file.

7. To exit the game, click the "Exit" button or close the window.

## Example

Here's an example of how to use the Sudoku game:

```python
# Import the necessary modules
import csv
import tkinter as tk

#...

def main():
    sudoku = Sudoku(file_location="data.csv")
    sudoku.main()


if __name__ == "__main__":
    main()
```
