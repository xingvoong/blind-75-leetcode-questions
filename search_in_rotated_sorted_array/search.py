'''
search in rotated sorted array

there is an integer array nums sorted in ascending order (with distinct values)

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k <= nums.length).

given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algo with O(logN) runtime complexity

# nums[0] = 4
# target = 1
# 1 < 4: search in the right side
# binary_search(nums, rotation_index, n - 1, target)

# if target > nums[0]
# because ascending order, if there is no rotation, 1 2 3 4 5 6
# compare with the first element so we can know where they are
nums = [4, 5, 6, 7, 0, 1, 2]

'''


def find_rotation_index(nums):

        if len(nums) == 1:
            return 0

        left = 0
        right = len(nums) - 1

        # if the array is already sorted, then no need to do the search

        if nums[left] < nums[right]:
            return 0

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid+1]:
                return mid+1

            if nums[mid] < nums[mid - 1]:
                return mid

            # have not seen the rotation, keep searching
            if nums[mid] > nums[0]:
                left = mid + 1
            # nums[mid] < nums[0]
            # already seen the rotation, search right
            else:
                right = mid - 1

def binary_search(nums, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def search(nums, target):
    # similar to previous questions
    # use a binary search

    # find the rotation index
    rotation_index = find_rotation_index(nums)
    n = len(nums)

    # if the array only has 1 element
    if n == 1:
        if nums[0] == target:
            return 0
        else:
            return -1

    # if the rotation index element is the target
    if nums[rotation_index] == target:
        return rotation_index

    # if the array is not rotated
    if rotation_index == 0:
        return binary_search(nums, 0, n - 1, target)

    # search right
    if target < nums[0]:
        return binary_search(nums, rotation_index, n - 1, target)

    # search left
    else:
        return binary_search(nums, 0, rotation_index, target)


nums1 = [4, 5, 6, 7, 0, 1, 2]
nums2 = [1]
nums3 = [1, 3]

target1 = 0
target2 = 6
target3 = 3
target4 = 0


print(search(nums1, target1))
print(search(nums1, target2))
print(search(nums1, target3))
print(search(nums2, target4))
print(search(nums3, 3))





