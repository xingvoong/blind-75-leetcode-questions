'''
Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overllapping intervals that cover all the intervals in the input

example 1:
input: intervals = [[1, 3], [2, 6], [8,10], [15, 18]]
output: [[1, 6], [8, 10], [15, 18]]
explanation: since intervals [1, 3] and [1, 6] overlap, merge them into [1, 6]

example 2:
input: intervals = [[1, 4], [4, 5]]
output: [[1, 5]]
explanation: intervals [1, 4] and [4, 5] are considered overlapping
'''


def merge(intervals):
    intervals = sorted(intervals, key=lambda x: x[0], reverse=False)

    n = len(intervals)
    toReturn = [intervals[0]]

    # for loop to go through intervals:
    # start at 1 because I need to compare witht the previous
    for i in range(1, n):
        if len(toReturn) > 0:
            current_start = intervals[i][0]
            current_end = intervals[i][1]
            prev_start = toReturn[-1][0]
            prev_end = toReturn[-1][1]

            # compare current interval with the previous interval
            # over lap
            if current_start <= prev_end:
                new_start = min(current_start, prev_start)
                new_end = max(current_end, prev_end)
                new_interval = [new_start, new_end]
                # have to return the previous one
                # before appending a new now
                toReturn.pop()
                toReturn.append(new_interval)
            else:
                toReturn.append(intervals[i])

    return toReturn


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge([[1, 4], [4, 5]]))
