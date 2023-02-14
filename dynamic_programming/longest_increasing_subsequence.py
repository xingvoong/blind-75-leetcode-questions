'''
Longest increasing subsequence

Given an integer array nums, return the length of the longest strictly increasing
subsequence.

Example 1:
input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
explanation: the longest increasing subsequence is [2, 3, 7, 101],
there the length is 4


example 2:
input: nums = [0, 1, 0, 3, 2, 3]
output: 4

example 3:
input: nums = [7, 7, 7, 7, 7, 7]
output: 1

Constraints:
- 1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4

Follow up: can you come up with an algorithm that runs in O(nlog(n)) time complexity?

'''


def lengthOfLIS(nums):

    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)


nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
nums2 = [0, 1, 0, 3, 2, 3]
nums3 = [7, 7, 7, 7, 7, 7, 7]

print(lengthOfLIS(nums1))
print(lengthOfLIS(nums2))
print(lengthOfLIS(nums3))

