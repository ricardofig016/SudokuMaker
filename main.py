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
    # grid_file_nb = input("grid file number: ")
    # file_path = "dummy_grids/grid" + grid_file_nb + ".txt"
    # sud = Sudoku(grid=read_grid(file_path))
    sud = Sudoku(9, 3)
    print(sud.genRandomGrid().toString())
