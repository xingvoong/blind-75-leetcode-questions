'''
Given a string s, return the longest palindromic substring in s


Example 1:
input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"


Algo:
- check all substrings
- since we want the longest substring palindrom, it's good
to start from the end, longest string first
- use helper isPalindrome for help

'''

def longestPalindrome(s):

    def isPalindrome(i, j):
        left = i
        right = j - 1

        while left <= right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        return True

    for length in range(len(s), 0, -1):
        for start in range(len(s) - length + 1):
            if isPalindrome(start, start + length):
                return s[start:start+length]

    return ""

s1 = "babad"
s2 = "cbbd"
print(longestPalindrome(s1))
print(longestPalindrome(s2))

