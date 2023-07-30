'''
you are given an integer array height of length n.  There are n vertical lines that drawn such that 2 endpoints of the ith line are (i, 0) and (i, height[i])

find 2 lines that together with the x-axis form a container, such that the container contains the most water

return the maximum amount of water a container can store

Intuition
- the area is limited by the height of shorter line
- the farther the lines, the more will be the area obtained.
- use 2 pointers, and move the pointers with shorter height.  This will decrease the width but increase the height, potentially.

- maintain a variable max area to store the max area obtained till now.
- the goal is to calculate the area, and return the max area
'''

def maxArea(height):
    max_area = 0
    left = 0
    right = len(height) - 1

    # use 2 pointers
    while left < right:
        width = right - left
        max_area = max(max_area, min(height[left], height[right]) * width)

        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return max_area


height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
height2 = [1, 1]
print(maxArea(height1))
print(maxArea(height2))