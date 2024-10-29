'''
I: n nodes, labels from 0 to n - 1 and an array of n - 1 edges,
where edges[i] = [ai, bi] indicates that there is an undirected edge
between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root,
the result tree has height h. Among all possible rooted trees, those with min height (i.e min(h)) are called min height trees (MHTs)

return a list of all MHTs root labels. You can return the answer in any order

Input: n = 4, edges = [[1, 0],[1, 2], [1, 3]]
Output: [1]
explanation:


- use technique similar to Kahn's algorithm, which is primarily used for topological sorting of directed acyclic graph (DAGs). Here, we'll use a modified version of it to find MHT. The idea is to trim the tree layer by layer, removing the leaves (nodes with only connection) until we reach the centroids of the tree, which will be our roots for MHTs.

Approach:
1: Identify leaves: a leaf is a node with only one edge. We can find all the leaves at the beginning
2: Remove leaves level by level: use a process similar to BFS to remove leaves iteratively. After removing the current leaves, the new set of leaves will emgere. This process continues until we are left with 1 or 2 nodes
3: The remaining nodes are the MHT roots: There are the centroids of the tree, which can be considered as the root nodes of MHT.

'''

def findMinHeightTrees(n, edges):
    from collections import deque, defaultdict

    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    # step 1: build the adjacency graph and in degree
    graph = defaultdict(list)
    degree = {i:0 for i in range(n)}

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1

    # step 2: get all the leaf nodes
    queue = deque([node for node in degree if degree[node] == 1])


    # step 3: remove leave layer by layer, until only centroids, either 1 or 2 nodes left
    remaining_nodes = n
    while remaining_nodes > 2:
        leaves_count = len(queue)
        remaining_nodes -= leaves_count

        # process current layer of leaves
        for _ in range(leaves_count):
            leaf = queue.popleft()

            for neighbor in graph[leaf]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    queue.append(neighbor)

    # remain nodes are the MHT
    return list(queue)





    # step 4:





edges_1= [
    [0, 1],
    [0, 2],
    [0, 3],
    [3, 4],
    [4, 5]
]

n_1 = 6  # Total number of nodes

n_2 = 4
edges_2 = [[1,0],[1,2],[1,3]]

n_3 = 6
edges_3= [[3,0],[3,1],[3,2],[3,4],[5,4]]

# Call the function to find Minimum Height Trees
mht_roots1 = findMinHeightTrees(n_1, edges_1)
mht_roots2 = findMinHeightTrees(n_2, edges_2)
mht_roots3 = findMinHeightTrees(n_3, edges_3)

print("Minimum Height Trees Roots:", mht_roots1)
print("Minimum Height Trees Roots:", mht_roots2)
print("Minimum Height Trees Roots:", mht_roots3)

'''
edges = [
    [0, 1],
    [0, 2],
    [0, 3],
    [3, 4],
    [4, 5]
]

n = 6
     0
   / | \
  1  2  3
        |
        4
        |
        5

'''