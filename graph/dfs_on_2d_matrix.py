'''
General Recursive DFS Template for 2D matrix problems

This template handles problems where:
- The matrix represents a grid where each cell is a node
- we're trying to find connected components or regions that meet specific criteria (e.g, islands or reachable cells)

example for number of islands, or number of connected components
'''

def solve_matrix_problem(grid):

    # step 1: invalid inputs
    if not grid or not grid[0]:
        return 0

    # step 2: define matrix dimensions and initialize a visited matrix
    ROWS, COLS = len(grid), len(grid[0])

    visited = [[False] * COLS for _ in range(ROWS)]

    result = 0

    # step 3: recursive DFS function with the main function
    def dfs(r, c):
        # mark the current cell as visited
        visited[r][c] = True

        # list of possible directions (up, down, left, right)
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        # explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # check if the neighbor is within bounds and meets criteria
            if 0 <= nr < ROWS and 0 <= nc < COLS and not visited[nr][nc]:
                # add additional check if needed
                # matrix[nr][nc] == '1' for islands
                dfs(nr, nc)

    # step 4: main loop to init DFS on unvisited cells that meet criteria
    for r in range(ROWS):
        for c in range(COLS):
            # Check if the cell has not been visited and meets the starting criteria
            # Add a criteria check here if needed, e.g., matrix[r][c] == '1'
            if not visited[r][c] and grid[r][c] == "1":
                dfs(r,c)
                result += 1

    # step 5: return result
    return result


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

# count number of 1
print(solve_matrix_problem(grid))

'''
runtime: O(rows x cols)
space: O(rows x cols)

'''