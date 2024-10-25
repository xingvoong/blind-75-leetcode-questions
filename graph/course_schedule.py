'''
course schedule on leetcode using Kahn'algo

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

step 0:
- no adjacency list, need to build one
step 1:
- calculate in degree of all nodes, courses in this case,
what course leet to another
step 2:
- get all courses that require to prereq,
step 3:
- process the courses
step 4:
- remove courses that need to prereq
step 5:
- check for cycle
'''

def canFinish(numCourses, prerequisites):
    from collections import defaultdict, deque
    # step 1: build the graph and calculate in degree
    # pre1 : course1,
    # pre2 : course2,
    # pre3: course3
    graph = defaultdict(list)
    in_degree = {i:0 for i in range(numCourses)}

    # pre -> course
    for course, pre in prerequisites:
        # add the direct edge, pre -> course
        graph[pre].append(course)
        in_degree[course] += 1

    # step 2: collect all courses with in-degree 0
    queue = deque([course for course in in_degree if in_degree[course] == 0])

    topological_order = []

    # step 3: process all courses


    while queue:
        course = queue.popleft()
        topological_order.append(course)

        # remove in-degree of course
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # check for cycles
    return len(topological_order) == numCourses


# Example usage:
numCourses = 4
prerequisites = [[1, 0], [2, 1], [3, 2]]
print(canFinish(numCourses, prerequisites))  # Output: True

