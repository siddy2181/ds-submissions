class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        l = 0
        result = 0
        for r in range(len(s)):
            if(s[r] in charMap):
                l = max(charMap[s[r]] +1, l)
            charMap[s[r]] = r
            result = max(result, r-l+1)

        return result