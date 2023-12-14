def exist(board, word):

    MAX_ROW = len(board)
    MAX_COL = len(board[0])

    def backtracking(row, col, remain_characters):

        # condition to stop
        if len(remain_characters) == 0:
            return True

        # check the current status before going to backtracking
        # if out of bound or the letter in the current cell does not
        # match with letter of the current word
        #then return false

        if row < 0 or row >= MAX_ROW or col < 0 or col >= MAX_COL or board[row][col] != remain_characters[0]:
            return False

        # mark the current position before exploring further
        # so we don't revisit it
        board[row][col] =  '#'

        # backtracking, explore all possible choices
        for row_offset, col_offset in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            if backtracking(row + row_offset, col + col_offset, remain_characters[1:]):
                return True

        # revert the choice back:
        board[row][col] = remain_characters[0]

        return False

    for row in range(MAX_ROW):
        for col in range(MAX_COL):
            if backtracking(row, col, word):
                return True
    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

word1 = "ABCCED"
word2 = "SEE"
word3 = "ABCB"

print(exist(board, word1))
print(exist(board, word2))
print(exist(board, word3))

'''
runtime: O(N3^L)

N: is the number of cell in the board
L is the length of the word

- go through the board take N time
- 3 for each direction backtracking can do,
starts with 4 but reduce to 3 because you can't go back to the one already visitied
- search for at most L lenght word

space:
O(L): stack for recursion call

'''