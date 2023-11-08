'''
Given 2 strings s and t, return true if t is an anagram of s, and false otherwise

An anagram is a word or phrase form by rearranging the letters of a different word or phrase, typically using all the original letters exactly one

'''

def isAnagram(s, t):

    d = {}

    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    for c in t:
        if c in d:
            d[c] -= 1
        else:
            d[c] = 1

    for v in d.values():
        if v != 0:
            return False
    return True


s1 = "anagram"
t1 = "nagaram"

s2 = "rat"
t2 = "car"

print(isAnagram(s1, t1))
print(isAnagram(s2, t2))

''''
runtime: O(n)
space: O(n)
'''
