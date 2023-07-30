def canFinish(numCourses, prerequisites):
    indegree = [0] * numCourses
    adj = [[] for _ in range(numCourses)]

    
    for prerequisite in prerequisites:
        adj[prerequisite[1]].append(prerequisite[0])
        # the goal is to reduce the number of 0 in degree
        indegree[prerequisite[0]] += 1

    queue = dequeu()
    for i in range(numCourse):
        if indegree[i] == 0:
            queue.append(i)

    nodesVisited = 0
    while queue:
        node = queue.popleft()
        nodesVisited += 1

        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return nodesVisited == numCourses
'''
There is an mxn rectangular island that border both the pacific ocean and
atlantic ocean. The pacific ocean touches the island's left and top edges, and the atlantic ocean touches the island's right and bottom edges.

The island is partioned into a grid of square cells. You are given an mxn integer matix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cell directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinate result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.



'''