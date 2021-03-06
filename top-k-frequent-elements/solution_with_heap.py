'''
1: Problem Statement.
Given an array nums and an integter k, return the k most frequent elements.
You may return the answer in any order

Example 1:
Input: nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
- 1 <= nums.length <= 10 ** 5
- k is in the range [1, the number of unique elements in the array]
- it is guaranteed that the answer is unique

Follow up:  your algo's time complexity must be better than O(nlogn), where n is the array's size.

'''

def topKFrequent(nums, k):

  if len(nums) == 1:
    return nums

  import heapq
  valueMap = {}

  for i in range(len(nums)):
    if nums[i] in valueMap:
      valueMap[nums[i]] += 1
    else:
      valueMap[nums[i]] = 1

  return heapq.nlargest(k, valueMap.keys(), key=valueMap.get))

'''
Complexity Analysis
time: O(klog(K))
  - build a heap of k elements
space: O(n)
  - for valueMap
'''
