'''
given an int array nums, find the contiguos subarray (containing at least one number) which has the largest sum and return its sum

a subarray is a contigious part of an array

- the largest sum at a given moment can is:
+ the current number
+ or the current sub array + current_number
+ this can be solve by doing greedy
'''

def maxSubArray(nums):
    largest_sum = nums[0]
    current_sub_array = nums[0]

    for num in nums[1:]:
        current_sub_array = max(num, current_sub_array + num)
        largest_sum = max(current_sub_array, largest_sum)

    return largest_sum

nums1 = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [1]
nums3 = [5, 4, -1, 7, 8]
print(maxSubArray(nums1))
print(maxSubArray(nums2))
print(maxSubArray(nums3))

'''
let N be the length of the nums array

runtime: O(N)
space: O(1)

'''