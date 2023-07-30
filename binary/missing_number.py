'''
given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array

example 1:
input: nums = [3, 0, 1]
output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0, 3]. 2 is the missing number in the range since it does not appear in nums

example 2:
input: nums = [0, 1]
output: 2
explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0, 2]. 2 is the missing number in the range since it does not appear in nums

example 3:
input: nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
output: 8
'''

def missingNumber(nums):
    n = len(nums)
    expected_sum = n*(n+1)//2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

nums1 = [3, 0, 1]
nums2 = [0, 1]
nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missingNumber(nums1))
print(missingNumber(nums2))
print(missingNumber(nums3))


def missingNumber2(nums):
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    
    return missing
    

