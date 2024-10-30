'''
Pacific Atlantic Water Flow

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans

Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
'''

def pacificAtlantic(heights):
    if not heights or not heights[0]:
        return []

    ROWS, COLS = len(heights), len(heights[0])
    pacific_reachable = [[False] * COLS for _ in range(ROWS)]
    atlantic_reachable = [[False] * COLS for _ in range(ROWS)]


    # DFS function to mark reachable cells
    def dfs(r, c, reachable):
        reachable[r][c] = True
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and not reachable[nr][nc] and heights[nr][nc] >= heights[r][c]:
                dfs(nr, nc, reachable)

    # run DFS for cells touching the pacific ocean (top and left edges)
    for r in range(ROWS):
        # left edge of pacific
        dfs(r, 0, pacific_reachable)
        # right edge of atlantic
        dfs(r, COLS - 1, atlantic_reachable)
    for c in range(COLS):
        # top edge of pacific
        dfs(0, c, pacific_reachable)
        # bottom edge of
        dfs(ROWS - 1, c, atlantic_reachable)

    # collect cells that are reachable by both oceans
    result = []
    for r in range(ROWS):
        for c in range(COLS):
            if pacific_reachable[r][c] and atlantic_reachable[r][c]:
                result.append([r, c])

    return result


heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

print(pacificAtlantic(heights))

