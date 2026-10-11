class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ABBCBA
        l = 0
        freqMap = {}
        result = 0

        for r in range(len(s)):
            # check condition
            freqMap[s[r]] = freqMap.get(s[r],0)+1
            # if valid
            maxFreq = max(freqMap.values())
            windowLen = (r-l)+1
            if windowLen - maxFreq<= k:
                result = max(result, windowLen)
            # not valid
            else:
                freqMap[s[l]] -=1
                l+=1
        return result


