'''
given an integer array nums, find a contiguos non empty subarray within the array that has the largest product, and return the product

the test cases are generated so that the answer will fit in
a 32-bit integer

a subarray is a contiguos subsequence of the array

example 1:

- can I solve this using the same techque as the max_sum
- the problem with product sub array is that they can have negative number and 0
- but, I mean does that


the most naive way to tackle this problem is to go through each element in nums, and for each element, consider the product of every a contiguous subarray starting from that element.  This will result in a cubic runtime

for i in[0... nums-1]:
    for j in [i..nums-1]:
        accumulator = 1
        for k in [i..j]:
            accumulator = accumulator * nums[k]
        result = max(result, accumulator)

Brute force solution:
- at each index: find the sub arrays that can include that index


'''


from itertools import accumulate


def maxProduct(nums):
    if len(nums) == 0:
        return 0

    result = nums[0]

    for i in range(len(nums)):
        current_product = 1
        for j in range(i, len(nums)):
            current_product *= nums[j]
            result = max(result, current_product)

    return result

nums1 = [2,3,-2,4]
nums2 = [-2,0,-1]
nums3 = [-2, 3, -4]
print(maxProduct(nums1))
print(maxProduct(nums2))
print(maxProduct(nums3))

'''
runtime: O(N^2)

'''


def maxSubArray(nums):
    if len(nums) == 0:
        return 0

    result = 0

    for i in range(len(nums)):
        current_total = 0
        for j in range(i, len(nums)):
            current_total += nums[j]
            result = max(current_total, result)

    return result


nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [1]
nums3 = [5, 4, -1, 7, 8]
print(maxSubArray(nums1))
print(maxSubArray(nums2))
print(maxSubArray(nums3))
