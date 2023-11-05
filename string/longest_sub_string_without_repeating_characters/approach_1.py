'''
Given a string s, find the length of the longest substring without
repeating characters

example 1:
I: s = "abcabcbb"
O: 3
explanation: the answer is "abc", with the length of 3

example 2:
input: s = "bbbbbb"
output: 1
explanation: the answer is "b", with the length of 1

example 3:
input: s = "pwwkew"
output: 3
explanation: the answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Approach 1:
check all duplicate
'''


def lengthOfLongestSubstring(s):

    def checkDuplicate(start, end):
        chars = set()
        for i in range(start, end+1):
            c = s[i]
            if c in chars:
                return False
            chars.add(c)
        return True

    n = len(s)

    result = 0

    for i in range(n):
        for j in range(i, n):
            if checkDuplicate(i, j):
                result = max(result, j - i + 1)

    return result

s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
print(lengthOfLongestSubstring(s1))
print(lengthOfLongestSubstring(s2))
print(lengthOfLongestSubstring(s3))

'''
time: O(n^3)
space: O(N)

'''