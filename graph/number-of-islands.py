def numberIslands(grid):

    def dfs(r, c):
        if grid[r][c] == "1":
            grid[r][c] = "0"

            if r - 1 >= 0:
                dfs(r-1, c)
            if r + 1 < len(grid):
                dfs(r+1, c)
            if c - 1 >= 0:
                dfs(r, c - 1)
            if c + 1 < len(grid[0]):
                dfs(r, c + 1)

    if grid == None and len(grid) == 0:
        return 0
    islands = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                islands += 1
                dfs(i, j)

    return islands

grid_1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]


grid_2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numberIslands(grid_1))
print(numberIslands(grid_2))


'''
runtime: O(mxn)
space: O(mxn)

'''



