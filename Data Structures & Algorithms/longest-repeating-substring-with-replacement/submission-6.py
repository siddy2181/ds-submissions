class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        charFreq = {}
        l=0

        for r in range(len(s)):
            charFreq[s[r]] = charFreq.get(s[r],0)+1

            maxFreq = max(charFreq.values())
            if (r-l+1 - maxFreq) > k:
                charFreq[s[l]] -= 1
                l += 1
            result = max(result, r-l+1)


        return result


        