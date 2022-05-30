'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if everyy element is distinct


goal:
- make a hashmap
- if it has not seen, add in the hashmap
- if has seen, return true
- in the end, return false
'''

def containsDuplicate(nums):
    hash_map = {}
    for i in range(len(nums)):
        if nums[i] in hash_map:
            return True
        else:
            hash_map[nums[i]] = 1

    return False


print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

'''
run time: O(N)
space: O(1)
'''