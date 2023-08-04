from sudoku import Sudoku


def read_grid(file_path):
    with open(file_path, "r") as file:
        grid = []
        for line in file:
            line = line.strip()
            if line and line[0] != "#":
                row = [cell for cell in line]
                grid.append(row)
        return grid


if __name__ == "__main__":
    file_path = "dummy_grids/grid1.txt"
    sud = Sudoku(grid=read_grid(file_path))
    print(sud.isLegalMove(9, 9))
