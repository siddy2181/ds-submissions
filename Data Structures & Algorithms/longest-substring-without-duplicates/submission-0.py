class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        char_set = collections.deque()
        for j in range(len(s)):
            while s[j] in char_set:
                char_set.remove(s[l])
                l+=1
            char_set.append(s[j])
            longest=max(longest,j-l+1)
        return longest


