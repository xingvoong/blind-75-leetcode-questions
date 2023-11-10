'''
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

'''

def isPalindrome(s):

    #filter
    s = s.lower()

    #Alphanumeric characters include letters and numbers.

    #s = "".join(c for c in s if c.isalnum())
    temp = []
    for c in s:
        if c.isalnum():
            temp.append(c)
    s = "".join(temp)
    l = 0
    r = len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "
s4 = "???!!!"
print(isPalindrome(s1))
print(isPalindrome(s2))
print(isPalindrome(s3))
print(isPalindrome(s4))

'''
runtime: O(N)
space: O(N) if use temp
O(1) if not using temp


'''
