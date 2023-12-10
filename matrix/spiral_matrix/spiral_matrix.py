'''
Given an mxn matrix, return all elements of the matrix in spiral order

'''

def spiralOrder(matrix):
    result = []
    rows = len(matrix)
    columns = len(matrix[0])
    top = left = 0
    right = columns - 1
    bottom = rows - 1

    while len(result) < rows * columns:
        # traverse from left to right
        for col in range(left, right + 1):
            result.append(matrix[top][col])

        # traverse downwards
        for row in range(top + 1, bottom + 1):
            result.append(matrix[row][right])

        # make sure we are now on a different row
        if top != bottom:
            # traverse from right to left
            for col in range(right-1, left - 1, -1):
                result.append(matrix[bottom][col])

        # make sure we are now on a different col
        if left != right:
            # traverse from bottom to top
            for row in range(bottom - 1, top, -1):
                result.append(matrix[row][left])

        left += 1
        right -= 1
        top += 1
        bottom -= 1

    return result

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


print(spiralOrder(matrix1))
print(spiralOrder(matrix2))







