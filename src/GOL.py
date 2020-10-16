import numpy as np

class GameOfLife:

    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.grid = np.array([[0 for x in range(grid_width)] for y in range(grid_height)])
        self.pct_of_living = 0
        self.count = 0

    # Initializes the grid with random cells
    def initialize_grid(self):
       self.grid = np.random.choice([0, 1], (self.grid_height, self.grid_width), [.8, .2])

    def empty_grid(self):
       self.grid = np.zeros((self.grid_height, self.grid_width))
       
    def update_grid(self):
        next_grid = np.array([[0 for x in range(self.grid_width)] for y in range(self.grid_height)])
        alive = 0
        count = 0

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                count += 1
                if self.grid[i][j] == 1:
                    if self.neighbours(i, j) < 2 or self.neighbours(i, j) > 3:
                        next_grid[i][j] = 0
                    else:
                        next_grid[i][j] = 1
                        alive += 1
                else:
                    if self.neighbours(i, j) == 3:
                        next_grid[i][j] = 1
                        alive += 1
                    else:
                        next_grid[i][j] = 0

        self.count = alive
        self.pct_of_living = alive / count
        self.grid = next_grid

    # Count the number of neighbours
    def neighbours(self, row, col):
        neighbours = 0

        neighbour_cells = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                           (row, col - 1),                     (row, col + 1),
                           (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]

        for row, col in neighbour_cells:
            if row >= 0 and col >= 0:
                try:
                    neighbours += self.grid[row][col]
                except IndexError:
                    pass
                    
        return neighbours
