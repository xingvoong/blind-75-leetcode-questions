def pacificAtlantic(matrix):

    # check if input is empty:
    if not matrix or not matrix[0]:
        return []
    
    # initialize variables, including sets used to keep track of visited cells
    num_rows, num_cols = len(matrix), len(matrix[0])
    
    # setup each queue with cells adjacent to their respective ocean

    pacific_queue = deque()
    atlantic_queue = deque()
    for i in range(num_rows):
        pacific_queue.append((i, 0))
        atlantic_queue.append((i, num_cols - 1))
    for i in range(num_cols):
        pacific_queue.append((0, i))
        atlantic_queue.append((num_rows - 1, i))

    def bfs(queue):
        reachable = set()
        while queue:
            (row, col) = queue.popleft()
            # this cell is reachable, so mark it
            reachable.add((row, col))
            for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # check all 4 directions
                new_row, new_col = row + x, col + y
                # check if the new cell is within bounds
                if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                    continue
                # check that the new cell hasn't already been visited
                if (new_row, new_col) in reachable:
                    continue
                #check that the new cell has a higher or equal heights,
                
                # so that water can flow from the new cell to the old cell
                if matrix[new_row][new_col] < matrix[row][col]:
                    continue
                # if we've gotten this far, that means the new cell is reachable
                queue.append((new_row, new_col))
            return reachable
        
        # perform a bfs for each ocean to find all cells accessible by each ocean
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)

        # find all cells that can reach both oceans, and convert to list
        return list(pacific_reachable.intersection(atlantic_reachable))
    
