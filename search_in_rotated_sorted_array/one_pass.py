def search(nums, target):
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] == target:
            return mid

        # go left or right in the sub rotated index
        # find where the rorated index is
        # rotated index is not include mid
        elif nums[mid] >= nums[start]:
            # go left or rigth in the sub-array
            if target >= nums[start] and target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        # nums[mid] < nums[start]
        else:
            if target > nums[mid] and target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1