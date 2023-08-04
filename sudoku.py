class Sudoku(object):
    def __init__(self, grid_size=9, square_size=3, grid=[]):
        self.grid_size = grid_size
        if grid != []:
            for row in grid:
                assert len(grid) == len(row), "Grid must be a Square"
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

    def isLegalMove(self, cell_x, cell_y):
        cell = (cell_x - 1, cell_y - 1)
        cell_square = (cell[0] // self.square_size, cell[1] // self.square_size)
        row = []
        col = []
        square = []
        for i in range(self.grid_size):
            if self.grid[cell[0]][i] != "0":
                row.append(self.grid[cell[0]][i])
            if self.grid[i][cell[1]] != "0":
                col.append(self.grid[i][cell[1]])
            if i // self.square_size == cell_square[0]:
                for j in range(self.grid_size):
                    if (
                        j // self.square_size == cell_square[1]
                        and self.grid[i][j] != "0"
                    ):
                        square.append(self.grid[i][j])
        print(row, col, square)
        if (
            len(row) == len(set(row))
            and len(col) == len(set(col))
            and len(square) == len(set(square))
        ):
            return True
        return False

    def isCompleted(self):
        for row in self.grid:
            if "0" in row:
                return False
        return True

    def solve(self):
        ptr = (0, 0)
        while ptr != (self.grid_size + 1, 0):
            pass

        return

    def toString(self):
        s = ""
        for i in range(self.grid_size):
            s += "["
            for j in range(self.grid_size):
                s += self.grid[i][j]
                if j < self.grid_size - 1:
                    s += ","
            s += "]"
            if i < self.grid_size - 1:
                s += "\n"
        return s
