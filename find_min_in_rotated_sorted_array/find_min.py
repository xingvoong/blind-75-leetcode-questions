'''
find min in rotated sorted array

Given the sorted rotated array nums of unique elements,
return the min element of this array

you must write an algorithm that runs in O(logN time)

example

return the min
'''

from gettext import find


def findMin(nums):

    if len(nums) == 1:
        return nums[0]

    left = 0
    right = len(nums) - 1

    if nums[left] < nums[right]:
        return nums[0]

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[mid+1]:
            return nums[mid+1]

        if nums[mid] < nums[mid - 1]:
            return nums[mid]

        if nums[mid] > nums[0]:
            left = mid

        else:
            right = mid + 1

nums1 = [3, 4, 5, 1, 2]
nums2 = [4, 5, 6, 7, 0, 1, 2]
print(findMin(nums1))
print(findMin(nums2))
