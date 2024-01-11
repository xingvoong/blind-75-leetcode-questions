''''
given a string, return the number of palindromic substrings in it.

a string is a palindrome when it reads the same backward as forward.
a substring is a contiguous sequence of characters within the string
'''
def countSubstring(s):
    def isPalindrome(s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True

    ans = 0
    for start in range(0, len(s)):
        for end in range(start, len(s)):
            if isPalindrome(s, start, end):
                ans += 1
    return ans

print(countSubstring("abc"))
print(countSubstring("aaa"))