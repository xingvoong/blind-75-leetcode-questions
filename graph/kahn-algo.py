'''
- perform topological sorting on directed acylic graph (DAG)
- Use BFS

Purpose

Topoligical sorting of a DAG is a linear ordering of vertices such that
for every directed edge u->v, vertex u appear before vertex v in the ordering

Key Concepts:
- In-degree of a vertex: The number of incoming edges to that vertex
- A vertex with an in-degree of zero means there are no dependencies before
it, so it can appear early in ordering

Steps of Kahn's algorithm:
1: Calculate in-degress
2: Add all vertices with in-degree 0 to a queue
3: Process the vertices in the queue
- remove a vertex from the queue
- add it to the topological ordering
- for each neighbor of the vertex, decrease its in-degree by 1 (since we have
removed an edge from the graph)
- if any neighbor's in-degree becomes 0, add it to the queue

4: repeat
5: check for cycles

For this to work:
- I need an adjacency list

Use cases:
- Task scheduling: when certain tasks must be completed before others
- Course presequisites: determining an order of courses bases on presequite dependencies
- compilation order: deciding the order in which code files or modules should be complied

'''

from collections import defaultdict, deque

def kahn_topological_sort(graph):
    # step 1: calculate in-degree of all vertices
    # initialize all in-degree to 0
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            # edge u->v: so in degree of v += 1
            in_degree[v] += 1

    # step 2: collect vertices with in-degree 0
    queue = deque([v for v in graph if in_degree[v] == 0])

    topological_order = []

    # step 3: process vertices in queue
    while queue:
        u = queue.popleft()
        topological_order.append(u)

        # step 4: decrease in-degree of all neighbors
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # step 5: check for cycles
    if len(topological_order) != len(graph):
        raise ValueError("Graph contains a cycle, topological sorting is not possible.")


    return topological_order


# Example usage:
if __name__ == "__main__":
    # Define a graph using adjacency list representation
    graph = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: [4],
        4: []
    }

    try:
        top_order = kahn_topological_sort(graph)
        print("Topological Order:", top_order)
    except ValueError as e:
        print(e)