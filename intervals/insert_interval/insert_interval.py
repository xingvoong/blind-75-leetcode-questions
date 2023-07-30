'''
You are given an array of non-overlapping intervals intervals where
intervals[i] = [start_i, end_i] represent the start and the end of the ith interval and intervals is sorted in ascending order by start_i. You are also given an interval newInterval = [start, end] that represents the start and end of another interval

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still not have any overlapping intervals (merge overlapping intervals if neccessary)

return intervals after the insertion

example 1:
input: intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
output: [[1, 5], [6, 9]]

example 2:
input: intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
newInterval = [4, 8]
output: [[1, 2], [3, 10], [12, 16]]
explanation: because the new interval [4,8] overlaps with [3, 5], [6, 7]. [8, 10]

'''

def insert(intervals, newInterval):

    # step 1: append the new interval in intervals
    intervals.append(newInterval)

    # step 2: sort them again
    intervals.sort()
    n = len(intervals)
    toReturn = [intervals[0]]

    # step 3: merge
    # 3.1: prepare for merging
    for i in range(1, n):
        current_start = intervals[i][0]
        current_end = intervals[i][1]

        previous_start = toReturn[-1][0]
        previous_end = toReturn[-1][1]

        if current_start <= previous_end:
            new_start = min(current_start, previous_start)
            new_end = max(current_end, previous_end)
            toReturn.pop(-1)
            toReturn.append([new_start, new_end])
        else:
            toReturn.append(intervals[i])

    return toReturn


print(insert([[1, 3], [6, 9]], [2, 5]))
print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))


'''
complexity: sort runtime is O(NLogN)

'''