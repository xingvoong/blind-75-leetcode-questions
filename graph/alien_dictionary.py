'''
There is a new alian language that uses the English alphabet. However, the order of the letters is unknown to you

You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are sorted lexicographically by the rules of this new langauge

if this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicopgraphically increasing order by the new language's rules. If there are multiple solutions, return any of them.

1: Graph representation

- treat each characer as a node
- if a character comes before another in two consecutive words, draw a directed edge from the first character to the second. This will help us determine the relative order of the character

2: Topological sortring

- Since the problem essentially boils down to determining the order of characters, we can solve it using topological sorting on a directed acylic graph (DAG)

- if we detect a cycle during the sorting, it means the input is inconsistent, and we should return ""

3: Implementation steps:
- create an adjacency list to represent the graph
- track the in-degree (number of incoming edges) for each node
- compare each pair of adjacent words to build the graph
- perform a topological sort using Kahn's algorithm (BFS-based approach)

'''

def alianOrder(words):
    from collections import defaultdict, deque

    # step 1: init the in degree list and graph
    graph = defaultdict(list)
    in_degree = {}


    in_degree = {char: 0 for word in words for char in word}

    # step 2: build the graph by comparing adjacent words
    for i in range(len(words) - 1):
        first_word = words[i]
        second_word = words[i+1]

        # find the first different character
        min_length = min(len(first_word), len(second_word))
        found_different = False

        for j in range(min_length):
            if first_word[j] != second_word[j]:
                # there is a directed edge from first_word[j]
                # to second_word[j]
                graph[first_word[j]].append(second_word[j])
                in_degree[second_word[j]] += 1
                found_different = True
                break

        # edge case: check for invalid input like ["abc", "ab"]
        if not found_different and len(first_word) > len(second_word):
            return ""

    # step 3: perform topological sort (Kahn's algoritm)
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    result = []

    while queue:
        current_word = queue.popleft()
        result.append(current_word)

        for neighbor in graph[current_word]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # if we have sorted all characters, return the result
    if len(result) == len(in_degree):
        return "".join(result)
    else:
        # there was a cycle, meaning the input was inconsistent
        return ""

words = ["wrt","wrf","er","ett","rftt"]
result = alianOrder(words)
print(result)  # Output should be "wertf"









