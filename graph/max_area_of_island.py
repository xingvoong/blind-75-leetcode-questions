'''
you are given an mxn binary matrix grid. An island is a group of 1's (representing land) connected 4 directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water


The area of an island is the number of cells with a value 1 in the island

return the maxinum area of an island in grid. if there is no island, return 0
'''

def maxAreaOfIsland(grid):

    # step 1: invalid inputs
    if not grid or not grid[0]:
        return 0

    # step 2: define grid dimensions and init a visited grid
    ROWS, COLS = len(grid), len(grid[0])
    visited = [[False]*COLS for  _ in range(ROWS)]
    max_area = 0

    # step 3: recursive DFS function to calculate area of an island
    def dfs(r, c):
        # mark the current cell as visited
        visited[r][c] = True

        # start area count at 1 for the current cell
        area = 1

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # check if the neighbor is within bounds, unvisited, and is part of the island
            if 0 <= nr < ROWS and 0 <= nc < COLS and not visited[nr][nc] and grid[nr][nc] == 1:
                # Accumulate area from connected cells
                area += dfs(nr, nc)

        return area

    # step 4: main loop to init DFS on each unvisted land cell
    for r in range(ROWS):
        for c in range(COLS):
            if not visited[r][c] and grid[r][c] == 1:
                max_area = max(max_area, dfs(r, c))

    # step 5: return the max area found
    return max_area

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(maxAreaOfIsland(grid))

'''
runtime: O(MxN)
- call dfs on each cell, there could ne MxN cell
space:  O(MxN)
- recursive stack
- extra grid for visited

'''