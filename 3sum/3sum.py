'''
given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j and i != k, and j!= k
and nums[i] + nums[j] + nums[k] == 0

notice that the solution set must not contain duplicate triplets

Hint 1: reduce to 2sum, what number is missing that would make
x + y = -k
or x + y = a
a + k = 0

Hint 2: for the 2 sum problem, if we fix one of the numbers, say x,
we have to scan the entire array to find the next y, which is
value -x where vlaue is the input parameter. can we change our array somehow so that this search becomes faster?


Hint 3:  the second train of though for 2 sum is, without changing the array, can
we use additional space somehow?  like maybe a hashmap to speed uo the search

'''
def threeSum(nums):
    res = []
    nums.sort()

    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i-1] != nums[i]:
            twoSum(nums, i, res)

    return res


def twoSum(nums, i, res):
    seen = set()
    j = i + 1

    while j < len(nums):
        complement = -nums[i] - nums[j]

        if complement in seen:
            res.append([nums[i], nums[j], complement])

            while j + 1 < len(nums) and nums[j] == nums[j+1]:
                j += 1

        seen.add(nums[j])

        j+=1


nums1 = [-1,0,1,2,-1,-4]
nums2 = [0,1,1]
nums3 = [0,0,0]
print(threeSum(nums1))
print(threeSum(nums2))
print(threeSum(nums3))
