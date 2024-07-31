from tkinter import *

def get_color(value):
    color_map = {
        0: "black",
        1: "yellow"
    }
    return color_map.get(value, "cyan")


def display_grid(grid, parent, wid=2, heig=1):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            color = get_color(cell)
            label = Label(parent, text='', bg=color, borderwidth=0.5, relief="solid", width=wid, height=heig,
                          font=("Arial", 2))
            label.grid(row=i, column=j, padx=1, pady=1)


def display_grid_test(grid, updated, parent, wid=2, heig=1):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            color = get_color(cell)
            label = Label(parent, text='', bg=color, borderwidth=0.5, relief="solid", width=wid, height=heig,
                          font=("Arial", 2))
            label.grid(row=i, column=j, padx=1, pady=1)
