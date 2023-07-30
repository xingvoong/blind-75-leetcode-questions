'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde"

A common subsequence of two strings is a subsequence that is common to both strings

Example 1:
input: text1 = "abcde", text2 = "ace"
output: 3
Explanation: the longest common subsequence is "ace" and it's lenghth is 3

Example 2:
input: text1 = "abc", text2 = "abc"
output: 3
explanation: the longest common subsequence is "abc" and it's length is 3

example 3:
input: text1 = "abc", text2 = "def"
output: 0
explantation: there is so such common subsequence, so the result is 0

constraints:
- 1 <= text1.length, text2.length <= 1000
'''