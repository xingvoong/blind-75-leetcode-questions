'''
given an integer array nums, return an array answer such that answer[i] is equal to the product of all the element of nums except nums[i]

The product of any prefix or suffix of nums is guaranteed to fit in a 32-fit integer
You must write an algorithm that runs in O(N) time and without using the division operation
Goal:
- nums          [1, 2, 3, 4]
- left_product: [1, 1, 2, 6]

- nums           [1, 2, 3, 4]
- right_product: [24, 12,4,1]
- result: [24, 12, 8, 6 ]

'''

def product_except_self(nums):
    left_product = [1] * len(nums)
    right_product = [1] * len(nums)
    for i in range(1, len(nums)):
        left_product[i] = left_product[i-1] * nums[i-1]

    for j in range(len(nums) - 2, -1, -1):
        right_product[j] = right_product[j+1] * nums[j+1]

    for k in range(len(nums)):
        left_product[k] *= right_product[k]

    return left_product

print(product_except_self([1,2,3,4]))
print(product_except_self([-1,1,0,-3,3]))

'''
runtime: O(3N) = O(N)
space: O(2N) = O(N)
'''

# Optimize solution
# nums:          [1, 2, 3, 4]
# right_product: [24, 12, 4, 1]
# left_product:  [1, 1, 2, 6]
# result:        [24, 12, 8, 6]
'''
now, I am going to go backward to commute the right product
- the result = current right_product * left product
- next_right_product = right_product - current nums
'''

def product_except_self(nums):
    result = [1] * len(nums)
    right_product = 1

    for i in range(1, len(nums)):
        result[i] = result[i-1] * nums[i-1]

    for j in range(len(nums) - 1, -1, -1):
        result[j] *= right_product
        right_product = right_product * nums[j]

    return result


print(product_except_self([1,2,3,4]))
print(product_except_self([-1,1,0,-3,3]))

'''
runtime: O(2N) => O(N)
space: O(2N) => O(2N)
'''