'''
dp solution

'''

def countSubstring(s):
    if not s: return None

    n = len(s)
    ans = 0

    dp = [[False] * n for _ in range(n)]

    #dp[i][j] depends on dp[i+1][j]
    # so check larger i first
    for i in reversed(range(n)):
        for j in range(i, n):
            if j - i < 2 and s[i] == s[j]:
                dp[i][j] = True
                ans += 1
            elif dp[i+1][j-1] and s[i] == s[j]:
                dp[i][j] = True
                ans += 1

    return ans

print(countSubstring("fdsklf"))
print(countSubstring("aaa"))

'''
runtime: O(N^2)
space: O(N^2)

'''
