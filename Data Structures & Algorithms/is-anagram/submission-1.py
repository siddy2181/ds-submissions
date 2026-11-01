class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}
        if len(s) != len(t): return False
        for char in s:
            anagram[char] = anagram.get(char,0)+1

        for char in t:
            if char not in anagram:
                return False
            else:
                anagram[char]-=1
        for i in anagram.values():
            if i != 0:
                return False
        return True
