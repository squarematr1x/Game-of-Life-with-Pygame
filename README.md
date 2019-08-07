# Game-of-Life-with-Pygame

Creating a GUI with Pygame to demonstrate [John Conway's famous cellular automata](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). 

## Rules
* Any live cell with fewer than two live neighbours dies, as if by underpopulation.
* Any live cell with two or three live neighbours lives on to the next generation.
* Any live cell with more than three live neighbours dies, as if by overpopulation.
* Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## Features
* Initializing random game grid
* Selecting/deselecting living cells
* Pausing the game
* Displaying the number of living cells in the grid
* Displaying the percentage of living cells
* Changing the color of the cell according to the number of adjacent cells

### One possible state of the game:
![One possible state of the game](https://raw.githubusercontent.com/squarematr1x/Game-of-Life-with-Pygame/master/one_possible_state_of_game.png)
