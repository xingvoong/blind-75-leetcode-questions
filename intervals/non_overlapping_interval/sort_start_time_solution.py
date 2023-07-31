'''
Algo:
1: check whether it is:
- overlapping: prev_end > current_start
    - increase the count by 1
    - completely overlap: prev_end > current_end
        - use greedy: remove the interval directly after it by update previous
- if no overlap:
    - move on by update previous

2: return the count

'''


def eraseOverlapIntervals(intervals):
    # sort base on starting time:
    intervals.sort(key=lambda x:x[0])

    n = len(intervals)
    prev = 0
    count = 0

    for i in range(1, n):
        prev_end = intervals[prev][1]
        current_start = intervals[i][0]
        if prev_end > current_start:
            count += 1


            current_end = intervals[i][1]
            if prev_end > current_end:
                prev = i
        else:
            prev = i

    return count
