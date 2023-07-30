# definition for a node
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

from collections import deque

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: node
        :rtype: node
        """

        if not node:
            return node

        # Dictionary to save the visited node and it's respective clone as
        # key and value respectively. This helps to avoid cycles
        visited = {}

        # put the first node in the queue
        queue = deque([node])
        #clone the node and put it in the visited dictionary
        visited[node] = Node(node.val, [])

        # start BFS traversal
        while queue:
            # pop a node say "n" from the front of the queue
            n = queue.popleft()
            # iterate through all the neighbors of the node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    # add the newly encountered node to the queue
                    queue.append(neighbor)
                # add the clone neighbor to the clone node
                visited[n].neighbors.append(visited[neighbor])

        # return the clone of the node from visited
        return visited[node]


'''
let N be the number of node
M be the number of edges
time: O(N+M)
space: O(N), for the hashmap


'''
