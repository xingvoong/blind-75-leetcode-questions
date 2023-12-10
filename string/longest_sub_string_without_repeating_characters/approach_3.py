def lengthOfLongestSubstring(s):
    chars = [None] * 128

    left = right = 0

    res = 0
    while right < len(s):
        r = s[right]

        index = chars[ord(r)]
        if index is not None and left <= index <= right:
            left = index + 1

        res = max(res, right - left + 1)

        chars[ord(r)] = right
        right += 1

    return res


s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
print(lengthOfLongestSubstring(s1))
print(lengthOfLongestSubstring(s2))
print(lengthOfLongestSubstring(s3))