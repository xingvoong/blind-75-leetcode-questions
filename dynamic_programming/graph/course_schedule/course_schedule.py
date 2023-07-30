'''
There are a total of numCourse courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi], indicates that you must take course b1 first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0, you have to first take course 1

Return true if you can finish all courses, otherwise, return false

Example 1:
Input: numCourses = 2, prerequisites = [[1, 0]]
Output: true
Explanation: there are a total of 2 courses to take. To take course 1, you should have finished course 0. So it is possible.

=> the later is prerequisites.

Example 2:
input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
output: false
explanation: there are a total of 2 courses to take. to take course 1, you should have finished course 0, and to take course 0, you should also have finished course 1. So it is impossible.


'''

class Solution:
    def dfs(self, node, adj, visit, inStack):
        # if the node is already in the stack, we have a cycle
        if inStack[node]:
            return True
        if visit[node]:
            return False
        # mark the current node as visited and part of current recursion stack
        visit[node] = True
        inStack[node] = True
        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, visit, inStack):
                return True

        # remove the node from the stack
        inStack[node] = False
        return False

    def canFinish(self, numCourses, prerequisites):
        adj = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[1].append(prerequisite[0])]

        visit = [False] * numCourses
        inStack = [False] * numCourses
        for i in range(numCourses):
            if self.dfs(i, adj, visit, inStack):
                return False
        return True


def canFinish(self, numCourse, prerequisites):
    courses = defaultdict(list)

    for c, p in prerequisites:
        courses[p].append(c)

    seen = set()

    def check_cycle(cur, path):
        if cur in path:
            return True
        if cur in seen:
            return False

        path.add(cur)
        for child in courses[cur]:
            if check_cycle(child, path):
                return True
        path.remove(cur)

        seen.add(cur)

        return False

    for cur in range(numCourse):
        if check_cycle(cur, set()):
            return False

    return True
