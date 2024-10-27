'''
you have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph

return true if the edges of the given graph make up a valid tree, and false otherwise.

Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

modify Kahn' algorithm:
- reduce indegree
- detect cycle


Step 1: check edge count:
    - if the number of edges isn't n - 1, the graph can't be a tree (its either disconnected or has cycles). Return False immediately

Step 2: Build the graph and track degree
    - construct an adjacency list to represent the undirected graph
    - maintain a degree count for each node

Step 3: Init queue with leaf nodes
    - start with nodes that have a degree of 1 (leaf nodes)
    - This is analogous to Kahn' algo queue for nodes with zero in-degree in a directed graph

Step 4:
    - use a queue to iteratively "peel off" leaf nodes
    - for each node processed, reduce the degree of its neighbors. if any neighbor's degree become 1, add it to the queue
    - keep track of the number of processed nodes

Step 5:
    - If the number of processed nodes equal to n, then all nodes were part of the graph, and no cycles were present, indicating a valid tree
    - if fewer nodes are processed, it means some nodes were part of a cycle or disconnected component, so return false

'''
# n nodes, edges
def validTree(n, edges):

    from collections import defaultdict, deque
    # step 0: for this problem, tree definition, check the edge count
    if len(edges) != n - 1:
        return False

    # check for special case: only 1 node, no leaf
    if n == 1 and len(edges) == 0:
        return True
    # step 1: build the adjacency list and degree count
    graph = defaultdict(list)
    degree = {i:0 for i in range(n)}

    # undirected graph
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1

    # step 2: get all the nodes with in degree of 1
    queue = deque([v for v in degree if degree[v] == 1])

    # step 3: process all the nodes
    # don't need a list
    processed_node = 0
    while queue:
        leaf = queue.popleft()
        processed_node += 1

        for neighbor in graph[leaf]:
            degree[neighbor] -= 1
            if degree[neighbor] == 1:
                queue.append(neighbor)

    return processed_node == n


# Example usage:
print(validTree(5, [[0,1],[0,2],[0,3],[1,4]]))  # Output: True
print(validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))  # Output: False
print(validTree(1, [])) #output True


'''
let n is the number nodes
m is the number of edges, or len(edges)

runtime: O(n + m)
space: O(n + m)

'''


