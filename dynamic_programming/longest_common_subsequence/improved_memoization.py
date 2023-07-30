from functools import lru_cache
def longestCommonSubsequence(text1, text2):
    @lru_cache(maxsize=None)
    def memo_solve(p1, p2):

        # base case: if either string is now empty, we can't match
        # up anymore characters
        if p1 == len(text1) or p2 == len(text2):
            return 0

        # recursive case 1
        if text1[p1] == text2[p2]:
            return 1 + memo_solve(p1+1, p2+1)

        # recursive case 2
        else:
            return max(memo_solve(p1, p2+1), memo_solve(p1+1, p2))

    return memo_solve(0, 0)


'''
Time: O(M.N)

This time, solve each subproblem has a cost of O(1). Again there are M.N subproblems, and so we get a total time complexity of O(M.N)



'''