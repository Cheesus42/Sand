
rows = 10
cols = 10
grid = [[0 for i in range(cols)] for j in range(rows)]

grid[5][0] = 1
grid[0][0] = 1
grid[5][5] = 1
grid[5][3] = 1
for row in grid:
    print(row)

#grid[row][col]
w = 0
while w < 11:
    for i in range(rows - 1):
        for j in range(cols):
            if grid[i][j] == 1 and grid[i+1][j] == 0:
                grid[i][j] = 0
                grid[i+1][j] = 1
    w += 1

print("\n")
for row in grid:
    print(row)
