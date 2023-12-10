''''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter
you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
output: 4
explanation: replace the two 'A's with two 'B's or vice versa

Example 2:
input: s = "AABABBA", k = 1
output: 4
Explanation: replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
'''
def characterReplacement(s, k):
    count = {}
    res = 0

    l = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)

    return res
s1 = "ABAB"
k1 = 2

s2 = "AABABBA"
k2 = 1
print(characterReplacement(s1, k1))
print(characterReplacement(s2, k2))


