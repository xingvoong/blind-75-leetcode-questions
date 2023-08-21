def setZeroes(matrix):

    R = len(matrix)
    C = len(matrix[0])

    # additional variable first col
    is_col = False

    # assign the first row, and first column to 0
    for i in range(R):
        # check first col whether there is any 0
        if matrix[i][0] == 0:
            is_col = True
        for j in range(1, C):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    # iterate over the array once again
    # and using the first row and first column, update the elements
    for i in range(1, R):
        for j in range(1, C):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

    # check whether the first row need to set to 0
    if matrix[0][0] == 0:
        for j in range(C):
            matrix[0][j] = 0
    if is_col:
        for i in range(R):
            matrix[i][0] = 0

    return matrix


input1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
input2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

input3 = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
expected_output = [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

print(setZeroes(input1))
print(setZeroes(input2))
print(setZeroes(input3))

'''
I need to protect the first element regardless so only iterate from 1,
except the first element

Let N be the number of row
Let M be the number of col

runtime: O(NxM)
space: O(1)
'''