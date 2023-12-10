'''
You are given an nxn 2D matrix representing an image, rotate the image by 90 degree (clockwise)

You have to rotate the image(in-place), which means you have to modify the input 2D matrix directly. Do not allocate another 2D matrix and do the rotation

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
'''

def rotateMatrix(matrix):
    n = len(matrix)

    def transpose(matrix):
        for i in range(n):
            for j in range(i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

    def reverse(matrix):
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
        return matrix

    transpose(matrix)
    reverse(matrix)

    return matrix

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

print(rotateMatrix(matrix1))
print(rotateMatrix(matrix2))

'''
runtime:
let N be the number of rows
runtime: O(NxN)
space: O(NxN)
'''
