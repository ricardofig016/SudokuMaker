class Sudoku(object):
    def __init__(self, grid_size=9, square_size=3) -> None:
        self.grid_size = grid_size
        self.grid = [[0 for i in range(grid_size)] for i in range(grid_size)]
        self.square_size = square_size

    def isValid(self, board):
        squares = [[] for i in range(len(board) // 3)]
        for i in range(len(board)):
            row = []
            col = []
            for j in range(len(board[i])):
                if board[i][j] != 0:
                    row += board[i][j]
                if board[j][i] != 0:
                    col += board[j][i]
                if board[i][j] != 0:
                    squares[j // 3] += board[i][j]

            if (i + 1) % 3 == 0:
                for square in squares:
                    if len(set(square)) != len(square):
                        return False
                squares = [[] for i in range(len(board) // 3)]
            if len(set(row)) != len(row):
                return False
            if len(set(col)) != len(col):
                return False

        return True
