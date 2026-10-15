class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        subS = set()
        l = 0

        for r in range(len(s)):

            while(s[r] in subS):
                subS.remove(s[l])
                l+=1

            subS.add(s[r])
            result = max(result, r-l+1)
        return result