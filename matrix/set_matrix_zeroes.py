'''
Given an mxn integer matrix matrix, if an element is 0, set it entire row and column to 0's


You must do it in place (no return new matrix, but the same one)

Follow up:
- a straightforward solution using O(mn) space is prob a bad idea
- a simple improvement uses O(m + n) space, but still not the best solution
- could you devise a constant space solution?
'''

def setZeros(matrix):
    R = len(matrix)
    C = len(matrix[0])

    row_set = set()
    col_set = set()

    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                row_set.add(i)
                col_set.add(j)

    for i in range(R):
        for j in range(C):
            if i in row_set or j in col_set:
                matrix[i][j] = 0

    return matrix



input1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
input2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(setZeros(input1))
print(setZeros(input2))

