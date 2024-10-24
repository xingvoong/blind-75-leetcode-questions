'''
Given unsorted array of integers nums, return the length of the longest consecutive elements sequence

You must write an algoritm that runs in O(n) time

this is actually a sliding window problem

example 1:
input: nums = [100, 4, 200, 1, 3, 2]
output: 4
explanation: the longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4

Example 2:
input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
output: 9

'''

def longestConsecutive(nums):

    numSet = set(nums)
    longest_streak = 0

    for num in nums:
        if num - 1 not in numSet:
            current_streak = 0
            while num + current_streak in numSet:
                current_streak += 1

        longest_streak = max(longest_streak, current_streak)

    return longest_streak

example_1 = [100, 4, 200, 1, 3, 2]
example_2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longestConsecutive(example_1))
print(longestConsecutive(example_2))

