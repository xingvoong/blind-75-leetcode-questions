import unittest
def longestCommonSubsequence(text1, text2):

    # make a 2D grid with col =  len(text2) + 1
    # and row = len(text1) + 1
    dp = [[0] * (len(text2)+1) for _ in range(len(text1) + 1)]

    # traverse the grid

    for col in reversed(range(len(text2))):
        for row in reversed(range(len(text1))):
            # if the characters are the same
            # text2[col] == text1[rol]
            if text2[col] == text1[row]:
                dp[row][col] = 1 + dp[row+1][col+1]
            # if the characters are not the same
            else:
                dp[row][col] = max(dp[row+1][col], dp[row][col+1])

    # return result
    return dp[0][0]


print(longestCommonSubsequence("abcde", "ace"))
print(longestCommonSubsequence("abc", "abc"))
print(longestCommonSubsequence("abc", "def"))

