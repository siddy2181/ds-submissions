class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}
        # iterate over the string add it to the set <value, count>
        for i in s:
            anagram[i] = anagram.get(i,0) +1
        print(anagram)
        # iterate over the 2nd string and check the key
        for j in t:
            # Present? => reduce the count
            if(j in anagram):
                anagram[j]=anagram.get(j)-1
            # Not Present? => return False
            else:
                return False
        print(all(j==0 for j in anagram.values()))
        # Check if all character count is 0 return Bool 
        return all(j==0 for j in anagram.values())
        