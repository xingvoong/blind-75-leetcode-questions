'''
Given a reference of a node in a connected undirected graph

Return a deep copy (clone) of the graph.

Each node in the graph contains a value(int) and a list(List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:
each node's value is the same as the node's index(1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Input: adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]

Algo:
- build the clone node, and the graph as we go
- undirected, connected graph, so we need to avoid cycle

'''
"""
# definition for a node

"""


class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

def __init__(self):
    # dictionary to save the visited node and it's respective clone
    # as key and value resepectively. This helps to avoid cycles
    self.visited = {}

def cloneGraph(self, node):
    """
    :type node: Node
    :rtype: Node
    """

    # if the node was already visited before
    # return the clone from the visited dictionary
    if node in self.visited:
        return self.visited[node]

    # create a clone for the given node
    # node that we don't have clone neighbors as of now, hence [].
    clone_node = Node(node.val, [])

    # the key is original node and value being the clone node
    self.visited[node] = clone_node

    # iterate through the neighbors to generate their clones
    # and prepare a list of cloned neighbors to be added to the cloned node
    if node.neighbors:
        clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

    return clone_node


'''
Complexity Analysis:
Let N be the number of nodes
M be the number of vertices

- time complexity: O(N+M), where N is a number of nodes (vertices) and M is the number of edges
- Space: O(N) + O(H) = > O(N)

H: the height of the graph:
N: the number of nodes for the hashmap



'''