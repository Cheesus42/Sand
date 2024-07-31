import InstanciateWindow as win
from tkinter import *
import time

window = Tk()
icon = PhotoImage(file='Sand_JE5_BE3.png')
window.title("Falling Sand")
window.iconphoto(True, icon)

#grid[row][col]
rows = 10
cols = 10
grid = [[0 for i in range(cols)] for j in range(rows)]


grid[5][0] = 1
grid[6][0] = 1
grid[0][0] = 1
grid[5][5] = 1
grid[5][3] = 1

new_grid = [row[:] for row in grid]
def display(grid):
    for row in grid:
        print(row)
    print("\n")


def move_sand(check_grid, new_grid):
    for i in range(rows - 1):
        for j in range(cols):
            if check_grid[i][j] == 1 and new_grid[i + 1][j] == 0:
                check_grid[i][j] = 0
                new_grid[i][j] = 0
                new_grid[i + 1][j] = 1
    check_grid = [row[:] for row in new_grid]
    win.display_grid(check_grid, window,  8, 4)
    window.after(500, lambda: move_sand(check_grid, new_grid))


move_sand(grid, new_grid)

window.mainloop()



