'''
You are given an mxn matrix board containing letter 'X' and '0', capture regions that are surrounded:
- connect: a cell is connected to adjacent cells horizontall or vertically
- region: to form a region connect every '0' cell
- surround: the region is surrounded with 'X'cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board

a surrounded region is captured by replacing all '0' with 'X's in the input matrix board.

Solution Approach

1: Mark unsurrounded regios:
- any '0' cell that is on the border or connected to an '0' on the border cannot be fully surrounded.
- start by making these unsurrounded cells (border-connected '0' cells) using a temporary marker (e.g, '#') through depth-first search (DFS) or BFS

2: transform surrounded regions
- once we mark add edge-connected cells as "#", traverse the board and:
- convert any remaning '0' cells to 'X' (as they are surrounded)
- restore '#' cells back to '0' (as they are edge-connected and should not be captured)

'''
def solve(board):

    # step 1: invalid inputs:
    if not board or not board[0]:
        return

    # step 2: define grid dimensions
    ROWS, COLS = len(board), len(board[0])

    # step 3: recursive DFS function to mark unsurrounded regions
    def dfs(r, c):
        # mark the current cell as part of an unsurrounded region
        board[r][c] = '#'

        # list of possible direction
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # exploring neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == 'O':
                dfs(nr, nc)

    # step 4: mark all 'O' on the border and connected to the border as '#'
    for r in range(ROWS):
        # left border
        if board[r][0] == 'O':
            dfs(r, 0)
        # right border
        if board[r][COLS-1] == 'O':
            dfs(r, COLS-1)

    for c in range(COLS):
        # top border
        if board[0][c] == 'O':
            dfs(0, c)
        if board[ROWS-1][c] == 'O':
        # bottom border
            dfs(ROWS-1, c)

    # step 5: tranform the board by capturing surrounded regions

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == '#':
                board[r][c] = 'O'

    return board


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(solve(board))

board2 = [["X","O","X"],["O","X","O"],["X","O","X"]]
print(solve(board2))



