class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for num in numSet:
            if (num-1) not in numSet:
                temp =1
                while(num+temp in numSet):
                    temp +=1
                longest = max(temp,longest)
        return longest
                