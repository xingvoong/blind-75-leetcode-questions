'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum

a subarray is a contigious part of an array

- need to keep track of the current_subarray
- greedy: the max sub array is the current_subarray + num
'''

def maxSubArray(nums):
    largest_sum = current_subarray = nums[0]
    for num in nums[1:]:
        current_subarray = max(num, current_subarray + num)
        largest_sum = max(largest_sum, current_subarray)

    return largest_sum

print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray([5, 4, -1, 7, 8]))

'''
time: O(N)
space: O(1), only 2 extra space for result and current_subarray
'''