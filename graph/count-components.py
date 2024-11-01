'''
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph

Return the number of connected components in the graph
'''

def countComponents(n, edges):
    from collections import defaultdict

    # build a graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # visited array to keep track of all visited node
    visited = [False] * n

    # dfs function
    def dfs(node):
        # mark the node as visit
        visited[node] = True
        # visit all neighbors of the node
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    # count the number of connected components
    component = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            component += 1

    return component

n = 5
edges = [[0,1],[1,2],[3,4]]
edges2 = [[0,1],[1,2],[2,3],[3,4]]
print(countComponents(n, edges))
print(countComponents(n, edges2))