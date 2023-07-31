'''
Given an array of intervals where intervals[i] = [starti, endi], return the mininum number of intervals you need to remove to make the rest of the intervals non-overlapping

Example 1:
input: intervals = [[1,2], [2, 3], [3, 4], [1, 3]]
ouput: 1
explanation: [1, 3] can be removed and the rest of the intervals are non-overlapping

example 2:
input: intervals = [[1, 2], [1, 2], [1, 2]]
output: 2
explanation: you need to remove two [1, 2] to make the rest of the intervals non-overlapping

example 3:
input: intervals = [[1, 2], [2, 3]]
output: 0
explanation: you don't need to remove any of the intervals since they're already non-overlapping

Algo:
1: import inf
2: let k be the smallest inf, or -inf

3: go through the intervals to
3.1:  check whether k is
if k >= x,
- there is no over lap
- update k to equal to the previous end
else:  x > k > y
there is overlap
increase count
4:

'''

from cmath import inf


def eraseOverLapInterval(intervals):
    intervals.sort(key=lambda x:x[1])
    ans = 0
    k = -inf

    for start, end in intervals:
        # case 1
        # take this interval
        if start >= k:
            k =  end
        else:
            ans += 1

    return ans


'''
runtime: O(NlogN)
- because of the sorting
space:
- O(1)

'''