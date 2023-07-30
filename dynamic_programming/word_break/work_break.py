'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into space-separated sequence of one or more dictionary words.

Note: the same word in the dictionary may be reused multiple times in the segmentation.

Example:
input: s = "leetcode", wordDict = ["leet", "code"]
output: true
explanation: return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s  = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: return true because "applepenapple" can be segmented as "apple pen apple"
Note: you are allowed to reuse a dictionary word

Example 3:
Input: s = "catsanddog", wordDict = ["cats", "dog", "sand", "and", "cat"]
output: false


print(wordBreak("leetcode", ["leet", "code"]))

'''

from functools import cache


def wordBreak(s, wordDict):
    @cache
    def dp(i):
        if i < 0:
            return True

        for word in wordDict:
            print("i", i)
            print("word lenght", len(word))
            print(i - len(word)+1)
            print(i+1)
            print(s[i-len(word)+1:i+1])
            # if s[i-len(word)+1:i+1] == word and dp(i-len(word)):
            #     print("inside if",s[i-len(word)+1:i+1])
            #     return True

        return False
    return dp(len(s) - 1)


print(wordBreak("leetcode", ["leet", "code"]))

