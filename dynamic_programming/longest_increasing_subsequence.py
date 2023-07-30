'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Input:
nums = [10, 9, 2, 5, 3, 7, 101, 18]

'''

from functools import lru_cache
class Solution:
    def longestCommonSubsequence(text1, text2):

        @lru_cache(maxsize=None):
        def memo_solve(p1, p2):

            # base case: if either string is now empty, we can't match
            if p1 == len(text1) or p2 == len(text2):
                return 0

            # recursive case 1
            if text1[p1] ==  text2[2]:
                return 1 + memo_solve(p1 + 1, p2 + 1)

            # recursive case 2
            else:
                return max(memo_solve(p1, p2+1), memo_solve(p1+1, p2))

        return memo_solve(0, 0)


