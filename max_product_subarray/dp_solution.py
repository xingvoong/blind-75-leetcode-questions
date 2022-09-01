def maxProduct(nums):
    if len(nums) == 0:
        return 0

    max_so_far = nums[0]
    min_so_far = nums[0]
    result = max_so_far

    for n in nums[1:]:
        temp = max(n, max_so_far * n, min_so_far * n)
        min_so_far = min(n, max_so_far * n, min_so_far * n)

        max_so_far = temp

        result = max(max_so_far, result)

    return result


nums1 = [2, 3, -2, 4]
nums2 = [-2, 0, -1]
nums3 = [-2, 3, -4]
print(maxProduct(nums1))
print(maxProduct(nums2))
print(maxProduct(nums3))

'''
runtime: O(N)
space: O(1)

'''
