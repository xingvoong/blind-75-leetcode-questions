
class Solution:
    def countSubstrings(self, s: str) -> int:
        self.ans = 0

        def expand(l, r):
            global ans
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

                self.ans += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return self.ans

S = Solution()
print(S.countSubstrings("fdsklf"))
print(S.countSubstrings("aaa"))

'''
time: O(N^2)
space: O(1)

expand around center gives the best result for strings problems
'''

