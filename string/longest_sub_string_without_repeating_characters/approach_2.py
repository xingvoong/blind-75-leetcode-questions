'''
Approach 2: sliding window

Intuition

Given a substring with a fixed end index in the string, maintain a HashMap to record the frequency of each character in the current substring. If any character occurs more than once, drop the leftmost characters until there are no duplicate characters.

'''
from collections import Counter
def lengthOfLongestSubstring(s):
    chars = Counter()

    left = right = 0

    result = 0
    while right < len(s):
        r = s[right]
        chars[r] += 1

        while chars[r] > 1:
            l = s[left]
            chars[l] -= 1
            left += 1

        result = max(result, right - left + 1)

        right += 1
    return result


s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
print(lengthOfLongestSubstring(s1))
print(lengthOfLongestSubstring(s2))
print(lengthOfLongestSubstring(s3))

'''
runtime: O(N)
space: O(N)

'''