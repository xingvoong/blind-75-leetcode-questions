'''
Given an array of integers nums and an integer target, return indices of the 2 numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice

You can return the answer in any order

Example 1:
input: nums = [2, 7, 11, 15], target = 9
output: [0, 1]
Explanation: because nums[0] + nums[1] == 9, we return [0, 1]

Example 2:

input: nums = [3, 2, 4], target = 6
output: [1, 2]

Example 3:
input: nums = [3, 3], target = 6
Output: [0, 1]

'''

def twoSum(nums, target):
    # 2 steps:
    # build the hashmap
    # traverse the hashmap
    hash_map = {}
    for i in range(len(nums)):
        remain = target - nums[i];
        if remain not in hash_map:
            hash_map[nums[i]] = i
        else:
            return [hash_map[remain], i]
    return hash_map


print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))

'''
runtime: O(N)
space: O(N)
'''