from sudoku import Sudoku
import turtle


def read_grid(file_path):
    with open(file_path, "r") as file:
        grid = []
        for line in file:
            line = line.strip()
            if line and line[0] != "#":
                row = [cell for cell in line]
                grid.append(row)
        return grid


def text(message, x, y, size, align):
    FONT = ("Arial", size, "normal")
    pen.penup()
    pen.goto(x, y)
    pen.write(message, align=align, font=FONT)


def drawGrid(grid):
    pen.clear()
    intDim = 35
    for row in range(0, 10):
        if (row % 3) == 0:
            pen.pensize(3)
        else:
            pen.pensize(1)
        pen.penup()
        pen.goto(topLeft_x, topLeft_y - row * intDim)
        pen.pendown()
        pen.goto(topLeft_x + 9 * intDim, topLeft_y - row * intDim)
    for col in range(0, 10):
        if (col % 3) == 0:
            pen.pensize(3)
        else:
            pen.pensize(1)
        pen.penup()
        pen.goto(topLeft_x + col * intDim, topLeft_y)
        pen.pendown()
        pen.goto(topLeft_x + col * intDim, topLeft_y - 9 * intDim)

    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] != "0":
                text(
                    grid[row][col],
                    topLeft_x + col * intDim + 9,
                    topLeft_y - row * intDim - intDim + 8,
                    18,
                    "left",
                )


if __name__ == "__main__":
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("#000000")
    pen.hideturtle()
    topLeft_x = -150
    topLeft_y = 150

    text("loading grid", 0, 0, 18, "center")

    # file_path = "dummy_grids/grid1.txt"
    # sud = Sudoku(grid=read_grid(file_path))

    sud = Sudoku(9, 3)
    sud = sud.genRandomGrid()

    drawGrid(sud.grid)

    turtle.done()
