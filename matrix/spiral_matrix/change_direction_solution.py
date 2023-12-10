'''
There are only 2 movement patterns, right+down and left+up. In the first case we increment either the row or columm by 1, and in the latter case we increment either the row or columb by -1. Also notice that after we move horizontally the number of possible vertical steps decrease by 1, and after
we move vertically the number of possible horizontal steps decrease by 1. When we run out of either vertical steps or horizontal steps, we reach the end. Therefore a simple solution is
'''

def spiralOrder(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    direction = 1
    i, j = 0, -1
    output = []

    while rows * columns > 0:
        for _ in range(columns): # move horizontally
            j += direction
            output.append(matrix[i][j])

        rows -= 1

        for _ in range(rows): # move vertically
            i += direction
            output.append(matrix[i][j])

        columns -= 1
        direction *= -1 #flip direction

    return output




matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


print(spiralOrder(matrix1))
print(spiralOrder(matrix2))
