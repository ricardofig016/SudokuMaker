class Sudoku(object):
    def __init__(self, grid_size=9, square_size=3, grid=[]):
        self.grid_size = grid_size
        if grid != []:
            assert len(grid) == len(grid[0]), "Grid must be a Square"
            self.grid = grid
            self.grid_size = len(grid)
        else:
            self.grid = [["0" for i in range(grid_size)] for i in range(grid_size)]
            self.grid_size = grid_size
        assert (
            self.grid_size % square_size == 0
        ), "Squares of this size do not fit the grid"
        self.square_size = square_size

    def isValid(self):
        squares = [[] for i in range(self.grid_size // self.square_size)]
        for i in range(self.grid_size):
            row = []
            col = []
            for j in range(self.grid_size):
                if self.grid[i][j] != "0":
                    row += self.grid[i][j]
                if self.grid[j][i] != "0":
                    col += self.grid[j][i]
                if self.grid[i][j] != "0":
                    squares[j // self.square_size] += self.grid[i][j]

            if (i + 1) % self.square_size == 0:
                for square in squares:
                    if len(set(square)) != len(square):
                        return False
                squares = [[] for i in range(self.grid_size // self.square_size)]
            if len(set(row)) != len(row):
                return False
            if len(set(col)) != len(col):
                return False

        return True

    def isCompleted(self):
        for row in self.grid:
            if "0" in row:
                return False
        return True
